# Read a file of TeleBirr transactions, summarise them by customer using a dictionary,
# and handle a missing file gracefully.


from fileinput import filename
from functools import total_ordering

# Step by step solution
# 1. Read transactions.txt line by line (name,amount per line).
INPUT_FILE= "transaction.txt"
OUTPUT_FILE= "report.txt"



def read_transaction(filename):
    # Empty dict to be filled with data after reading
    total_spend = {}
    try:
        with open("transaction.txt","r") as f:
            for line in f:
                cleaned_line=line.strip()
                if not cleaned_line:
                    continue

                name, str_amount = cleaned_line.split(",")
                #Here the amount is string, so it need casting to float.
                float_amount = float(str_amount)

                total_spend[name]=total_spend.get(name,0.0) + float_amount

    except FileNotFoundError:
        print(f"ERROR! The required file '{filename}' is not found")
        return {}
    return total_spend


# 4. Wrap the file read in try / except for a missing file

def print_summary(total_spend):
    if not total_spend:
        print("No transaction data is available to summarize.")
        return

    sorted_total= sorted(total_spend.items(), key=lambda item: item[1],reverse=True)
    for name, total in sorted_total:
        print(f"{name}:{total_spend:.2f}")

def write_report(totals,filename):
    if not total:
        return







#     try:
#     with open("transaction.txt") as f:
#         for line in f:
#             print(line.strip())
# except FileNotFoundError:
#     print("Missing file found.")
#
# # 5. Write the summary to report.txt, then push to GitHub.
# with open("report.txt", "x") as f:
#     for line in f:
#         f.write(f"")
#
