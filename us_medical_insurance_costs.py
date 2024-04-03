import csv

# Initialize an empty dictionary to store columns
medicalRecords = []


# Open the CSV file and read its contents into the list
with open('insurance.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Append each row as a dictionary
        medicalRecords.append(row)


# calculcating the average age.
# converting the ages into INT
total_age = sum(int(row['age']) for row in medicalRecords)
average_age = total_age / len(medicalRecords) if medicalRecords else 0

print("Average age:", round(average_age))
print(medicalRecords[0])

