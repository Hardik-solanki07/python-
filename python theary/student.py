students={}
subjects=[]
rollno1=0

def add():
    name=input("Enter a name :")
    # email=input("Enter a email-id :")
    # rollno=int(input("Enter a rollno :"))
    # mobile=int(input("Enter a mobile no :"))
    # male=input("Enter a male or female :")
    # rollno1=rollno
    
    # students={"name":name,
    #          "email":email,
    #          "rollno":rollno,
    #          "mobile":mobile,
    #          "male":male}
    
    students.update({"name":name})
    print(students)
    print("student details store successfully")
   

def sub():
    rollno=int(input("Enter a rollno :"))
    
    if rollno==rollno1:
        
        subject=int(input("Enter a subject name :"))
        min=int(input("Enter a minimum mark :"))
        max=int(input("Enter a maximum mark :"))
        
        subjects={"subject":subjects,
                "min":min,
                "max":max}
        print("")
        print("subject mark add successfully")
    else:
        print("Invalid roll no, try again")
        
def marksheet():
    print("Marksheet")
    rollno=int(input("Enter a rollno :"))
    if rollno==rollno1:
        print(students[name])
        print(subjects)
    else:
        print("invalid roll no, try again")

a=True

while a:
    
    print("1.add student details")
    print("2.add subject")
    print("3.print marksheet")
    
    choice = int(input("Enter your choice :"))
    
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        marksheet()
    else:
        print("Invalid choice")
        
    user=input("Enter y or n :")
    if user=='y':
        a=True
    else:
        a=False
    







