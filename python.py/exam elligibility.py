Total_days = int(input("Enter total no of days: "))
No_of_days_present = int(input("Enter no of days you were present : "))
Atendence_percentage = (No_of_days_present / Total_days) * 100
print("your Atendence_percentage is :", Atendence_percentage)

if Atendence_percentage >= 75:
    print("you are eligible for the exam")
else:
    print("you are'nt eligible for the exam")
