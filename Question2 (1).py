# Stack class definition
class Stack:
    def __init__(self, size=80):
        self.stack = []  # The stack will be implemented using a list
        self.size = size  # Optional size limit, though Python lists don't need it

    def push(self, item):
        self.stack.append(item)  # Push an item onto the stack

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Pop the top item from the stack
        else:
            return None  # Return None if the stack is empty

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # Return the top item without removing it
        return None  # Return None if the stack is empty


# Function to invert a string using a stack
def invert_string(input_string):
    stack = Stack()  # Create an instance of the Stack class
    
    # Push each character of the input string onto the stack
    for char in input_string:
        stack.push(char)
    
    # Pop each character from the stack to form the inverted string
    inverted_string = ''
    while not stack.is_empty():
        inverted_string += stack.pop()  # Pop and append to the inverted string
    
    return inverted_string


# Main code to test the invert_string function
def main():
    # Test 1
    input_string = "abcdefghij"
    print(f"Input String is: {input_string}")
    inverted_string = invert_string(input_string)
    print(f"Inverted String is: {inverted_string}")

    # Test 2
    input_string = "123456789"
    print(f"\nInput String is: {input_string}")
    inverted_string = invert_string(input_string)
    print(f"Inverted String is: {inverted_string}")
    input_string2 = input("Enter an input string: ")
    inverted_string2 = invert_string(input_string2)
    print(f"Inverted String is: {inverted_string2}")

# Call the main function to test the implementation
if __name__ == "__main__":
    main()