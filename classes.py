class Point:
    # self a variable that represent "self",
    # the object that we are creating
    # other words, here , self is the name,
    # referring to the point object that we have just created
    # self.x accessing the particular attribute of self object i.e. created
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 5)
# accessing x and y attribute of self or p object
print(p.x)
print(p.y)
