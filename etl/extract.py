import csv
def extract_data(path="data/input.csv"):
    rows=[]
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    
    # these changes are done to test feature branch
    # add 2nd change
    return rows