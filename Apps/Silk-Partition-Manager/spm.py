# Silk Partition Manager Version 0.1 by Silk
import subprocess
import curses

class SilkPartitionManager:
    def __init__(self, stdscr):
        self.parted_command = "parted /dev/sda"
        self.stdscr = stdscr

    def run_command(self, command):
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e.stderr}"

    def list_partitions(self):
        return self.run_command(f"{self.parted_command} print")

    def create_partition(self, start, end, fs_type):
        return self.run_command(f"{self.parted_command} mklabel gpt mkpart primary {fs_type} {start} {end}")

    def delete_partition(self, partition):
        return self.run_command(f"{self.parted_command} rm {partition}")

    def format_partition(self, partition, fs_type):
        return self.run_command(f"mkfs -t {fs_type} {partition}")

    def display_menu(self):
        self.stdscr.clear()
        self.stdscr.addstr(0, 0, "Silk Partition Manager (SPM)")
        self.stdscr.addstr(2, 0, "1. List Partitions")
        self.stdscr.addstr(3, 0, "2. Create Partition")
        self.stdscr.addstr(4, 0, "3. Delete Partition")
        self.stdscr.addstr(5, 0, "4. Format Partition")
        self.stdscr.addstr(6, 0, "5. Exit")
        self.stdscr.refresh()

    def get_input(self, prompt):
        self.stdscr.addstr(8, 0, prompt)
        self.stdscr.refresh()
        curses.echo()
        input_str = self.stdscr.getstr(9, 0).decode('utf-8')
        curses.noecho()
        self.stdscr.clear()
        return input_str

    def run(self):
        while True:
            self.display_menu()
            choice = self.stdscr.getch()
            self.stdscr.clear()
            if choice == ord('1'):
                self.stdscr.addstr(7, 0, self.list_partitions())
            elif choice == ord('2'):
                start = self.get_input("Start (e.g., 1MiB): ")
                end = self.get_input("End (e.g., 10GiB): ")
                fs_type = self.get_input("Filesystem Type (e.g., ext4): ")
                self.stdscr.addstr(7, 0, self.create_partition(start, end, fs_type))
            elif choice == ord('3'):
                partition = self.get_input("Partition to delete: ")
                self.stdscr.addstr(7, 0, self.delete_partition(partition))
            elif choice == ord('4'):
                partition = self.get_input("Partition to format: ")
                fs_type = self.get_input("Filesystem Type (e.g., ext4): ")
                self.stdscr.addstr(7, 0, self.format_partition(partition, fs_type))
            elif choice == ord('5'):
                break
            self.stdscr.refresh()

def main(stdscr):
    spm = SilkPartitionManager(stdscr)
    spm.run()

if __name__ == "__main__":
    curses.wrapper(main)