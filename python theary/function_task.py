# Q-1  l1=(8,2,3,0,7)
#     output : 20
 

# l1=(8,2,3,0,7)
# def cal_sum():
#     c=0
    
#     for i in l1:
#         c+=i
#     print(c)

# cal_sum()

# other method:

# def sum(num):
#     c=0
#     for i in num:
#         c+=i
#     return c

# print(sum((8,2,3,0,7)))
    
# =====================================
# multiply number l1:

# def mul(num):
#     c=1
#     for i in num:
#         c*=i
#     return c

# print(mul((8,2,3,-1,7)))

# other method :

# l1=(8,2,3,-1,7)

# def mul():
#     c=1
#     for i in l1:
#         c*=i
#     print(c)
    
# mul()

# =====================================
# Reverse number :

# l1='1234abcd'

# print(l1[::-1])
# ==============
# def rev(num):
#     re=num[::-1]
#     return re

# print(rev(('1234abcd')))

# ================================

#  Q : 2 ==> nums1 = [1, 2, 3]  using  function
#           nums2 = [4, 5, 6] 
#           nums3 = [7, 8, 9] 
#           output:(12, 15, 18)


# nums1 = [1, 2, 3]  
# nums2 = [4, 5, 6] 
# nums3 = [7, 8, 9] 

# n1=nums1[0]+nums2[0]+nums3[0]
# n2=nums1[1]+nums2[1]+nums3[1]
# n3=nums1[2]+nums2[2]+nums3[2]

# def sum():
#     print(tuple([n1,n2,n3]))
    
# sum()

# ===============================================

# l1=[1,2,3,4,5,1,2,3,3,4,5,10,11,12,13,14]

# def reapet():
#     l2=[]
    
#     for i in l1:
#         if i not in l2:
#             if l1.count(i)<=1:
                
#                 l2.append(i)
#     print(l2)
    
# reapet()

# ===========================================

# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
# s = 'The quick Brow Fox'

# =============================================


# Q : 4 ==> Write a Python program to insert a given string at the beginning of all items in a list.
#           num=[1,2,3,4,5,6,7,8,9,10]  
#           output: [student-10] [student-9] [student-8] [student-7] [student-6] [student-5] [student-4] [student-3] [student-2] [student-1]  

# num=[1,2,3,4,5,6,7,8,9,10] 

# num.reverse()
# print(num)

# for i in num:
#     print(f"[student-{i}]",end=' ')
    
# =============================================

# Q : 3 ==> color = ['Red', 'Blue', 'Black', 'White', 'Pink']    
#           output : [['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

# color = ['Red', 'Blue', 'Black', 'White', 'Pink']   

# for i in color:
#     print([i],end=' ')
#     # for n in i:
#     #     print([n],end=' ')
    
    
# a=[1,2,3,4,5,6]
# b=[7,8,9,10,11,12]
# e=[]
# d=a+b
# for i in d:
    
#     e.append(i)
# print(e)

# ===================================

# find maximum three number of three number:

# a=100
# b=20
# c=100
# def max():
#     if a>b and a>c:
#         print("max num a is",a)
#     elif b>a and b>c:
#         print("max num b is",b)
#     elif c>a and c>b:
#         print("max num c is",c)
#     elif a==b:
#         print(a,b)
        
# max()

# multiplication of number :
# l1=[]
# def mul():
#     for i in range(1,21):
#         l1.append(i**2)
#     print(l1)
        
# mul()
    
    

