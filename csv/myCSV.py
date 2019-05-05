# comma seperated values CSV
import csv
from statistics import mean
with open('E:/PythonProjects/csv/grades.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        #print (row)
        name = row[0]
        these_grades = list()
        # The list will contain integer form of grades
        for grade in row[1:]: #because the first one is the name
            these_grades.append(int(grade))
        print('average of %10s is %5.2f'%(name,mean(these_grades)))



