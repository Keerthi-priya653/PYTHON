#polymorphism
class methover:
    def add(self,datatype,*args):
        if(datatype=='int'):
           answer=0
        if(datatype=='str'):
           answer=''
        for x in args:
           answer=answer + x
        print(answer)
a=methover()    
a.add('int',5,15,25)
a.add('str','computer','science')
    
