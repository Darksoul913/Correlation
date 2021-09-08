import csv
import numpy as np


def getDataSource(data_path):
    Coffee_in_ml = []
    sleep_in_hours = []
    with open('/Volumes/U/Python(WHJ)/correlation-master/data/Student Marks vs Days Present.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee_in_ml.append(float(row["Marks In Percentage"]))
            sleep_in_hours.append(float(row["Days Present"]))

    return {"x" : Coffee_in_ml, "y": sleep_in_hours}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Cups of cofee and Hours of sleep :-  \n--->",correlation[0,1])

def setup():
    data_path  = "/Volumes/U/Python(WHJ)/correlation-master/data/cups of coffee vs hours of sleep.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
