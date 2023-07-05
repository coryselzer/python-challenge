import os
import csv

# Paths to collect and distribute data
budget_csv = os.path.join("Resources", "budget_data.csv")
budget_txt = os.path.join("analysis", "budget_analysis.txt")

# Define Variables
total_months = 0
net_total = 0
net_monthly_average = 0
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999]

# Read the CSV 
with open(budget_csv, encoding = "UTF-8") as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read header row first
    csv_header = next(csvreader)

    # Set formulas
    total_months += 1
    first = next(csvreader)
    net_total += int(first[1])
    previous = int(first[1])

    # Loop through CSV and perform calculations
    for row in csvreader:

        total_months += 1
        net_total += int(row[1])
        net_change = int(row[1]) - previous
        previous = int(row[1])
        net_change_list += [net_change]
        
        # Calculate greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
        
        # Calculate greatest decrease
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate net monthly average
net_monthly_average = sum(net_change_list) / len(net_change_list)

# Write Text File with Printed Outputs
with open(budget_txt, "w") as txtfile:

    output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${net_monthly_average: .2f}\n"
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]}) \n"
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]}) "
    )
    print(output)
    txtfile.write(output)


# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)