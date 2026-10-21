
import json
import csv
from urllib.request import urlopen

# Fetch data from a public REST API
url = "https://jsonplaceholder.typicode.com/posts"

with urlopen(url) as response:
    data = json.loads(response.read().decode("utf-8"))

print("Total records:", len(data))
print("First record:", data[0])

# Save the JSON data as a CSV file
with open("api_data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["userId", "id", "title", "body"]
    )
    writer.writeheader()
    writer.writerows(data)

print("Success! CSV file created: api_data.csv")
