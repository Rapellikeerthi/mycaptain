condition=True

while(condition):
    student_info=input("Enter some student information:")
    
    print(student_info)
    
    condition_check=input("Enter (yes/no) if you want to enter information for another student:")
    if condition_check=="yes":
        condition=True
    elif condition_check=="no":
        condition=False
