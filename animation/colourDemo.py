import csv
import plotly.express as px
import random

with open('states.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
       fig = px.choropleth(locations=[row['state']],
                    locationmode="USA-states",
                    color=[random.randint(0,10)],
                    scope="usa")
       break
    fig.update_layout( title_text='2001 US Hepatitis<br>(Hover for breakdown of score)')
file.close()

fig.show()

