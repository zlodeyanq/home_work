import csv

#define variables
total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 9999999999999999999999]

revenue_changes = []
#open the CSV
with open('budget_data.csv', newline='') as csvfile:
    budget_data = csv.reader(csvfile, delimiter=',')
    next(budget_data)
#find number of rows
    for x in budget_data:
        total_months = total_months + 1
        total_revenue = total_revenue + int(x[1])

        revenue_change = int(x[1]) - prev_revenue
        prev_revenue = int(x[1])
       
        if (revenue_change > greatest_increase[1]):
            greatest_increase[1] = revenue_change
            greatest_increase[0] = x[1]

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = x[1]

        # Add to the revenue_changes list
        revenue_changes.append(int(x[1]))

    # Set the Revenue average
    revenue_avg = sum(revenue_changes) / len(revenue_changes)
    
    # Show Output
    print()
    print()
    print()
    print("Financial Analysis")
    print("-------------------------")
    print("Total Months: " + str(total_months))
    print("Total Revenue: " + "$" + str(total_revenue))
    print("Average Change: " + "$" + str(round(sum(revenue_changes) / len(revenue_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    

