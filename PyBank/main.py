#files using for code resource: web_solved, zipper, netflix
#houseofpie, readcsv, writecsv

import os
import csv
from statistics import mean

#path to collect data
csvpath = os.path.join("./Resources/budget_data.csv")

# assign
total_profitloss = 0
final_profitloss = 0
total_change_profitloss = 0
counter = 0
previous = 0

# lists
profit = []
monthly_change = []
date = []

#Read data w CSV module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        # count the lines of data for the month
        counter = counter + 1

        # collect the dates into a list
        date.append(row[0])

        # add all the profits in column 2 to the profit/loss list
        # make a calculation to add the totals to a 'total profits' variable
        profit.append(row[1])
        total_profitloss = total_profitloss + int(row[1])

        # calculate change #DOUBLE NEGATIVE calc ISSUE how to deal w it
        final_profitloss = int(row[1])
        changes = final_profitloss - previous

        #if int(row[1]) < 0:
        #    changes = final_profitloss - (-previous)
        #else:
        #    changes = (final_profitloss - previous)

        monthly_change.append(changes)
        
        total_change_profitloss += changes
        previous  = final_profitloss

        # calc ave
        ave_change_profitloss = (total_change_profitloss/counter)

        #calc year
        years = (counter/12)

        # get max & min
        max_in = max(monthly_change)
        max_de = min(monthly_change)

        max_in_PL = date[monthly_change.index(max_in)]
        max_de_PL = date[monthly_change.index(max_de)]


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

#print(profit)
#print(monthly_change)
#print(total_change_profitloss)
#print(int(counter))

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
