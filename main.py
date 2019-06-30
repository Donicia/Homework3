import os
import csv

budget_data_path = r'C:\Users\donic\Desktop\CLASS\RICEHOU201906DATA1\HW\03-Python\Instructions\PyPoll\Resources\election_data.csv'

with open(budget_data_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    print(csv_reader)

    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
    for row in csv_reader:



    #The total number of votes cast
    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won
    #The winner of the election based on popular vote