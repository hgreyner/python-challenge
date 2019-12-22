# Import Modules
import os
import csv

# Set path for file
# budget_data.csv
csvpath = os.path.join("PyBank","budget_data.csv")

#Print headers of File
print("Financial Analysis")
print("-------------------------")

# Read the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header from Count
    header = next(csvreader)
    # Define variable for the total number of months by adding value of 1 for each row in csv file 
    totalMonths = sum(1 for row in csvfile)
    # Print number of rows
    print(f"Total Months: {totalMonths}")

# Read the csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header from count
    header = next(csvreader)
    # Assign list for Dates and Values (Total)
    Dates = []
    Total = []
    # Loop to add values of row to the lists
    for row in csvreader:
        Dates.append(str(row[0]))
        Total.append(int(row[1]))

#Print Variable netTotal by adding all values in list "Total"
netTotal = sum(Total)
print(f"Total: ${netTotal}")

#Calculate the difference values by looping througn the Total list and substracting a value from the previous one
Totaldiff = [Total[n]-Total[n-1] for n in range(1,len(Total))]
#Calculate the avg by dividing the sum of differences by the lenght of new list "Totaldiff"
avgdiff = round(sum(Totaldiff)/len(Totaldiff),2)
print(f"Averge Change: ${avgdiff}")

#Calculate Greatest Increase Value and Month by finding the Maximun value inside the list "Totaldiff" and it's index position to find the month.
greatestIncrease = max(Totaldiff)
maxMonth = Dates[(Totaldiff.index(greatestIncrease))+1]
print(f"Greatest Increase in Profits: {maxMonth} $({greatestIncrease})")

#Calculate Greatest Decrease Value and Month by finding the Minimun value inside the list "Totaldiff" and it's index position to find the month.
greatestDecrease = min(Totaldiff)
minMonth = Dates[(Totaldiff.index(greatestDecrease))+1]
print(f"Greatest Decrease in Profits: {minMonth} $({greatestDecrease})")

#Create file to write results
output_path=os.path.join("PyBank","pyBank_Output.txt")
file = open(output_path,'w')

#Write to file all results
file.write("Financial Analysis")
file.write("\n-------------------------")
file.write(f"\nTotal Months: {totalMonths}")
file.write(f"\nTotal: ${netTotal}")
file.write(f"\nAverge Change: ${avgdiff}")
file.write(f"\nGreatest Increase in Profits: {maxMonth} $({greatestIncrease})")
file.write(f"\nGreatest Decrease in Profits: {minMonth} $({greatestDecrease})")

file.close()