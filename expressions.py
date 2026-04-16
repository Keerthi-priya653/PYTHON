Python 3.13.12 (tags/v3.13.12:1cbe481, Feb  3 2026, 18:22:25) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=4
b=2.5
c=a+b
print(c)
6.5
print(type(b))
<class 'float'>
print(type(a))
<class 'int'>
a='12'
print(type(a))
<class 'str'>
b=6
a=int(a)
sum=a*a
print(sum)
144
print(type(a))
<class 'int'>
b=float(b)
print(type(b))
<class 'float'>
a=10
b=7.5
c=7+5i
SyntaxError: invalid decimal literal
c=6+2i
SyntaxError: invalid decimal literal
c=5+6j
print(type(a))
<class 'int'>
print(type(b))
<class 'float'>
print(type(c))
<class 'complex'>
b=int(b)
print(type(b))
<class 'int'>
c=int(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    c=int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
print(type(c))
<class 'complex'>
ab='cse'
print(type(a))
<class 'int'>
print(type(ab))
<class 'str'>
print('the usage of single quation',ab)
the usage of single quation cse
>>> print("the usage of single quation",ab)
the usage of single quation cse
>>> print('''this is multiline''')
this is multiline
>>> a=[2,3,6,7]
>>> print(a)
[2, 3, 6, 7]
>>> print(type(a))
<class 'list'>
>>> b=(4,6,8,9)
>>> print(type(b))
<class 'tuple'>
>>> c={7,4,1,6}
>>> print(type(c))
<class 'set'>
>>> print(c)
{1, 4, 6, 7}
>>> a=[2,3,4,5]
>>> print(a[1])
3
>>> print(a[3])
5
>>> print(a[2]=6)
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
>>> print(a)
[2, 3, 4, 5]
>>> a[2]=6
>>> print(a)
[2, 3, 6, 5]
>>> a=['joshi','manasa','anu','kavya']
>>> print(a[3])
kavya
>>> print(a[0])
joshi
>>> print(a[1])
manasa
>>> a={2,3,4,6}
>>> print(a)
{2, 3, 4, 6}
>>> print(type(a))
<class 'set'>
