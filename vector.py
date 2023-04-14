class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, vec):
        return Vector(self.x + vec.x, self.y + vec.y)

    def __iadd__(self, vec):
        self.x += vec.x
        self.y += vec.y
        return self
    
    def __sub__(self, vec):
        return Vector(self.x - vec.x, self.y - vec.y)
    
    def __isub__(self, vec):
        self.x -= vec.x
        self.y -= vec.y
        return self

    def __mul__(self, num):
        return Vector(self.x * num, self.y * num)
    
    def __imul__(self, num):
        self.x *= num
        self.y *= num
        return self
    
    def __truediv__(self, num):
        return Vector(self.x / num, self.y / num)
    
    def __itruediv__(self, num):
        self.x /= num
        self.y /= num
        return self
    
    def normalize(self):
        magnitude = (self.x**2 + self.y**2)**0.5
        if magnitude != 0:
            self.x /= magnitude
            self.y /= magnitude
        return self
        