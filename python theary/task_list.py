# Q : 1 ==> Write a Python program to compute the element-wise sum of given tuples.
#           Original lists:
#           (1, 2, 3, 4)
#           (3, 5, 2, 1)
#           (2, 2, 3, 1)
#           Element-wise sum of the said tuples:
#           (6, 9, 8, 6)

# t1 = (1, 2, 3, 4)
# t2 = (3, 5, 2, 1)
# t3 = (2, 2, 3, 1)

# a=t1[0]+t2[0]+t3[0]
# b=t1[1]+t2[1]+t3[1]
# c=t1[2]+t2[2]+t3[2]
# d=t1[3]+t2[3]+t3[3]


# print(tuple([a,b,c,d]))

# ==================================================

# Q : 2 ==> Write a Python program to check if a list is empty or not.

# l1=[]


# if l1==[]:
#     print("list is empty")
# else:
#     print("Not empty")   

# =======================================================

# Q : 3 ==> C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
        #   output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']] 
        
# c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# print(c[::3],end='')
# print(c[1::3],end='')
# print(c[2::3],end='')
# for i in c:
#         ans = i[::4]
#         print(ans,end='')

# =======================================================

# Q : 6 ==> l1=[1,2,3,4,1,2,3,4,5,6,7]
#           output: [5,6,7]
#                   3

l1=[1,2,3,4,1,2,3,4,5,6,7]
l2=[]
l3=[]



# for i in l1:
#     if l1.count(i)>1:    
#         if i not in l2:
#                 l2.append(i)
                
#     else:
#         if i not in l3:
#              l3.append(i)
            
                        
# print(l2)
# print(l3)

# ========================================================

# Write a Python program to insert a given string at the beginning of all items in a list.
#           num=[1,2,3,4,5,6,7,8,9,10]  
#           outpt: [student-10] [student-9] [student-8] [student-7] [student-6] [student-5] [student-4] [student-3] [student-2] [student-1]

# num=[1,2,3,4,5,6,7,8,9,10] 


# num.reverse()
# print(num)


# for i in num:
#         print(f"[student-{i}]",end=" ")
        
# =====================================================

# Q : 4 ==> numbers_x = [10, 20, 30, 40, 10]
#         numbers_y = [75, 65, 35, 75, 30]
#         output = Given list: [10,520, 30, 40, 10]
#                         result is True

#                         numbers_y = [75, 65, 35, 75, 30]
#                         result is False

        
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]          

# # result = numbers_x[0],numbers_x[-1]

# if numbers_x[0]==numbers_x[-1]:
#         print("result is true ")
# else:
#         print("result is not true")
        
# if numbers_y[0]==numbers_y[-1]:
#         print("result is true ")
# else:
#         print("result is not true")
# ===================================================
# Q : 2 ==> numbers = [12, 75, 150, 180, 145, 525, 50] using for loop
#           output =  75
#                     150
#                     145

# numbers = [12, 75, 150, 180, 145, 525, 50] 

# print(numbers[1])
# print(numbers[2])
# print(numbers[4])

# for i in numbers:
#         if i==75 or i==150 or i==145:
#                 print(i)
                # print("75")
                # print("150")
                # print("145")

# for i in 12, 75, 150, 180, 145, 525, 50:
#     if i==75:
#         print(i)
#     elif i==150:
#         print(i)
#     elif i==145:
#         print(i)
        
# ========================================================
# Q : 4 ==> num = [10.0, 20.0, 30.0, 40.0, 50.9, 60.8, 70.7, 80.6, 90.5, 100.4]
#           output : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        
        
# num = [10.0, 20.0, 30.0, 40.0, 50.9, 60.8, 70.7, 80.6, 90.5, 100.4]

# for i in num:
#        print(int(i),end=' ')

# Q : 2 ==> nums1 = [1, 2, 3]  using  function
#           nums2 = [4, 5, 6] 
#           nums3 = [7, 8, 9] 
#           output:(12, 15, 18)

# nums1 = [1, 2, 3] 
# nums2 = [4, 5, 6] 
# nums3 = [7, 8, 9]

# a=nums1[0]+nums2[0]+nums3[0]
# b=nums1[1]+nums2[1]+nums3[1]
# c=nums1[2]+nums2[2]+nums3[2]


# cal_sum=tuple([a,b,c])

# print(tuple([a,b,c]))


        
# Q : 1 ==> Write a Python function that accepts a string and counts the number of upper and lower case letters
#       Original String :  The quick Brow Fox                                                                         
#       No. of Upper case characters :  3                                                                             
#       No. of Lower case Characters :  13  
 
# s =  'The quick Brow Fox' 

# u=0
# l=0

# for i in s:
#         if i.isupper():
#                 u+=1
                
#         elif i.islower():
#                 l+=1

# print("upper case : ",u)        
# print("lower case : ",l)


# Q : 2 ==>  Addition of first and last digit of the number ==> number = 12475 ==> output=6

# num = 12345
# num=str(12345)
# a=int(num[0])
# b=int(num[-1])
# print(a+b)

# Q : 3 ==>  Python program to print positive numbers and nagitive numbers in a list

# a=[1,2,3,4,5,6,7,8,-1,-2,-3,-4]
# b=[]
# c=[]
# for i in a:
#         if i>=1:
#                 c.append(i)
#         else:
#                 b.append(i)
# print("positive num : ",c)
                
# print("nagetive num : ",b)

# ========================================

# color = ['Red','Blue','Black']

# l1=[]

# for i in color:
#         l1.append(list(i))
# print(l1)
        
        
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}  
# dic4={}       

                
# dic4.update(dic1)
# dic4.update(dic2)
# dic4.update(dic3)
# print(dic4)        
        
# =======================================

h='hardik hardik1234 hardik5555555'
a=h.split()
b=max(a)
print(max(b))
print(len(b))
                
        




