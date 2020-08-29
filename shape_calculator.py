class Rectangle:
    def __init__(self, width: float, height: float):
        self.height = height
        self.width = width
    
    def set_width(self, width: float):
        self.width = width
    
    def set_height(self, height: float):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})" 


class Square(Rectangle):
    def __init__(self, side: float):
        self.side = side
        super().__init__(side, side)

    def set_side(self, side: float):
        self.side = side
        self.set_width = side
        self.set_height = side

    def __repr__(self):
        return f"Square(side={self.side})"

