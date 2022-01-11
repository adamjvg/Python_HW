#Import modules
import os
import csv

#Find csv file
Pypollcsv = os.path.join("pypoll","election_data.csv")

#create lists to store data later
count = 0
candidatelist = []
candidateunique = []
votecount = []
voteperc =[]

#open csv and do the calculations
with open(Pypollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        count = count + 1 #counting the votes
        candidatelist.append(row[2]) #appending the list
    
    for i in set(candidatelist):
        candidateunique.append(i) 
        
        j = candidatelist.count(i) #j is total number of votes/candidate
        votecount.append(j)

        k = (j/count)*100 #k is percentage of votes won
        voteperc.append(k)

    #find the winner!
    winning_vote= max(votecount)
    winner = candidateunique[votecount.index(winning_vote)]

#print the results
print("----------------")
print("Election Results")
print("----------------")
print("Total Votes :" + str(count))
print("----------------")
for x in range (len(candidateunique)):
    print(candidateunique[x] + ": " + str(voteperc[x]) +"% (" + str(votecount[x]) + ")")
print("----------------")
print("The winner is: " + winner)
print("----------------")

#write to a text file
with open ('electionResults', 'w') as text:
    text.write("Election Results\n")
    text.write("------------------\n")
    text.write("Total Vote: " + str(count) + "\n")
    text.write("------------------\n")
    for x in range (len(candidateunique)):
        text.write(candidateunique[x] + ": " + str(voteperc[x]) +"% (" + str(votecount[x]) + ")\n")
    text.write("------------------\n")
    text.write("The winner is: " + winner +"\n")
    text.write("------------------\n")