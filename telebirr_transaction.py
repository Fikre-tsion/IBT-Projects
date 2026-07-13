# Read a file of TeleBirr transactions, summarise them by customer using a dictionary,
# and handle a missing file gracefully.

# Step by step solution
# 1. Read transactions.txt line by line (name,amount per line).
with open("transaction.txt") as f:
    for line in f:
        print(line.strip())

# 2. Build a dict mapping each customer to their total spend.
# customer= {
#     "name":"Abebe",
#     "total_spend":250.00,
# }
customer = {"Abebe": 250.00, "Kalkidan": 120.50, "Mekdes": 300.00, "Yonas": 45.00, "Selam": 500.00}

# 3. Print each customer and total, sorted highest first.
for name, total_spend in customer.items():
    print(f"{name}:{total_spend}")
# 4. Wrap the file read in try / except for a missing file
try:
    with open("transaction.txt") as f:
        for line in f:
            print(line.strip())
except FileNotFoundError:
    print("Missing file found.")

# 5. Write the summary to report.txt, then push to GitHub.
with open("report.txt", "x") as f:
    for line in f:
        f.write(f"")

