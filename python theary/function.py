# simple function :

def evan_odd():
    a=2
    if a%2==0:
        print("Evan number ")
    else:
        print("odd number ")    

def evan_odd1():
    a=5
    if a%2==0:
        print("Evan number ")
    else:
        print("odd number ") 

# evan_odd1()
# evan_odd()

# def addition():
#     a=int(input("Enter a number : "))
#     b=int(input("Enter a number : "))
    
#     sum=a+b
#     print("sum of ",sum)
    
# def subtraction():
#     a=int(input("Enter a number : "))
#     b=int(input("Enter a number : "))
    
#     sub=a-b
#     print("sub of ",sub)
    
# def multiplication():
#     a=int(input("Enter a number : "))
#     b=int(input("Enter a number : "))
    
#     mul=a*b
#     print("mul of ",mul)
    
# def division():
#     a=int(input("Enter a number : "))
#     b=int(input("Enter a number : "))
    
#     div=a/b
#     print("div of ",div)
  
# a=True  
# while a:
#     print("""             1. Addition
#              2. subtraction
#              3. multiplication
#              4. division """)
#     choice = int(input("Enter a choice : "))
    
#     if choice==1:
#         addition()
#     elif choice==2:
#         subtraction()
#     elif choice==3:
#         multiplication()
#     elif choice==4:
#         division()
#     else:
#         print("invalid choice")

#     n=input("Enter y or n : ")
#     if n=='y':
#         a=True
#     else:
#         a=False


# ======================================
#parameterize function

# def fun(a,b,c):
#     print("sum of ",a+b+c)

# fun(2,3,4)


# ==============================
#default function

# def fun(a=10,b=20,c=30):
#     print("sum of ",a+b+c)

# fun(2,3,4)

# ================================
# return type

# def addition(a,b,c):
#     return "hello"

# print(addition(2,3,4))

# ====================================

# def fun(*args):
#     print(args)
    
    
#     for i in args:
#         print(i*5)
        
# fun(1,2,3,4,5,6)    


# ===============================


# def fun(**kwargs):
#     print(kwargs)
 
# fun(name="python",age=23)
    
    
# =====================================    
    
# Q : 1 ==> num = (1, 2, 3, 4, 5, 6, 7) using function
#           output:[3, 6, 9, 12, 15, 18, 21]
    
num = (1, 2, 3, 4, 5, 6, 7)
l1 = []
def mul():
    for i in num:
        l1.append(i*3)
    print(l1)
       
mul()    
# def fun(*args):
#     print(args)
#     l2=[]
#     for i in args:
#         l2.append(i*3)
#         # print(i*3)
#     print(l2)    
# fun(1,2,3,4,5,6,7)


# def fun(*args):
#     print(args)
#     for i in args:
#         a=i*3
#         print(a,end=' ')
#          
# fun(1,2,3,4,5,6,7)

# ===================================

# def fun(a):
#     return a*3

# l1=[1,2,3,4,5,6,7,8,9,10]


# a=map(fun,l1)

# print(list(a))

   
# def fun(a):
#     if a%2==0:
#         return a
    
# l1=[1,2,3,4,5,6,7,8,9,10]

# a=filter(fun,l1)

# print(list(a))    
    
        
# ============================

# fun=lambda b:b*10

# print(fun(10)) 


# =================================

# monkey paching : runtime changes

# def fun():
#     print('function')
    
# def fun1():
#     print("after monkey paching")
    
# fun=fun1    
    
# fun()
# fun1()

# x = lambda a,b : a+b
# print(x(10,20))

import datetime

a=datetime.datetime.now()
# print(a)

# a.day
a.month
print(a)
   
















    
    
    