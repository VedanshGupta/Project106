import plotly.express as px
import csv

with open("data2.csv") as csv_file:
	df = csv.DictReader(csv_file)
	fig = px.scatter(df, x="Coffee in ml", y="\tsleep in hours")
	fig.show()