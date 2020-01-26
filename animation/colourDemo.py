import plotly.express as px

fig = px.choropleth(locations=["CA", "TX", "NY", "FL"], locationmode="USA-states", color=[1,2,3,5], scope="usa")
fig.show()