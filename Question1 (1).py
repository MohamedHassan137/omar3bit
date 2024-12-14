class Stack:
    def __init__(self, size=80):  # Fix: Constructor method should be init
        self.stack = []  # Initialize an empty list to act as the stack
        self.size = size  # Optional: If you want to limit stack size, otherwise remove this

    def push(self, item):
        self.stack.append(item)  # Add the item to the stack

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the top item from the stack
        else:
            return None  # If the stack is empty, return None

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Return the top item without removing it
        return None  # If the stack is empty, return None


def check_balanced_parentheses(input_string):
    stack = Stack()  # Create an instance of the Stack class
    
    # Iterate through each character in the input string
    for char in input_string:
        # Ignore non-parenthesis characters (you can remove or modify this condition as needed)
        if char not in '()[]{}':
            print("Illegal char in input")
            return
        
        # If the character is an opening bracket, push it to the stack
        if char in '({[':
            stack.push(char)
        
        # If the character is a closing bracket, check for balance
        elif char in ')}]':
            if stack.is_empty():
                print("Not Balanced")
                return
            top = stack.pop()
            # Check if the popped item matches the closing bracket
            if (top == '(' and char != ')') or (top == '{' and char != '}') or (top == '[' and char != ']'):
                print("Not Balanced")
                return

    # After processing the entire string, check if the stack is empty
    if stack.is_empty():
        print("Properly Nested structure")
    else:
        print("Not Balanced")


# Test the function with some examples
check_balanced_parentheses("({[]})")  # Properly Nested structure
check_balanced_parentheses("((([])")  # Not Balanced
check_balanced_parentheses("(0)")  #Illegal char in input 
input_string = input("Enter a parenthesis string: ")
check_balanced_parentheses(input_string)