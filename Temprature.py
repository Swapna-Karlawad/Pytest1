def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def main():
    try:
        celsius = float(input("Enter temperature in Celsius: "))
    except EOFError:
        print("No input provided. Skipping user input.")
        return

    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"Celsius: {celsius}")
    print(f"Fahrenheit: {fahrenheit}")


if __name__ == "__main__":
    main()
