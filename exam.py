class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def P(self):
        P = self.width * 2 + self.length * 2
    def S(self):
        S = self.width * self.length

R = Rectangle(10, 15)
print(R.S())

