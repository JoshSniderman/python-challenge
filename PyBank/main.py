import os
import csv

csvpath = os.path.join('./Resources', 'budget_data.csv')

with open(csvpath, newline = '', encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader, None)
    
    months = 0
    profits = 0
    PrevProfit = 0
    NewProfit = 0
    ProfitChange = []
    GreatProfit = 0
    GreatDate = ''
    LeastProfit = 0
    LeastDate = ''
    
    for row in csvreader:
        months += 1
        profits += int(row[1])
        if PrevProfit != 0:
            NewProfit = int(row[1]) - PrevProfit
            ProfitChange.append(NewProfit)
            if NewProfit > GreatProfit:
                GreatProfit = NewProfit
                GreatDate = row[0]
            if NewProfit < LeastProfit:
                LeastProfit = NewProfit
                LeastDate = row[0]
        PrevProfit = int(row[1])
        
filetxt = open("Bank_Analysis.txt", "w")

analysis = f'''\nFinancial Analysis \n---------------------------- \n
                Total Months: {months} \n
                Total: ${profits} \n
                Average Change: ${round(sum(ProfitChange) / (months-1), 2)} \n
                Greatest Increase in Profits: {GreatDate} (${GreatProfit}) \n
                Greatest Decrease in Profits: {LeastDate} (${LeastProfit}) '''

print(analysis)
filetxt.write(analysis)