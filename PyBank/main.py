import os
import csv

#path to collect data
csvpath = os.path.join("./Resources/budget_data.csv")

# assigning variables...
total_profitloss = 0
final_profitloss = 0
total_change_profitloss = 0
counter = 0
previous = 0

# .. and lists
profit = []
monthly_change = []
date = []

# read file data w csv module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        # count the lines of data for the month
        counter = counter + 1

        # collect the dates into a list
        date.append(row[0])

        # Add all the profits in column 2 to the profit/loss list
        profit.append(row[1])
        
        # Make a calculation to add the totals to a 'total profits' variable
        total_profitloss = total_profitloss + int(row[1])

        # Calculate changes and get average...
 
        # !!! Not getting the value reflected in the answer example in the hw description
        # Having a double negative calculation issue! Tried to fix it...
        # ...Still not correct!

        # Here's how I tried to fix the problem:
    
        # if int(row[1]) < 0:
        #    changes = final_profitloss - (-previous)
        # else:
        #    changes = (final_profitloss - previous) 

        # Calculate changes...
        final_profitloss = int(row[1])
        changes = final_profitloss - previous
        monthly_change.append(changes)
        total_change_profitloss += changes
        previous  = final_profitloss

        # Get average
        ave_change_profitloss = (total_change_profitloss/counter)
 
        # calculate year
        years = (counter/12)

        # Get max increase and decrease
        max_in = max(monthly_change)
        max_de = min(monthly_change)
        max_in_PL = date[monthly_change.index(max_in)]
        max_de_PL = date[monthly_change.index(max_de)]

# Print in terminal and to a txt file
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" FINANCIAL ANALYSIS")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Total Months: " + str(counter))
print(" Total Years: " + str(int(years))+ "ish")
print(" Total Profits: " + "$" + str(total_profitloss))
print(" Average Change: " + "$" + str(int(ave_change_profitloss)))
print(" Greatest Increase in Profits: $" + str(max_in) + " " + str(max_in_PL))
print(" Greatest Decrease in Profits: $" + str(max_de) + " " + str(max_de_PL))
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

with open('Pybank.txt', "w") as text_file:
    print(f" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
    print(f" FINANCIAL ANALYSIS", file=text_file)
    print(f" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
    print(f" Total Months: " + str(counter), file=text_file)
    print(f" Total Years: " + str(int(years))+ "ish", file=text_file)
    print(f" Total Profits: " + "$" + str(total_profitloss), file=text_file)
    print(f" Average Change: " + "$" + str(int(ave_change_profitloss)), file=text_file)
    print(f" Greatest Increase in Profits: $" + str(max_in) + " " + str(max_in_PL), file=text_file)
    print(f" Greatest Decrease in Profits: $" + str(max_de) + " " + str(max_de_PL), file=text_file)
    print(f" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
