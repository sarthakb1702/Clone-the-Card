import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def main():
    parser = argparse.ArgumentParser(
        description="Convert temperatures between Celsius and Fahrenheit."
    )
    
    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument(
        "--c2f", type=float, metavar="C", 
        help="Convert Celsius to Fahrenheit. Provide the Celsius value."
    )
    
    group.add_argument(
        "--f2c", type=float, metavar="F", 
        help="Convert Fahrenheit to Celsius. Provide the Fahrenheit value."
    )
    
    args = parser.parse_args()
    
    if args.c2f is not None:
        f = celsius_to_fahrenheit(args.c2f)
        print(f"{args.c2f}°C = {f:.2f}°F")
        
    elif args.f2c is not None:
        c = fahrenheit_to_celsius(args.f2c)
        print(f"{args.f2c}°F = {c:.2f}°C")

if __name__ == "__main__":
    main()
