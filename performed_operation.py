"""The code reads a CSV file containing monthly operations.
    The code calculates the total income, total expenses and transaction amount for each month
    At the end creates two bar charts to visualize final balance for each month
    and number of operations (income and expenses) for each month"""

import csv
from datetime import datetime
import matplotlib.pyplot as plt


statistics = {}

with open('operacje.csv', encoding='utf8', newline='') as csvfile:
    columns = ['data', 'rodzaj operacji', 'opis operacji', 'kwota operacji']
    # dane pobrane z pliku
    reader = csv.DictReader(csvfile)
    for line in reader:
        operation_date = datetime.strptime(line['data'], '%Y-%m-%d')
        # change to month format
        if operation_date.strftime('%B') not in statistics:
            statistics[operation_date.strftime('%B')] = {
                "total": 0,
                "income_quantity": 0,
                "expense_quantity": 0
            }
        if line['rodzaj operacji'] == 'przychód':
            statistics[operation_date.strftime('%B')]['total'] += float(line['kwota operacji'])
            statistics[operation_date.strftime('%B')]['income_quantity'] += 1
        else:
            statistics[operation_date.strftime('%B')]['total'] -= float(line['kwota operacji'])
            statistics[operation_date.strftime('%B')]['expense_quantity'] += 1

fig, ax = plt.subplots()
months = list(statistics.keys())
totals = []
total_operation = []

for month, data in statistics.items():
    totals.append(data['total'])
    total_operation.append(data['income_quantity'] + data['expense_quantity'])


ax.bar(months, totals)
plt.xlabel("Month")
plt.ylabel("Balance")
plt.title("Final balance in the month")
plt.savefig('summary.png')

fig, ax = plt.subplots()
ax.bar(months, total_operation)
plt.xlabel("Month")
plt.ylabel("Operation amount")
plt.title("Amount of operation in the month")
plt.savefig('number-of-operation.png')
