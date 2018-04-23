import csv
with open('interview_scent.csv', 'rb') as csvfile:
     interview_scent = csv.reader(csvfile, delimiter=',', quotechar='"')
     fields = []
     distinct = {}
     count = 0
     total_rows = 0
     for i, row in enumerate(interview_scent):
	if i == 0:
		fields = row
	else:
		if row[4] != 'None':
			count += 1
			if row[4] not in list(distinct.keys()):
				distinct[row[4]] = 1
			else:
				distinct[row[4]] += 1

		total_rows += 1


print "Total Rows: " + str(total_rows)
print "Fields: "
print fields
print "Count where Predictions is not None: " + str(count)
#for key in distinct:
#	print key + " : " + str(distinct[key])


with open('results1.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Predictions Not None'] + list(distinct.keys()) )
    spamwriter.writerow([count] + list(distinct.values()))

