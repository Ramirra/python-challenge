#create file paths across operating systems
import os
#module for reading csv file
import csv

totalMonths = 0

#makes a reference to the path with the budget data
csvpath = os.path.join("..","Resources", "budget_data.csv")

#open the csv file
with open(csvpath) as csvfile:

    #set up the reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #skips the header info
    next(csvreader)

    #calculates the number of months
    for row in csvreader:
        totalMonths = totalMonths + 1

print(f"Financial Analysis")
print(f"-------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: $")
print(f"Average Change: $")
print(f"Greatest Increase in Profits: ")
print(f"Greatest Decrease in Profits: ")
