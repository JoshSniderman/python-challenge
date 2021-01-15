import os
import csv

csvpath = os.path.join('./Resources', 'election_data.csv')

with open(csvpath, newline = '', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    
    TotalVotes = 0
    rows = 0
    Candidates = []
    CandidateVotes = []
    
    for row in csvreader:
        TotalVotes += 1
        if row[2] not in Candidates:
            Candidates.append(row[2])
            CandidateVotes.append(1)
        else:
            CandidateVotes[Candidates.index(row[2])] += 1
  
    file = open("Election_analysis.txt", "w")
    
    print(f'\nElection Results\n-------------------------')
    print(f'Total Votes: {TotalVotes}\n-------------------------')
    file.write(f'\nElection Results\n-------------------------\n')
    file.write(f'Total Votes: {TotalVotes}\n-------------------------\n')

    for name in Candidates:
        tally = f'{name}: {round(CandidateVotes[Candidates.index(name)] / TotalVotes * 100)}.000% ({CandidateVotes[Candidates.index(name)]})'
        print(tally)
        file.write(f'{tally}\n')
        
    VoteMax = max(CandidateVotes)
    winner = Candidates[CandidateVotes.index(VoteMax)]
    print(f'-------------------------\nWinner: {winner}\n-------------------------')
    file.write(f'-------------------------\nWinner: {winner}\n-------------------------')
    
    file.close()