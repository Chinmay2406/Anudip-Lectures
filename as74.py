# 4. WAP to calculate total salary with DA and HRA
basic_salary = float(input("Enter your basic salary: "))

if basic_salary > 50000:
    DA = basic_salary * 0.10
    HRA = basic_salary * 0.12
    total_salary = basic_salary + DA + HRA
    print(f"Total Salary: {total_salary}")
else:
    print("Salary is less than 50,000, no DA or HRA applicable.")
