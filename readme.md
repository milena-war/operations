Code is responsible for reading a CSV file using context manager. Calculates the total income and expenses for each month. 
The code uses the DictReader class from the csv module to read the CSV file and extract the data into a dictionary.

The code loops through each line in the CSV file and extracts the date, 
operation type, operation description, and operation amount. 
Then uses the datetime module to convert the date string into a datetime object.

The code then checks if the month represented by the datetime object is present in the statistics dictionary.
If not, it adds a new entry with the total, income, and expense quantities initialized to 0.

If the operation type is income, the code adds the operation amount to the total income
and increments the income quantity. 
If the operation type is expense, the code subtracts the operation amount from 
the total expense and increments the expense quantity.

Finally, the code creates two bar charts using the Matplotlib library. 
The first bar chart shows the final balance for each month, 
and the second bar chart shows the total number of operations (income and expenses) for each month.
