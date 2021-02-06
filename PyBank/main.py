# The total number of months included in the dataset


# The net total amount of "Profit/Losses" over the entire period


# Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes


# The greatest increase in profits(date and amount) over the entire period


# The greatest decrease in losses(date and amount) over the entire period
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

# Import both the os and csv
import os
import csv

# specify the directory
# os.chdir(os.path.dirname(os.path.abspath(__file__)))
readFile = os.path.join("Resources/budget_data.csv")

# make the place for the csv file for PyBank

#PyBankcsv = os.path.join("./Resources/budget_data.csv")

#readFile = "./Resources/budget_data.csv"
#writeFile = "./Analysis/Analysis.txt"

# Make a place for the data


# The total number of months included in the dataset
profit = []
date = []


# input variables
initial_profit = 0
total_profit = 0
total_change_profits = []
count = 0


#
with open(readFile) as csvfile:

 # read the csvfile and store it in info
    info = csv.reader(csvfile, delimiter=",")
    header = next(info)
    for A in info:
        # print(row)
        count = count + 1
        profit.append(int(A[1]))
        date.append(A[0])

    for B in profit:
        total_profit = total_profit + B

    for C in range(1, len(profit)):
        total_change_profits.append(int(profit[C]) - int(profit[C - 1]))

# Create Variables
decProfit = min(total_change_profits)
incProfit = max(total_change_profits)
decDate = date[total_change_profits.index(decProfit) + 1]
incDate = date[total_change_profits.index(incProfit) + 1]
avgChng = sum(total_change_profits) / len(total_change_profits)

#total_months = total_months + [1]
#date = A[0]
#profit = float(A[1])
# print(profit)
# print(date)
# print(f"total_months:{total_months}")

# write to file

# with open(writeFile, "w") as text:
# text.write()
# for p in profit:
# text.write(str(p))
# add a new line character to start a new line
# text.write("\n")
# length of list
# Total Momths included in data set
#
# print(f"total_months:{total_months}")
# add up all of the profit column
#
