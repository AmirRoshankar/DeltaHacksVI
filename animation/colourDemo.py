import plotly.express as px

fig = px.choropleth(locations=["AK", "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "FL",
                               "GA", "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA",
                               "MD", "ME", "MI", "MN", "MO", "MS", "MT", "NC", "ND", "NE",
                               "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI",
                               "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY"],
                locationmode="USA-states",
                color=[1,2,2,1,2,1,3,5,1,6,
                           1,2,2,1,2,1,3,5,1,6,
                           1,2,2,1,2,1,3,5,1,6,
                           1,2,2,1,2,1,3,5,1,6,
                           1,2,2,1,2,1,3,5,1,6,10],
                scope="usa")

fig.update_layout( title_text='2001 US Hepatitis<br>(Hover for breakdown of score)')


fig.show()

