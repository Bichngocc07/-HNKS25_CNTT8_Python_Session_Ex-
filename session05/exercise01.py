total_employees = int(input("Enter number of employees: "))
print("") 

for i in range(1, total_employees + 1):
    
    employee_name = input("Enter employee name: ")
    working_days = int(input("Enter number of working days: "))
    
    if working_days < 0 or working_days > 22:
        print("Invalid data")
        print("") 
        continue
        
    print(f"{employee_name}: ", end="")
    for star in range(0, working_days):
        print("*", end="")
    print("") 
    
    if working_days == 0:
        print("Employee absent for the entire month")
    elif working_days >= 18:
        print("Work hard")
    elif working_days < 10:
        print("Work little")
    else:
        print("Work normally")
        
    print("") 
