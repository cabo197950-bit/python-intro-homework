import csv

clean_rows = []
skipped_rows = []
attempted = 0

try:
    with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)

        attempted = 0

        for row in reader:
            attempted += 1

            try:
                if None in row:
                    raise ValueError("Extra column found")

                name = row["name"]
                category = row["category"]
                amount = float(row["amount"])

                clean_rows.append({
                    "name": name,
                    "category": category,
                    "amount": amount
                })

            except (ValueError, KeyError) as error:
                skipped_rows.append({
                    "row": row,
                    "reason": str(error)
                })

except FileNotFoundError:
    print("The data file could not be found.")

parsed = len(clean_rows)
skipped = len(skipped_rows)

print(f"Attempted rows: {attempted}")
print(f"Parsed rows: {parsed}")
print(f"Skipped rows: {skipped}")

print("\nSkipped row reasons:")
for item in skipped_rows:
    print(f"{item['row']} - {item['reason']}")

print("\nClean data:")
for row in clean_rows:
    print(row)