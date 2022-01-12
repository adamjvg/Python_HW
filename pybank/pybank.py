#import modules
import os
import csv

#Set csv path
pybankcsv = os.path.join("pybank","budget_data.csv")

#create empty lists
profit = []
monthly_changes =[]
date = []

#make variables

count = 0
total_profit = 0
total_change = 0
initial_profit = 0

#read from csv
with open(pybankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    csv_header = next(csvreader)

    #ask csv
    for row in csvreader:
        #count the rows
        count=count + 1

        #append date list
        date.append(row[0])

        #calculate total profit and append list
        profit.append(row[1])
        total_profit = total_profit + int(row[1])
        
        #calculate change in profits month to month and average
        final_profit = int(row[1])
        monthly_change_profits = final_profit - initial_profit

        #create new list with monthly changes
        monthly_changes.append(monthly_change_profits)

        total_change = total_change + monthly_change_profits 
        initial_profit = final_profit

        #calculate average change
        average_change = (total_change/count)

        #find max and min and the date
        greatest_increase = max(monthly_changes)
        greatest_decrease = min(monthly_changes)

        increase_month = date[monthly_changes.index(greatest_increase)]
        decrease_month = date[monthly_changes.index(greatest_decrease)]

#print results
print("-------------")
print("Financial Analysis")
print("-------------")
print("Total Months: " + str(count))
print("Profits: " +str(total_profit))
print("Average change: " + str(average_change))
print("Greatest Increase in profits: " + str(increase_month) + " ($" + str(greatest_increase)+ ")")
print("Greatest Decrease in profits: " + str(decrease_month) + " ($" + str(greatest_decrease)+ ")")
print("-------------")

#print to txt file
with open('financial_analysis.txt', 'w') as text:
    text.write("-------------\n")
    text.write("Financial Analysis")
    text.write("-------------\n\n")
    text.write("Total Months: " + str(count) + "\n")
    text.write("Profits: " +str(total_profit) + "\n")
    text.write("Average change: " + str(average_change) + "\n")
    text.write("Greatest Increase in profits: " + str(increase_month) + " ($" + str(greatest_increase)+ ")\n")
    text.write("Greatest Decrease in profits: " + str(decrease_month) + " ($" + str(greatest_decrease)+ ")\n")
    text.write("-------------\n")
