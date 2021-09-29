#create file paths across operating systems
import os
#module for reading csv file
import csv

#declare and initialize variables for calculations
totalMonths = 0
totalRevenue = 0
greatestIncrease = 0
greatestDecrease = 0

monthlyChanges = []

#makes a reference to the path with the budget data
csvpath = os.path.join("..","python-challenge", "PyBank", "Resources", "budget_data.csv")
print(csvpath)

outputfile = os.path.join("..", "python-challenge", "PyBank", "Analysis", "budget_data_analysis.text" )

#open the csv file
with open(csvpath) as csvfile:

    #set up the reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #reads the header info
    header = next(csvreader)

    #moves to the next row of data
    firstRow = next(csvreader)

    totalMonths = totalMonths + 1

    totalRevenue = totalRevenue + float(firstRow[1])

    #establish value of previous revenuee
    previousRevenue = float(firstRow[1])

    #calculates the number of months
    for row in csvreader:
        totalMonths = totalMonths + 1

        totalRevenue = totalRevenue + float(row[1])

        if float(row[1]) > greatestIncrease:
            greatestIncrease = float(row[1])
        
        if float(row[1]) < greatestDecrease:
            greatestDecrease = float(row[1])

        #calculate the net change
        netChange = float(row[1]) - previousRevenue

        #add to the list of monthly changes
        monthlyChanges.append(netChange)

        #update the previous revenue
        previousRevenue = float(row[1])

#calculate the average net change per month
averageChange = sum(monthlyChanges) / len(monthlyChanges)


#print outputs to the terminal
print(f"Financial Analysis")
print(f"-------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${totalRevenue:,.2f}")
print(f"Average Change: ${averageChange:,.2f}")
print(f"Greatest Increase in Profits: ${greatestIncrease:,.2f}")
print(f"Greatest Decrease in Profits: ${greatestDecrease:,.2f}")

#export to text file
with open(outputfile, "w") as textfile:
    textfile.write(f"Financial Analysis \n")
    textfile.write(f"------------------- \n")
    textfile.write(f"Total Months: {totalMonths} \n")
    textfile.write(f"Total: ${totalRevenue:,.2f} \n")
    textfile.write(f"Average Change: $ {averageChange:,.2f}\n")
    textfile.write(f"Greatest Increase in Profits: ${greatestIncrease:,.2f} \n")
    textfile.write(f"Greatest Decrease in Profits: ${greatestDecrease:,.2f}")