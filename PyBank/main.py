# The total number of months included in the datase
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
os.chdir(os.path.dirname(os.path.abspath(__file__)))
readFile = "./Resources/budget_data.csv"
#writeFile = "./Analysis/Analysis.txt"

# make the place for the csv file for PyBank

writeFile = "./Analysis/Analysis.txt"

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

    # Print out profits and sums
    print(f"Financial Analysis")
    print("-------------------------")
    print(f"totalprofit:{total_profit}")
    print(f"decProfit{(decDate)}{decProfit}")
    print(f"incProfit{(incDate)}{incProfit}")
    print(f"totalmonth:{count}")
    print(f"avgChng:{round(avgChng,2)}")

# Write out results in analysis file
with open('Analysis.txt', 'w') as text:
    text.write(f" Finacial Analysis\n")
    text.write("-------------------------\n")
    text.write(f"Total Profit: {total_profit}\n")
    text.write(f"Profit Decreased {(decDate)} {decProfit}\n")
    text.write(f"Profit Increased {(incDate)} {incProfit}\n")
    text.write(f"Total Months: {count}\n")
    text.write(f"Average Change: {round(avgChng,2)}\n")
