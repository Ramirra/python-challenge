#create file paths across operating systems
import os
#module for reading csv file
import csv

#declares and initializes variables for calculations
totalMonths = 0
totalRevenue = 0

#creates list for monthly changes and months
monthlyChanges = []
months = []

#makes a reference to the path with the budget data
csvpath = os.path.join("..","python-challenge", "PyBank", "Resources", "budget_data.csv")
print(csvpath)

#creates ouptput file for results
outputfile = os.path.join("..", "python-challenge", "PyBank", "Analysis", "budget_data_analysis.text" )

#opens the csv file
with open(csvpath) as csvfile:

    #sets up the reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #reads the header info
    header = next(csvreader)

    #moves to the next row of data
    firstRow = next(csvreader)

    #adds 1 to the total # of months
    totalMonths = totalMonths + 1

    #calculates the total revenue 
    totalRevenue = totalRevenue + float(firstRow[1])

    #establish value of previous revenue
    previousRevenue = float(firstRow[1])

    #for each row
    for row in csvreader:
        #add 1 to the total # of months
        totalMonths = totalMonths + 1

        #adds to the total revenue/ calculates net amount
        totalRevenue = totalRevenue + float(row[1])
    
        #calculates the net change between months
        netChange = float(row[1]) - previousRevenue

        #adds to the list of monthly changes
        monthlyChanges.append(netChange)

        #adds the first month that a change occurs
        months.append(row[0])

        #updates the previous revenue
        previousRevenue = float(row[1])

#calculates the average net change per month
averageChange = sum(monthlyChanges) / len(monthlyChanges)

#creates list for greatest increase/decrease months + values
greatestIncrease = [months[0], monthlyChanges[0]]
greatestDecrease = [months[0], monthlyChanges[0]]

#calculate the index of the greatest and least monthly changes
for m in range(len(monthlyChanges)):
    #finds and stores the greatest increase
    if monthlyChanges[m] > greatestIncrease[1]:
        greatestIncrease[1] = monthlyChanges[m]
        greatestIncrease[0] = months[m]

    #finds and stoes the greatest decrease
    if monthlyChanges[m] < greatestDecrease[1]:
        greatestDecrease[1] = monthlyChanges[m]
        greatestDecrease[0] = months[m]
    

#prints outputs to the terminal
print(f"Financial Analysis")
print(f"-------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalRevenue:,.2f}")
print(f"Average Change: ${averageChange:,.2f}")
print(f"Greatest Increase in Profits: {greatestIncrease[0]}, ${greatestIncrease[1]:,.2f}")
print(f"Greatest Decrease in Profits: {greatestDecrease[0]}, ${greatestDecrease[1]:,.2f}")

#exports to text file
with open(outputfile, "w") as textfile:
    textfile.write(f"Financial Analysis \n")
    textfile.write(f"------------------- \n")
    textfile.write(f"Total Months: {totalMonths} \n")
    textfile.write(f"Total: ${totalRevenue:,.2f} \n")
    textfile.write(f"Average Change: $ {averageChange:,.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatestIncrease[0]}, ${greatestIncrease[1]:,.2f} \n")
    textfile.write(f"Greatest Decrease in Profits: {greatestDecrease[0]}, ${greatestDecrease[1]:,.2f}")