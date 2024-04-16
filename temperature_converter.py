import celsius_converter
import fahrenheit_converter

def main():
    print("Welcome to Simple Temperature Converter!\n")
    
    while True:
        print("Select conversion direction:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius\n")
        
        choice = input("Enter your choice (1/2): ")
        
        if choice == '1':
            temp_celsius = float(input("Enter temperature in Celsius: "))
            converted_temp = celsius_converter.to_other_unit(temp_celsius)
            print(f"\nResult: {temp_celsius}°C is equal to {converted_temp}°F.\n")
        elif choice == '2':
            temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            converted_temp = fahrenheit_converter.to_other_unit(temp_fahrenheit)
            print(f"\nResult: {temp_fahrenheit}°F is equal to {converted_temp}°C.\n")
        else:
            print("Invalid choice!\n")
            continue
        
        another_conversion = input("Do you want to convert another temperature? (yes/no): ")
        if another_conversion.lower() != 'yes':
            break
    
    print("\nThank you for using Simple Temperature Converter!")

if __name__ == "__main__":
    main()
