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

# make the place for the csv file for PyBank

PyBankcsv = os.path.join("Resources", "budget_csv.csv")

# Make a place for the data

profit = []
monthly_changes = []
date = []


# input variables
initial_profit = 0
total_profit = 0
total_change_profits = 0
count = 0

# Open csv
with open(PyBankcsv) as Bank_file
