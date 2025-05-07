import turtle

#Step 2: Factorial Function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
#Step 3: Fibonacci Function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#Step 4: Recursive Fractal Pattern (Bonus)
def draw_tree(t, size):
    if size < 10:
        return
    else:
        t.forward(size)
        t.left(30)
        draw_tree(t, size - 15)
        t.right(60)
        draw_tree(t, size - 15)
        t.left(30)
        t.backward(size)

#Step 1: Menu of Recursive Functions
print("Welcome to the Recursive Artistry Program!")
while True:
    print("Choose an option:")
    print("1. Calculate Factorial")
    print("2. Find Fibonacci")
    print("3. Draw a Recursive Fractal")
    print("4. Exit")
    choice = input("> ")

    if choice == "1":
        try:
            number = int(input("Enter a number to find its factorial: "))
            if number < 0:
                print("Please enter a non-negative integer.")
            else:
                result = factorial(number)
                print(f"The factorial of {number} is {result}.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        try:
            position = int(input("Enter the position of the Fibonacci number: "))
            if number < 0:
                print("Please enter a non-negative integer.")
            else:
                result = fibonacci(position)
                print(f"The {position}th Fibonacci number is {result}.")
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "3":
        screen = turtle.Screen()
        screen.bgcolor("white")
        t = turtle.Turtle()
        t.left(90)
        t.speed(0)
        draw_tree(t, 100)
        screen.mainloop()
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid option. Please select again.")