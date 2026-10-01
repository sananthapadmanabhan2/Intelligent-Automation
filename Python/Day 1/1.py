# Ask the user for an employee name, department, expense amount and status.
# If the expense is above ₹10,000, classify it as "High Value".
# If the status is "Pending", classify it as "Requires Approval".
# Otherwise classify it as "Normal"

def Employee():
    print("Employee Details\n")
    Employee_Name=input("Enter the Employee Name \n")
    Employee_Department= input("Enter Employee Department\n")
    Employee_Expense=int(input("Enter Expense\n"))
    Employee_Status=input("Enter Status\n")


    print("Employee Report\n")
    if Employee_Expense>10000:
        print("High Value\n")

    if Employee_Status == "Pending":
        print("Requires Approval\n")

    else:
        print("Normal")


Employee()