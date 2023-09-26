

# d1={
#     "name":"hardik",
#     "age":33,
#     "subject":"python"}


# print(type(d1))
# print(d1)

# ====================

# d1={
#     1:2,
#     2.2:3.5,
#     "name":"hardik",
# }

# print(d1)

# ========================

# d1={
#     "name":"hardik",
#     "age":33,
#     "subject":"python"
# }

# print(d1.keys())
# print(d1.values())
# print(d1.items())

# d1.update({
#     "std":1,
# })

# d2={
#     "std":12
# }

# d1.update(d2)

# d1.popitem()

# d1.pop("age")

# d1.clear()

# del d1

# print(d1.get('std'))


# ===================================


# d1={
#     "name":"hardik",
#     "age":33,
#     "subject":"python"
# }
# l1=[]
# for i in d1.keys():
#     l1.append(i)
# print(l1)

# for i in d1.values():
#     print(i)


# for i in d1.items():
#     print(i)





# d1={
#     1:{
#         "name":"python",
#         "age":23
#     },
#     2:{
#         "name":"hardik",
#         "age":24
#     },
#     3:{
#         1:{
#             "name":"hardik"
#         },
#         2:{
#             "name":"hardik1"
#         }
#     }
# }


# print(d1[1])
# print(d1[2]["age"])
# print(d1[3][2]["name"])


# task :

# Q : 1 ==> Print the value of key ‘history’ from the below dict
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

# print(sampleDict["class"]["student"]["marks"]["history"])

# Q : 2 ==> Check if a value exists in a dictionary
# sample_dict = {'a': 100, 'b': 200, 'c': 300}   

# for i in sample_dict.values():
#     print(i)
    
# Q : 3 ==>   Change value of a key in a nested dictionary
# sample_dict = {
#     'emp1': {'name': 'Jhon', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }       

# sample_dict["emp3"]["salary"]=1000
# # print(sample_dict)

# for i in sample_dict.items():
#     print(i)

# name = {'raj','shyam','ajay'}
# age = {25,26,28}

# a=dict.fromkeys(name,age)
# print(a)

