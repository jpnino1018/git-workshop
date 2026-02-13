def calculate():
    # Number 1
    num1 = float(input("Enter the first number: "))
    # Number 2
    num2 = float(input("Enter the second number: "))
    # Operation (Add or subtract)
    operation = input("Enter the operation (+ or -): ")
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    else:
        print("Invalid operation")
        return
    print(f"The result is: {result}")

if __name__ == "__main__":
    calculate()