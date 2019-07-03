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
        Candidates_Per[Candidate] = round(Candidates[Candidate]/votes,2)

        Winner = max(Candidates, key=lambda i:Candidates[i])


print("Election Results") 
print("-------------------------")
print(f"Total Votes: {votes}")
print("-------------------------")
print(f"{Candidates}")
print(f"{Candidates_Per}")
print("-------------------------")
print(f"Winner: {Winner}")
print("-------------------------")

PyPoll = r'C:\Users\donic\Desktop\Homework\Homework 3\Python Homework\PyPoll\election_data.txt'

Line_1 = ("Election Results")
Line_12 =("-------------------------")
Line_2 = (f"Total Votes: {votes}")
Line_22 = ("-------------------------")
Line_3 = (f"{Candidates}")
Line_4 = (f"{Candidates_Per}")
Line_5 = ("-------------------------")
Line_6 = (f"Winner:{Winner}")
LIne_7 = ("-------------------------")



with open("PyPoll.txt", "w") as output:
    output.write(str(Line_1))
    output.write('\n')
    output.write(str(Line_12))
    output.write('\n')
    output.write(str(Line_2))
    output.write('\n')
    output.write(str(Line_22))
    output.write('\n')
    output.write(str(Line_3))
    output.write('\n')
    output.write(str(Line_4))
    output.write('\n')
    output.write(str(Line_5))
    output.write('\n')
    output.write(str(Line_6))
    output.write('\n')
    output.write(str(LIne_7))
