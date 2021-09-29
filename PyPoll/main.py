#create file paths across operating systems
import os
#module for reading csv file
import csv

#declare and initialize variables
totalVotes = 0
candidates = []
candidatesVotes = {}

#makes a reference to the path with the election data
csvpath = os.path.join("..","python-challenge", "PyPoll", "Resources", "election_data.csv")
print(csvpath)

#creates ouptput file for results
outputfile = os.path.join("..", "python-challenge", "PyBank", "Analysis", "election_data_analysis.text" )

    #opens the csv file
with open(csvpath) as csvfile:

    #set up the reader object
    csvreader = csv.reader(csvfile, delimiter=",")

    #reads the header info
    header = next(csvreader)

    #for each row
    for row in csvreader:
        #adds 1 to the total # of votes
        totalVotes = totalVotes + 1

        #check to see if candidate is included in list
        if row[2] not in candidates:
            #add if not already listed
            candidates.append(row[2])

            #add vote to candidates votes
            candidatesVotes[row[2]] = 1

        else:
            #the candidate is already listed so only add the vote
            candidatesVotes[row[2]] +=1

        
print("Elections Results")
print("--------------------")
print(f"Total Votes: {totalVotes}")
print("--------------------")
print(candidatesVotes)
