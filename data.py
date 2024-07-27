import numpy as np
import pandas as pd
import matplotlib as plt
import plotly.graph_objects as go
import plotly.express as px
import dash


latlong = pd.read_csv('E:\python\CampusX\project\Campusx\my-dash-app\Project using Plotly\district wise centroids.csv')

census = pd.read_csv('E:\python\CampusX\project\Campusx\my-dash-app\Project using Plotly\india-districts-census-2011.csv')

print(latlong.info())
print(census.info())

cols =['District code', 'District name', 'Population','Male','Female','Literate','Households_with_Internet']

census = census[cols]
# print(census.info())

data = latlong.merge(census, left_on='District', right_on='District name').drop(columns='District name')

# print(data.info())

data['sex_ratio'] = round((data['Female']/data['Male'])*100)
# print(data)

data['literacy_ratio'] = round((data['Literate']/data['Population'])*100)
# print(data)

data.drop(columns=['Male', 'Female', 'Literate'], inplace=True)

# data.to_csv('india.csv', index=False)








