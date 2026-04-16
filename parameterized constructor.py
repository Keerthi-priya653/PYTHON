class person:
    def __init__ (self, name, age):
        self.name=name
        self.age=age
    def display(self):
        print("name is:",self.name)
        print("age is:",self.age)
p1=person("madhu",24)
p1.display()


class add:
    def __init__ (self, a, b):
        self.a=a
        self.b=b
    def display(self):
        print(self.a +self.b)
        
p1=add(4,6)
p1.display()
