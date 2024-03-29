import math

class My_shape:
    def __init__(self, color="black", is_filled=False):
        self.color = color
        self.is_filled = is_filled

    def __str__(self):
        filled_str = "filled" if self.is_filled else "not filled"
        return f"Shape color: {self.color}, Shape is {filled_str}"

    def getArea(self):
        return 0

class Rectangle(My_shape):
    def __init__(self, color="black", is_filled=False, x_top_left=0, y_top_left=0, length=0, width=0):
        super().__init__(color, is_filled)
        self.x_top_left = x_top_left
        self.y_top_left = y_top_left
        self.length = length
        self.width = width

    def __str__(self):
        return (f"Rectangle: Color={self.color}, Filled={self.is_filled}, "
                f"Top Left: ({self.x_top_left}, {self.y_top_left}), "
                f"Length={self.length}, Width={self.width}")

    def getArea(self):
        return self.length * self.width

def create_rectangle_from_input():
    color = input("Enter color of rectangle: ")
    is_filled = input("Is the rectangle filled? (True/False): ").lower() == 'true'
    x_top_left = float(input("Enter x-coordinate of top-left corner: "))
    y_top_left = float(input("Enter y-coordinate of top-left corner: "))
    length = float(input("Enter length of rectangle: "))
    width = float(input("Enter width of rectangle: "))
    return Rectangle(color, is_filled, x_top_left, y_top_left, length, width)


rectangle1 = create_rectangle_from_input()
print(rectangle1)
print("Rectangle Area:", rectangle1.getArea())
