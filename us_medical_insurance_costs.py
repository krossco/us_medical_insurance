import csv

# Initialize an empty dictionary to store columns

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []


# Open the CSV file and read its contents into the list
def csv_data(lst, csv_file, column_name):
    # open csv file
    with open(csv_file) as csv_info:
        # read the data from the csv file
        csv_dict = csv.DictReader(csv_info)
        # loop through the data in each row of the csv 
        for row in csv_dict:
            # add the data from each row to a list
            lst.append(row[column_name])

    
csv_data(ages, 'insurance.csv', 'age')
csv_data(sexes, 'insurance.csv', 'sex')
csv_data(bmis, 'insurance.csv', 'bmi')
csv_data(num_children, 'insurance.csv', 'children')
csv_data(smoker_statuses, 'insurance.csv', 'smoker')
csv_data(regions, 'insurance.csv', 'region')
csv_data(insurance_charges, 'insurance.csv', 'charges')


print(ages)

oldestAge = max(ages)
youngestAge = min(ages)
averageAge = sum(ages)/len(ages)
print('Average age: ', averageAge)