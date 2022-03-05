import csv
import json
import requests


r = requests.get('https://recruitment.aimtechnologies.co/ai-tasks')
with open ("dialect_dataset.csv","r") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
        data.append(row[0])
        print(row) 
    
    with open ("data.json","w") as f: 
        json.dump(data , f)

print(r.status_code)