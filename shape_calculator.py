class Rectangle:
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width
    
  def set_height(self, height):
    self.height = height
    
  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    output = ""
    if self.width <= 50 and self.height <= 50:
      for count in range(self.height):
        output += "*" * self.width
        output += "\n"
    else:
      return "Too big for picture."
    return output

  def get_amount_inside(self, shape):
    return self.get_area() // shape.get_area()
    
class Square(Rectangle):
  def __init__(self, side_length):
    super().__init__(width = side_length, height = side_length)
    #self.width = side_length
    #self.height = side_length
    
  def set_side(self, side_length):
    super().__init__(width = side_length, height = side_length)
    #self.width = side_length
    #self.heigth = side_length

  def __str__(self):
    return f"Square(side={self.width})"