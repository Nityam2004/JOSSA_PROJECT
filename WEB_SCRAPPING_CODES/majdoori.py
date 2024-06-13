import csv

# Specify the file name
filename = "rankvsmarks_ews.csv"

# Open the file in write mode
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(["Number"])
    
    # Initialize the starting number
    number = 1
    
    # Write numbers increasing by 100 until 26301
    while number <= 5301:
        writer.writerow([number])
        number += 100

print(f"CSV file '{filename}' created successfully.")
