class Taxicab:
    def __init__(self,x_coordinate, y_coordinate):
        self._x_coordinate = x_coordinate
        self._y_coordinate = y_coordinate
        self._odometer = 0

    def get_x_coord(self):
        return self._x_coordinate

    def get_y_coord(self):
        return self._y_coordinate

    def get_odometer(self):
        return self._odometer

    def move_x(self, new_x):
        self._x_coordinate += new_x
        self._odometer += abs(new_x)
    
    def move_y(self, new_y):
        self._y_coordinate += new_y
        self._odometer += abs(new_y)
    
taxi_1 = Taxicab(5, -8)
print(taxi_1.get_x_coord())
print(taxi_1.get_y_coord())
taxi_1.move_x(3)              
taxi_1.move_y(-4)              
print(taxi_1.get_x_coord(), 'x')
print(taxi_1.get_y_coord(), 'y')
print(taxi_1.get_odometer(), "Here")