import csv
import datetime

sn1 = input("Scan Barcode 1" , )
sn2 = input("Scan Barcode 2")
sn3 = input("Scan Barcode 3")
sn4 = input("Scan Barcode 4")
sn5 = input("Scan Barcode 5")
sn6 = input("Scan Barcode 6")


with open('test.csv', mode='w') as csv_file:
    fieldnames = ['SN', 'Time', 'Data']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'SN': sn1, 'Time': 'TBD', 'Data': 'TBD'})
    writer.writerow({'SN': sn2, 'Time': 'TBD', 'Data': 'TBD'})
    writer.writerow({'SN': sn3, 'Time': 'TBD', 'Data': 'TBD'})
    writer.writerow({'SN': sn4, 'Time': 'TBD', 'Data': 'TBD'})
    writer.writerow({'SN': sn5, 'Time': 'TBD', 'Data': 'TBD'})
    writer.writerow({'SN': sn6, 'Time': 'TBD', 'Data': 'TBD'})




