import os
import subprocess
import argparse
import logging
import requests
import json

class SPKG:
    def __init__(self):
        self.aur_dir = "/tmp/aur_packages"
        if not os.path.exists(self.aur_dir):
            os.makedirs(self.aur_dir)
        self.setup_logging()

    def setup_logging(self):
        logging.basicConfig(filename='spkg.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def run_command(self, command, verbose=False):
        try:
            result = subprocess.run(command, check=True, capture_output=True, text=True, timeout=300)
            if verbose:
                print(result.stdout)
            logging.info(f"Command executed successfully: {' '.join(command)}")
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            logging.error(f"Command failed: {' '.join(command)} - {e}")
        except subprocess.TimeoutExpired as e:
            print(f"Error: Command timed out: {' '.join(command)}")
            logging.error(f"Command timed out: {' '.join(command)} - {e}")

    def update(self):
        print("Updating system and AUR packages...")
        self.run_command(["sudo", "pacman", "-Syu", "--noconfirm"])

    def install(self, pkg_name, verbose=False):
        print(f"Installing {pkg_name}...")
        pkg_dir = os.path.join(self.aur_dir, pkg_name)
        if not os.path.exists(pkg_dir):
            self.run_command(["git", "clone", f"https://aur.archlinux.org/{pkg_name}.git", pkg_dir], verbose)
        try:
            os.chdir(pkg_dir)
            print(f"Changed directory to {pkg_dir}")
            self.run_command(["makepkg", "-si", "--noconfirm"], verbose)
        except Exception as e:
            print(f"Error changing directory: {e}")
            logging.error(f"Error changing directory: {e}")

    def remove(self, pkg_name, confirm=True):
        if confirm:
            user_input = input(f"Are you sure you want to remove {pkg_name}? (y/n): ").lower()
            if user_input != 'y':
                print("Removal cancelled.")
                return
        print(f"Removing {pkg_name}...")
        self.run_command(["sudo", "pacman", "-Rns", pkg_name, "--noconfirm"])

    def clean_up(self):
        print("Cleaning up AUR cache...")
        self.run_command(["rm", "-rf", self.aur_dir])

    def search(self, query, verbose=False):
        print(f"Searching for {query}...")

        url = f"https://aur.archlinux.org/rpc/?v=5&type=search&arg={query}"
        response = requests.get(url)
        if response.status_code == 200:
            results = response.json().get("results", [])
            for result in results:
                print(f"{result['Name']} - {result['Description']}")
                if verbose:
                    print(f"    Version: {result['Version']}")
                    print(f"    URL: {result['URL']}")
        else:
            print(f"Error: Unable to search for {query}. HTTP status code: {response.status_code}")
            logging.error(f"Error searching for {query}. HTTP status code: {response.status_code}")

    def list_installed(self):
        print("Listing installed AUR packages...")
        self.run_command(["pacman", "-Qm"])

def main():
    parser = argparse.ArgumentParser(description="Silkpackage (SPKG) - AUR Helper")
    parser.add_argument('-u', '--update', action='store_true', help='Update system and AUR packages')
    parser.add_argument('-i', '--install', metavar='PKG', help='Install package')
    parser.add_argument('-r', '--remove', help='Remove package')
    parser.add_argument('-c', '--clean', action='store_true', help='Clean AUR cache')
    parser.add_argument('-s', '--search', metavar='QUERY', help='Search for a package')
    parser.add_argument('-l', '--list', action='store_true', help='List installed AUR packages')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')

    args = parser.parse_args()
    spkg = SPKG()

    if args.update:
        spkg.update()
    elif args.install:
        spkg.install(args.install, args.verbose)
    elif args.remove:
        spkg.remove(args.remove)
    elif args.clean:
        spkg.clean_up()
    elif args.search:
        spkg.search(args.search, args.verbose)
    elif args.list:
        spkg.list_installed()
    else:
        print("No valid option provided. Use -h for help.")

if __name__ == "__main__":
    main()