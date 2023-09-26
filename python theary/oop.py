

# class A():
#     name="hardik"
#     age=23
#     subject="python"
    
    
# a=A()    
    
# print(a.name)
# print(a.age)
# print(a.subject)


# class A():
#     name="hardik" #data member
#     age=23
#     subject="python"
    
#     def display(self): #member function
#         print(self.name)
#         print(self.age)
#         print(self.subject)
        

# a=A()
# print(a.name)    
# a.display() 



# class  

# ===============================

# constructor

# class A():
#     def __init__(self,name,age,subject):
#         self.name=name
#         self.age=age
#         self.subject=subject
        
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.subject)
        
# a=A("hardik",23,"python")

# a.display() 


# =======================================

# inharitance
# 5 types :
# 1. single level inhetitance
# 2. multilevel inhetitance
# 3. multiple inhetitance
# 4. hirarical inhetitance
# 5. hybrid inhetitance


# 1. single level inhetitance

# class A():
#     def displayA(self):
#         print("Class A ")



# class B(A):
#     def displayB(self):
#         print("Class B ")


# b=B()

# b.displayA()
# b.displayB()



# 2. multilevel inheritance :

# class A():
#     def displayA(self):
#         print("Class A ")



# class B(A):
#     def displayB(self):
#         print("Class B ")


# class C(B):
#     def displayC(self):
#         print("Class C ")


# c=C()
# c.displayA()
# c.displayB()
# c.displayC()


# 3.multiple inheritance :


# class A():
#     def displayA(self):
#         print("Class A ")



# class B():
#     def displayB(self):
#         print("Class B ")


# class C(A,B):
#     def displayC(self):
#         print("Class C ")




# c=C()
# c.displayA()
# c.displayB()
# c.displayC()

# 4. hirarical inheritance :


# class A():
#     def displayA(self):
#         print("Class A ")



# class B(A):
#     def displayB(self):
#         print("Class B ")


# class C(A):
#     def displayC(self):
#         print("Class C ")
        
        
# b=B()
# c=C()
# b.displayA()
# b.displayB()
# c.displayA()
# c.displayC()

# 5. hybrid inheritance :

# class A():
#     def displayA(self):
#         print("Class A ")



# class B(A):
#     def displayB(self):
#         print("Class B ")


# class C(B,A):
#     def displayC(self):
#         print("Class C ")
# b=B()
# c=C()

# b.displayA()
# b.displayB()
# print('')
# c.displayA()
# c.displayB()
# c.displayC()
# =============================================
# Encapsulation
# s=[]
# class A():
#     name="hardik"
#     age=23
#     __pin=123
    
    
#     def display(self):
#         print(self.name)
#         print(self.age)
#         print(self.__pin)
#         s.extend([self.name,self.age])
# a=A()

# a.display()
# print(a.name)
# print(a.age)
# print(a.__pin)

# print(s)

# ============================================
# polymorephisam

# 2 types :
#     1. method overriding
#     2. method overloading # not support in python

# class A():
#     def display(self):
#         print("class A ")
        
# class B(A):
#     def display(self):
#         A.display(self)
#         print("class B ")
        
        
        
# b=B()

# b.display()

# ====================================================
# abstractmethod

# from abc import ABC,abstractmethod



# class RBI(ABC):
#     @abstractmethod
#     def display(self):
#         print("Class RBI")
        
# class SBI(RBI):
#     def display(self):
#         RBI.display(self)
#         print("Class SBI")
        
# class BOI(RBI):
#     def display(self):
#         RBI.display(self)
#         print("Class BOI")
        
        
# # rbi=RBI()
# sbi=SBI()
# boi=BOI()

# # rbi.display()
# sbi.display()
# boi.display()  

# ==================================    

# aggregation


class salary():
    def __init__(self,salary,bonus):
        self.salary=salary
        self.bonus=bonus
        
    def a_salary(self):
        return self.salary*12+self.bonus 

class employee():
    def __init__(self,name,age,sal):
        self.name=name
        self.age=age
        self.sal=sal
    def total_salary(self):
        print("name :",self.name)  
        print("age :",self.age)
        return self.sal.a_salary()  
        
       

sal=salary(10000,2000)
emp=employee("hardik",23,sal)

print(emp.total_salary()) 

# pip install django
# django-admin startproject .
# django-admin startapp
# python manage.py runserver
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser









       
        
