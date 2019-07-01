import os
import csv

election_data = r'C:\Users\donic\Desktop\CLASS\RICEHOU201906DATA1\HW\03-Python\Instructions\PyPoll\Resources\election_data.csv'
 
votes = 0
Candidate =[]
Candidates = {"Khan":0,"Correy":0,"Li":0,"O'Tooley":0}
Candidates_Per = {"Khan":0,"Correy":0,"Li":0,"O'Tooley":0}
with open(election_data, newline="") as File:
    csv_reader = csv.reader(File)
    next(csv_reader)
    
    for row in csv_reader:
        votes = votes + 1
    
    #The total number of votes each candidate won
        Candidates[row[2]]+= 1
   #The percentage of votes each candidate won
    for Candidate in Candidates:
        Candidates_Per[Candidate] = Candidates[Candidate]/votes

print("Election Results")
print("-------------------------")
print(f"Total Votes: {votes}")
print("-------------------------")
print(f"{Candidates}")
print(f"{Candidates_Per}")
print("-------------------------")
print(f"Winner:{max(Candidates)}")

output_file = r'C:\Users\donic\Desktop\Homework\Homework 3\Python Homework\PyPoll\election_data.txt'

with open(output_file) as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("{Candidates}")
    txt_file.write("{Candidates_Per}")
    txt_file.write("Total Votes " + str(votes))
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner" + {max(Candidates)})
    