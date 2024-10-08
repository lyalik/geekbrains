class Rectangle:
    """
    Класс для управления прямоугольником.

    >>> rect = Rectangle(3, 4)
    >>> rect.get_area()
    12
    >>> rect.get_perimeter()
    14

    >>> rect.set_dimensions(5, 6)
    >>> rect.get_area()
    30
    >>> rect.get_perimeter()
    22

    >>> rect.set_dimensions(-1, 2)
    Traceback (most recent call last):
        ...
    ValueError: Ширина и высота должны быть неотрицательными.

    >>> rect.set_dimensions(0, 0)
    >>> rect.get_area()
    0
    >>> rect.get_perimeter()
    0
    """

    def __init__(self, width, height):
        self.set_dimensions(width, height)

    def set_dimensions(self, width, height):
        if width < 0 or height < 0:
            raise ValueError("Ширина и высота должны быть неотрицательными.")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

if __name__ == "__main__":
    import doctest
    doctest.testmod()