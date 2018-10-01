# Imports
from csv import QUOTE_ALL, DictWriter, DictReader

def write_data(result_list):
    with open("result.csv",'w') as csvfile:
        csvwriter = DictWriter(csvfile, fieldnames=result_list[0].keys(), quoting=QUOTE_ALL, extrasaction='ignore')
        csvwriter.writeheader()
        try:
            csvwriter.writerows(result_list)
        except Exception as error:
            print(error)
            csvwriter.writerows("error")
