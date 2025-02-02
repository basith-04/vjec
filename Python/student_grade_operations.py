selection ="YES"
grades={}
while selection=="YES":
    print("select \n 1 . Add \n 2 . Remove \n 3. Modify grades \n 4. Show all \n 5. Exit")
    choice=int(input("Enter the selection 1 to 4 "))

    
    if choice==1:
        name=input("Enter the name of the student : ")
        grade=input("Enter the grade of the student : ")
        grades[name]=grade
        print(f"{name} is added ")

    elif choice==2:
        name=input("Enter the name of the student : ")
        if name in grades:
            del grades[name]
            print(f"{name} is removed ")
        else :
            print(f"{name} not found ")
    elif choice==3:
        name=input("Enter the name of the student : ")
        if name in grades:
            grade=input("Enter the grade :")
            grades[name]=grade
            print(f"Grade of {name} is changed.")
        else:
            print(f"{name} not found.")
    elif choice==4:
        for name,grade in grades.items():
            print(f"{name}:{grade}")
    selection=input("Do you want to continue (yes /no)").upper()
