class vechicles:
    def move(self):
        print("vechicles are move")
class car(vechicles):
    def drive(self):
        print("drive from one place to another")
class bike(vechicles):
    def ride(self):
        print("bike rides")
c=car()
c.drive()
c.move()
b=bike()
b.ride()
b.move()

