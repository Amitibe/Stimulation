class creature:
    def __init__(self,name):
       self.name = name
       self.speed = 10
       self.hunger = 3
       self.color = (0, 0, 0)
       self.x_dr = 0
       self.y_dr = 0
       self.y = 0
       self.x = 0
       self.hunger = 0
       self.protection_chance = 0
       self.radius = 15
    def get_protection_chance(self):
        return self.protection_chance
    def get_hunger(self):
        return self.hunger
    def get_name(self):
        return self.name
    def get_radius(self):
        return self.radius
    def get_color(self):
        return self.color
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_xdr(self):
        return self.x_dr
    def get_ydr(self):
        return self.y_dr
    def get_speed(self):
        return self.speed
    def set_hunger(self,h):
        self.hunger = h
    def set_speed(self,speed):
        self.speed = speed
    def set_x(self,x):
        self.x = x
    def set_protection_chance(self,c):
        self.protection_chance = c
    def set_y(self,y):
        self.y=y
    def set_color(self,color):
        self.color = color
    def set_x_dr(self,x):
        self.x_dr = x
    def set_y_dr(self,y):
        self.y_dr = y
    def set_radius(self,r):
        self.radius = r

class food:
    def __init__(self):
        self.radius = 7
        self.color = (255, 0, 0)
        self.x = 0
        self.y = 0
    def get_radius(self):
        return self.radius
    def get_color(self):
        return self.color
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y=y
    def set_color(self,color):
        self.color = color
    def set_radius(self,r):
        self.radius = r

class hunter:
    def __init__(self,name):
       self.name = name
       self.speed = 10
       self.hunger = 3
       self.color = (0, 0, 0)
       self.x_dr = 0
       self.y_dr = 0
       self.y = 0
       self.x = 0
       self.hunger = 0
       self.radius = 16
    def get_hunger(self):
        return self.hunger
    def get_name(self):
        return self.name
    def get_radius(self):
        return self.radius
    def get_color(self):
        return self.color
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_xdr(self):
        return self.x_dr
    def get_ydr(self):
        return self.y_dr
    def get_speed(self):
        return self.speed
    def set_hunger(self,h):
        self.hunger = h
    def set_speed(self,speed):
        self.speed = speed
    def set_x(self,x):
        self.x = x
    def set_y(self,y):
        self.y=y
    def set_color(self,color):
        self.color = color
    def set_x_dr(self,x):
        self.x_dr = x
    def set_y_dr(self,y):
        self.y_dr = y
    def set_radius(self,r):
        self.radius = r