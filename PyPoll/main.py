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
vote_perc = 0.0
cand_list = {}
winner = 0
count = 0

# open csv
with open(PyPollcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for A in csvreader:

        # count = count + 1
        # CandAll.append(A[2])
        if A[2] in cand_list.keys():
            cand_list[A[2]] += 1
        else:
            cand_list[A[2]] = 1


vote_count = sum(cand_list.values())

print("Election Results")
print("-------------------------")
print(f"Total Votes: {vote_count}")
print("-------------------------")

for C in cand_list:
    vote_perc = round((cand_list[C] * 100) / vote_count, 3)
    print(f"{C}: {vote_perc}% ({cand_list[C]})")
    if winner < cand_list[C]:
        winner = cand_list[C]
        Elected = C
print("-------------------------")
print(f"Winner: {Elected}")
print("-------------------------")

with open(writeFile, 'w') as outputFile:
    outputFile.write("Election Results\n")
    outputFile.write("-------------------------\n")
    outputFile.write(f"Total Votes: {vote_count}\n")
    outputFile.write("-------------------------\n")
    for C in cand_list:
        vote_perc = round((cand_list[C] * 100) / vote_count, 3)
        outputFile.write(f"{C}: {vote_perc}% ({cand_list[C]})\n")
    # if winner < cand_list[C]:
    #     winner = cand_list[C]
    #     Elected = C
    outputFile.write("-------------------------\n")
    outputFile.write(f"Winner: {Elected}\n")
    outputFile.write("-------------------------")
