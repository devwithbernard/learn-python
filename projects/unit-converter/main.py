import utils

def main() -> None:
    """Main function to run the unit converter application.

    Prompts user for conversion choice and input value, then performs
    the selected conversion and displays the result. Includes error
    handling for invalid input and user interruption.
    """
    try:
        choice = utils.get_user_choice()

        if choice == '1':
            # Celsius to Fahrenheit conversion
            celsius = float(input("Enter the temperature in Celsius: "))
            fahrenheit = utils.celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit}°F")

        elif choice == '2':
            # Kilometer to meter conversion
            kilometers = float(input("Enter the distance in kilometers: "))
            meters = utils.kilometer_to_meter(kilometers)
            print(f"{kilometers} km = {meters} m")

    except ValueError:
        print("Error: Please enter a valid numerical value!")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def run_converter() -> None:
    """Run the converter with option to restart.

    Allows users to perform multiple conversions without restarting
    the program. Continues until user chooses to exit.
    """
    print("=== Unit Converter ===")

    while True:
        main()

        try:
            restart = input("\nDo you want to perform another conversion? (y/n): ").lower().strip()
            if restart not in ('y', 'yes'):
                print("Thank you for using the Unit Converter!")
                break
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    run_converter()