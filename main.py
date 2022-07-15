student = []
ans=True
while ans:
    print("""
    1.Add a Student
    2.Remove a Student
    3.Add a quiz grade for Student 
    4.List a student quiz grade
    5.Get a student letter grad
    6.Quit
    """)
    ans=input("Select an opiion: ")
    if ans=="1":
      student= input("\n Enter a Student name:")
      
      print(f"{student} added!")
      print()
      #break
      print(student)
    elif ans=="2":
      print("\n Remove student")
      student= input("\n Enter a Student name:")
      for students in not student:
        print("not in dictionary")
#student = del(student)
       # print(f"{student} removed!")
    #  print(f"{student} removed!")
    elif ans=="3": 
      print("\n Student Record Found")
    elif ans=="4":
      print("\n Goodbye") 
      ans = None
    else:
      print("\n Not Valid Choice Try again")

      
