import csv

csvfile = open('/Users/ziyaozhou/Desktop/Datamining_sample/mt-OGT Parterner Data/jctt1.csv','r')
reader = csv.DictReader(csvfile)
count = 0
countUrl = 0
for row in reader:
    if count < 100000:
        #print(row)
        #if len(row['Uniport Accession Website']) != 0:
        num = row['Number']
        uan = row['Uniport Accession Number']
        url = row['Uniport Accession Website']
        item = [num,uan,url]
        print(item)
        count = count+1
