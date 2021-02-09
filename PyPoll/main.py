# # Make a new place for CSV PyPoll
import os
import csv
os.chdir(os.path.dirname(os.path.abspath(__file__)))
PyPollcsv = "./Resources/election_data.csv"
writeFile = "./Analysis/Analysis.txt"

# # make vcolumns and place for data
voter_id = []
voter_cand = []
county = []
CandAll = []

# # make variables
vote_count = 0
vote_perc = 0
cand_list = {"Candidate": [], "Votes": [], "Vote Percent": []}
winner = 0
count = 0

# open csv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for A in csvreader:

        count = count + 1
        CandAll.append(A[2])
        if A[2] not in cand_list["Candidate"]:
            cand_list["Candidate"].append(A[2])
    for i in cand_list:
        print(f"{cand_list[i]}: {vote_perc}% ")
