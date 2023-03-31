def calculate_bill(patient_name, cleaning, cavity_filling, x_ray):
    cleaning_rate = 60
    cavity_filling_rate = 200
    x_ray_rate = 100
    tax_rate = 0.15
    subtotal = 0
    
    if cleaning == 'y':
        subtotal += cleaning_rate
        
    if cavity_filling == 'y':
        subtotal += cavity_filling_rate
        
    if x_ray == 'y':
        subtotal += x_ray_rate
        
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    if total > 300:
        total *= 0.9
    elif total > 200:
        total *= 0.95
        
    print("\nMelanie Dental Clinic")
    print("--------------------")
    print(f"Receipt for patient name: {patient_name}\n")
    print("Subtotal: ${:.2f}".format(subtotal))
    print("Tax: ${:.2f}".format(tax))
    print("--------------------")
    print("Total: ${:.2f}".format(total))

# Take inputs from the user
patient_name = input("Enter patient's name: ")
cleaning = input("Was cleaning performed? (y/n): ")
cavity_filling = input("Was cavity-filling performed? (y/n): ")
x_ray = input("Was X-Ray performed? (y/n): ")

# Calculate the bill and print the receipt
calculate_bill(patient_name, cleaning, cavity_filling, x_ray)
