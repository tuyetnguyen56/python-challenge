# In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called budget_data.csv. The dataset is composed of two columns: Date and Profit/Losses. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:


#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period


#Create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Define and default variables
total_months = 0
total_revenue = 0
prev_revenue = 0
revenue_change= 0
average_change = 0
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
month_of_change = []
revenue_change_list = []



# open csv file
csvpath = os.path.join("budget_data.csv")
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first(skip this step if there is no header) 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Loop through the data
    for row in csvreader:

        # Track the totals for months and revenue
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Profit/Losses"])

        # Track the revenue change
        revenue_change = int(row["Profit/Losses"]) - prev_revenue

        # Reset the previous revenue
        prev_revenue = int(row["Profit/Losses"])

        # Calculate the greatest increase
        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change

        # Calculate the greatest decrease
        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change

# Calculate the Average Revenue Change
average_change = str(round(sum(revenue_change_list) / len(revenue_change_list)

# Print results
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total Revenue: ${total_revenue}")
    print(f"Average Revenue Change: ${average_change}")
    print(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})")
    print(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Print the output (to terminal)

with open("data.txt", 'w') as file:
	file.write(f"Financial Analysis")
	file.write(f"---------------------------\n") 
	file.write(f"Total Months: {total_months}\n")
	file.write(f"Total Revenue: ${total_revenue}\n")
	file.write(f"Average Revenue Change: ${average_change}\n")
	file.write(f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n")
	file.write(f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")



