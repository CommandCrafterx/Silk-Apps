# Average Rate Calculator

# Initialize an empty list to store numbers
numbers = []

# Function to calculate the average rate of a list of numbers
def calculate_average_rate(numbers_list):
    if not numbers_list:
        return 0
    total = sum(numbers_list)
    return total / len(numbers_list)

# Function to get valid input from the user
def get_valid_input():
    while True:
        try:
            user_input = input("Enter a number: ")
            if user_input.lower() == 'exit':
                print("Goodbye!")
                break
            num = int(user_input)
            numbers.append(num)
            print(f"Current list: {numbers}")
            print(f"Current average rate: {calculate_average_rate(numbers)}")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Main function to run the rate calculator
def main():
    print("Welcome to the Average Rate Calculator!")
    print("Type 'exit' to quit.")
    get_valid_input()

# Run the main function
if __name__ == "__main__":
    main()