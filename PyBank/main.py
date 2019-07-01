import os
import csv

date =[]
Profit_Losses = []

budget_data_path = r'C:\Users\donic\Desktop\CLASS\RICEHOU201906DATA1\HW\03-Python\Instructions\PyBank\Resources\budget_data.csv'

with open(budget_data_path) as File:
    csv_reader=csv.reader(File)

    next(csv_reader)    

    for row in csv_reader:
        date.append(row[0])
        Profit_Losses.append(int(row[1]))

Profit_Losses_Change = []
#The average of the changes in "Profit/Losses" over the entire period
for i in range(1, len(Profit_Losses)):
    Profit_Losses_Change.append(Profit_Losses[i] - Profit_Losses[i-1])

print(f"Average Revenue Change: ${sum(Profit_Losses_Change)/len(Profit_Losses_Change)}")

#The greatest increase in profits (date and amount) over the entire period
print(f"Greatest Increase in Revenue: {date[Profit_Losses_Change.index(max(Profit_Losses_Change))+1]} ({max(Profit_Losses_Change)})")

#The greatest decrease in losses (date and amount) over the entire period
print(f"Greatest Decrease in Revenue: {date[Profit_Losses_Change.index(min(Profit_Losses_Change))+1]} ({min(Profit_Losses_Change)})\n")   

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(date)}")
print(f"Total Revenue: ${sum(Profit_Losses)}")
print(f"Average Revenue Change: ${sum(Profit_Losses_Change)/len(Profit_Losses_Change)}")
print(f"Greatest Increase in Revenue: {date[Profit_Losses_Change.index(max(Profit_Losses_Change))+1]} ({max(Profit_Losses_Change)})")
print(f"Greatest Decrease in Revenue: {date[Profit_Losses_Change.index(min(Profit_Losses_Change))+1]} ({min(Profit_Losses_Change)})\n")


Output_file = r'C:\Users\donic\Desktop\Homework\Homework 3\Python Homework\PyBank\PyBank.txt'

with open(Output_file) as txt_file:
    txt_file.write(f"Total Months: {len(date)}")
    txt_file.write("\n")
    txt_file.write(f"Total Revenue: ${sum(Profit_Losses)}")
    txt_file.write("\n")
    txt_file.write(f"Average Revenue Change: ${sum(Profit_Losses_Change)/len(Profit_Losses_Change)}")
    txt_file.write("\n")
    txt_file.write(f"Greatest Increase in Revenue: {date[Profit_Losses_Change.index(max(Profit_Losses_Change))+1]} ({max(Profit_Losses_Change)})")
    txt_file.write("\n")
    txt_file.write(f"Greatest Decrease in Revenue: {date[Profit_Losses_Change.index(min(Profit_Losses_Change))+1]} ({min(Profit_Losses_Change)})\n")
