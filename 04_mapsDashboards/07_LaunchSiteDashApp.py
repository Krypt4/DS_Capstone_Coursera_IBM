import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv("../data/dataset_part_2.csv")

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id="site-dropdown",
        options=[{"label": i, "value": i} for i in df["LaunchSite"].unique()],
        value=df["LaunchSite"].unique()[0]
    ),
    
    dcc.Graph(id="pie-chart")
])

@app.callback(
    dash.dependencies.Output("pie-chart", "figure"),
    [dash.dependencies.Input("site-dropdown", "value")]
)
def update_graph(selected_site):
    filtered_df = df[df["LaunchSite"] == selected_site]
    
    fig = px.pie(
        filtered_df,
        names="Class",
        title="Success vs Failure"
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)