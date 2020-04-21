import os
import csv

#path to collect data
csvpath = os.path.join("./Resources/budget_data.csv")

# assigning variables...
netProfit = 0
monthProfit = 0
counter = 0
previous = 0
change = 0

# .. and lists
changesList = []
months = []

# read file data w csv module
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        # count the lines of data for the month
        counter = counter + 1

        # collect the dates into a list
        months.append(str(row[0]))

        # Add all the profits in column 2 to the profit/loss list
        netProfit += int(row[1])
        
        # Calulate changes in month to month profit
        # if there is previous data then...
        if change != 0:

            # set value of monthProfit to 2nd column in row
            monthProfit = int(row[1])

            # Subtract current profit from previous month
            change = monthProfit - change

            # take the change value and store it in a list
            changesList.append(change)

            # reset the change variable
            change = int(row[1])
        
        # if there is no previous data set the variable to the value in the first row, column 2
        elif change == 0:
            change = int(row[1])
    
    # remove first month from list since there is no change there
    months.pop(0)

    # find the greatest increase and decrease in profits in the change list
    max_in = max(changesList)
    max_de = min(changesList)

    # use index positions to find the months for those numbers
    maxIncDate = months[changesList.index(max_in)]
    maxDecDate = months[changesList.index(max_de)]

    # get the average of the changeList
    ave = sum(changesList)/float(len(changesList))
    ave = round(ave, 2)
 
    # calculate year
    years = float(counter/12)
    years = round(years, 2)

# Print in terminal and to a txt file
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" FINANCIAL ANALYSIS")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(" Total Months: " + str(counter))
print(" Total Years: " + str(float(years)))
print(" Total Profits: " + "$" + str(netProfit))
print(" Average Change: " + "$" + str(float(ave)))
print(" Greatest Increase in Profits: $" + str(max_in) + " " + str(maxIncDate))
print(" Greatest Decrease in Profits: $" + str(max_de) + " " + str(maxDecDate))
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

with open('Pybank.txt', "w") as text_file:
    print(f" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
    print(f" FINANCIAL ANALYSIS", file=text_file)
    print(f" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
    print(f" Total Months: " + str(counter), file=text_file)
    print(f" Total Years: " + str(int(years))+ "ish", file=text_file)
    print(f" Total Profits: " + "$" + str(netProfit), file=text_file)
    print(f" Average Change: " + "$" + str(float(ave)), file=text_file)
    print(f" Greatest Increase in Profits: $" + str(max_in) + " " + str(maxIncDate), file=text_file)
    print(f" Greatest Decrease in Profits: $" + str(max_de) + " " + str(maxDecDate), file=text_file)
    print(f" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", file=text_file)
