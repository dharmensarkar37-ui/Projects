def calculate_gross(basic):
    """Calculates HRA, DA, and Gross salary based on basic pay."""
    hra = 0.20 * basic
    da = 0.10 * basic
    gross = basic + hra + da
    return hra, da, gross

def calculate_deductions(basic, gross):
    """Calculates PF and Tax based on basic pay and gross salary brackets."""
    pf = 0.12 * basic
    
    # Tax slab conditions on gross salary
    if gross <= 25000:
        tax = 0.0
    elif gross <= 50000:
        tax = 0.05 * gross
    else:
        tax = 0.10 * gross
        
    return pf, tax

def print_slip(emp_id, emp_name, basic, hra, da, gross, pf, tax, net_salary):
    """Prints a neat, formatted salary slip for the employee."""
    print("\n" + "=" * 42)
    print("               SALARY SLIP               ")
    print("=" * 42)
    print(f"Employee ID   : {emp_id}")
    print(f"Employee Name : {emp_name}")
    print("-" * 42)
    print(f"Basic Salary  : {basic:,.2f}")
    print(f"HRA (20%)     : {hra:,.2f}")
    print(f"DA (10%)      : {da:,.2f}")
    print(f"Gross Salary  : {gross:,.2f}")
    print("-" * 42)
    print(f"PF (12%)      : {pf:,.2f}")
    print(f"Tax           : {tax:,.2f}")
    print(f"Net Salary    : {net_salary:,.2f}")
    print("=" * 42 + "\n")

def main():
    print("=== Employee Salary Calculator System ===")
    
    while True:
        emp_id = input("Enter Employee ID: ")
        emp_name = input("Enter Employee Name: ")
        
        # Robust input validation for basic salary (handles negative numbers and letters/invalid text)
        while True:
            try:
                basic = float(input("Enter Basic Salary: "))
                if basic <= 0:
                    print("Invalid salary. Enter a positive number.")
                    continue
                break
            except ValueError:
                print("Invalid salary. Enter a positive number.")
        
        # Calculations
        hra, da, gross = calculate_gross(basic)
        pf, tax = calculate_deductions(basic, gross)
        net_salary = gross - (pf + tax)
        
        # Display slip
        print_slip(emp_id, emp_name, basic, hra, da, gross, pf, tax, net_salary)
        
        # Loop control for multiple employees
        choice = input("Do you want to calculate for another employee? (y/n): ").strip().lower()
        if choice != 'y':
            print("Exiting program. Thank you!")
            break

if __name__ == "__main__":
    main()