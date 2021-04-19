salary = 67000.00
tax = 13322.00
hexDebtRepayment = 2345.00

postTaxIncome = salary - tax - hexDebtRepayment 
print("Post tax income (yearly): $" + str(postTaxIncome))

mothlyIncome = (postTaxIncome/12)
print("Post tax income (monthly): $" + str(mothlyIncome))

weeklyIncome = (postTaxIncome/12)/4
print("Post tax income (weekly): $" + str(weeklyIncome)) 

def weeklyCosts():
    rent = 0
    gym = 14.00
    food = 150.00
    carLoan = 0
    fixedCostsWeekly = [rent, gym, food, carLoan] 

    return sum(fixedCostsWeekly)

def monthlyCosts():
    netflix = 15.99
    spotify = 11.99
    phone = 88.76
    elec = ((711.00)/4)/4
    internet = 90.00/4.00
    fuel = 80.00
    mortage = 1500
    games = 20.00
    carLoan = 0
    fixedMonthlyCosts = [netflix, spotify, phone, elec, internet, fuel, mortage, games, carLoan]

    return sum(fixedMonthlyCosts)

def yearlyCosts():
    carRego = 1000.00
    insurance = 308.93
    pinkSlip = 40
    microsoft = 90
    healthIns = 747.60
    fixedYearlyCosts = [carRego, insurance, pinkSlip, microsoft, healthIns]

    return sum(fixedYearlyCosts)

    
totalYearlyExpenses = sum([yearlyCosts(), monthlyCosts()*12, weeklyCosts()*52])
print("Total yearly expenses: $" + str(totalYearlyExpenses))

yearlyRemainder = postTaxIncome - totalYearlyExpenses
print("Post expense total: $" + str(yearlyRemainder))

sp = 0.8
yearlySaving = yearlyRemainder * sp
monthlySaving = yearlyRemainder/12 

print("Money Saved at " + str(sp*100) + "% (yearly): $" + str(round(yearlySaving, 2)))
print("Money Saved at " + str(sp*100) + "% (monthly): $" + str(round(monthlySaving, 2)))


pissBuffer = yearlyRemainder - yearlySaving
print("Piss buffer (yearly): $" + str(round(pissBuffer)))
MonthlyOverSpend = pissBuffer/12
print("Piss buffer (monthly): $" + str(round(MonthlyOverSpend, 2)))
weeklyOverSpend = pissBuffer/52
print("Piss buffer (weekly): $" + str(round(weeklyOverSpend, 2)))

# Percantage of costs proportional to income
rent_per = ((((167.50)*4)*12)/postTaxIncome)*100

print("Rent as a percentage of post tax income: " + str(round(rent_per, 2)) + "%")