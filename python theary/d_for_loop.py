# syntax :

# for variable_name in range(1,11):
#     code

# for i in range(0,11,2):
#     print(i)

# a=1,2,3,4,5,6,7,8

# for i in a:
#     print(i)

#nested for loop :

# a=int(input("Enter a number :"))
# b=int(input("Enter a number :"))

# for i in range(a,b): #row 
#     for n in range(1,11): #colonm
#         print(f"{i} * {n} = {i * n}")
#     print("\n")

# c=0
# for i in range(1,6):
#     num=int(input("Enter a number :"))
#     c+=num

    

# odd number program
# for i in range(1,11):
#     if i%2==0:
#         pass
#     else:
#         print(i)


        


# name="python program count word"
# # print(name.count("p"))
# c=0
# for i in name:
#     c+=1
    

# odd and even :
# for i in range(1,11):
#     if i%2 == 0:
#         print("Even",i)
#     else:
#         print("odd",i)

    
# sum odd number : not run 

# sum=0
# for i in range(1,21):
#     if i%2 == 1:
#         sum += i
#         print(i)
 

# num=123456
# c=0
# for i in str(num):
#     c+=1
# print(c)    
             
        
        
# name="my name is python"

# name1=input("Enter A Name ")   

# print(name.count(name1)) 
# c=0
# for i in name:
#     if i==name1:
#         c+=1    
# print(c)      

# name="jadav nilesh"        
# for i in name:
#     print(i,end="")        

# start=int(input("Enter A Number  : "))
# end=int(input("Enter A Number  : "))

# for i in range(start,end):
#     print(i)


#  for i in range(1,2): # 1 
#     for n in range(1,5):
#         print(n)
#     print("\n")   



# start=int(input("Enter a start number : "))
# end=int(input("Enter a number : "))

# for i in ran9ge(start,end):
#     for n in range(1,11):
#         print(f"{i} * {n} = {n * i}")
    
# *
# ***
# *****
# *******
# *********
   

# num=int(input("Enter A Number"))
# for i in range(1,num+1,2): #1,3,5,7,9
#     for n in range(1,i+1): #
#         print("*",end=" ")
#     print("\n")
    

            
# num=int(input("Enter a number : "))

# for i in range(1,num+1):
#     for n in range(1,i+1):
#         print('*',end=" ")
#     print("\n")


# jumping statements


# break
# continue
# pass



# for i in range(1,11):
#     if i==5:
#         break
#     print(i)
    
# for i in range(1,11):
#     if i==4 and i==4:
#         continue
#     if i>=6:
#         break 
       
#     print(i)

# for i in range(1,11):
#     if i==5:
#         pass
#     print(i)
    

# for i in range(1,11):
#     if i%2==0:
#         pass
#     else:
#         print(i)




# prime number or not :

# num=7
# j=0

# for i in range(1,num+1):
#     if num%i==0: # 7%1==0 7%2==1 7%3==1 7%4==3 7%5==2 7%6==1 7%7==0
#         j+=1    


# if j==2:
#     print("prime number")

# else:
#     print("not")
# ============================================
# fibbonaci serias

# 0 1 1 2 3 5 8 13 
num=10
a=0
b=1
c=0
for i in range(num):
   print(c,end=" ")
   c=a+b #  0+1=1 
   b=a   #  1=0
   a=c   #  0=1 
   

# ===============================================

# factorial :

# f=5

# for i in range(1,f):
#     f*=i # 5=5*1   5=5*2  10=10*3  30=30*4 

# print(f)


