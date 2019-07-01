import csv
import os

election_data = r'C:\Users\donic\Desktop\CLASS\RICEHOU201906DATA1\HW\03-Python\Instructions\PyPoll\Resources\election_data.csv'

votes = 0
winner_votes = 0
total_candidates = 0
candidate_options = []
candidate_votes = {}
greatest_votes = ["", 0]

with open(election_data) as file:
    reader = csv.DictReader(file)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    for candidate in candidate_votes:
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")

        winner = sorted(candidate_votes.items(), key=index(1), reverse=True)

print("Election Results")
print("-------------------------")
print("Total Votes " + str(votes))
print("-------------------------")
 