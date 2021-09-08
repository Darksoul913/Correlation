import plotly.express as px
import csv

with open("/Volumes/U/Python(WHJ)/correlation-master/data/Student Marks vs Days Present.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Marks In Percentage", y="Days Present", color="Roll No")
      fig.show()
