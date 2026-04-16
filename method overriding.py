class mother:
    def parent(self):
        print("this is base class")
class child(mother):
    def parent(self):
         super().parent()
         print("this is child class")  
ch=child()
ch.parent() 

        
class animal:
    def sound(self):
        print("animal make sound")
class mammal(animal):
    def make_sound(self):
        print("mammals make sound")
class dog:
    def makes_sound(self):
        print("dog make sound")
obj=animal()
obj.make_sound()
obj.dog()
obj.make_sound()
