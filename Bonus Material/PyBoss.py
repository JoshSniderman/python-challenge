import os
import csv

csvpath = os.path.join('./Resources', 'PyBoss.csv')

with open(csvpath, newline='', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    
    EmpID = []
    Block = []
    FirstName = []
    LastName = []
    DOB = []
    SSN = []
    State = []
    StateName = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Washington DC","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
    StateAbb = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    x = 0
        
    for row in csvreader:
        EmpID.append(row[0])
        Block = row[1].split(' ')
        FirstName.append(Block[0])
        LastName.append(Block[1])
        Block = row[2].split('-')
        DOB.append(f'{Block[0]}/{Block[1]}/{Block[2]}')
        Block = row[3].split('-')
        SSN.append(f'***-**-{Block[2]}')
        State.append(StateAbb[StateName.index(row[4])])
        
with open('Employees.csv', 'w', newline = '') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(['Employee ID', 'First Name', 'LastName', 'Date of Birth', 'SSN', 'State'])
    
    for x in EmpID:
        a = EmpID.index(x)
        csvwriter.writerow([EmpID[a], FirstName[a], LastName[a], DOB[a], SSN[a], State[a]])