# Import Modules
import os
import csv

# Set path for file
csvpath = os.path.join("PyPoll","election_data.csv")

# Print Title and divider
print("Election Results")
print("-------------------------")

# Open the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip header
    header = next(csvreader)
    # Define variable of Total number of votes by adding 1 for each row in csvfile
    totalVotes = sum(1 for row in csvfile)
    # Print number of rows as the total number of votes
    print(f"Total Votes: {totalVotes}")
    print("-------------------------")

# Define variable for Candidates and the number of votes each received
Candidate = {}
# Define variable for number of votes for calculations based on row numbers
row_number = 0
# Command to loop throgh each row and add a value of 1 for each time each candidate receives a vote
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    for row in csvreader:
        row_number +=1
        if row[2] in Candidate:
                Candidate[row[2]] +=1
        else:
            Candidate[row[2]] = 1
# Define variable for the winner using the key parameter, since each candidate is already paired with a number of votes
winner = max(Candidate, key=Candidate.get)

# Command to loop trhough values in variable Candidate 
for word in Candidate:
    # Calculation to find the percentage each candidate received
    Percentage = float((Candidate[word])/(row_number))
    # Variable to show the amount of votes each candidate recieved
    candidateVotes = int(Candidate[word])
    # Print summanry of results
    print(f"{word}: {Percentage:.3%} ({candidateVotes})")

# Print dividers and final Winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

#Create file to write results
output_path=os.path.join("PyPoll","pyPoll_Output.txt")
file = open(output_path,'w')

#Write to file all results
file.write("Election Results")
file.write("\n-------------------------")
file.write(f"\nTotal Votes: {totalVotes}")
file.write("\n-------------------------")
for word in Candidate:
    Percentage = float((Candidate[word])/(row_number))
    candidateVotes = int(Candidate[word])
    file.write(f"\n{word}: {Percentage:.3%} ({candidateVotes})")
file.write("\n-------------------------")
file.write(f"\nWinner: {winner}")
file.write("\n-------------------------")

file.close()