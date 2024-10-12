class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    # Define the iteration method
    def __iter__(self):
        # Using a list of key-value pairs to match the required format
        yield {'length': self.length}
        yield {'width': self.width}


# Example usage:
rectangle = Rectangle(5, 10)

# Iterate over the instance of Rectangle
for attribute in rectangle:
    print(attribute)
