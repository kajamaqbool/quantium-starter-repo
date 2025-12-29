import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Load the processed data
df = pd.read_csv("formatted_data.csv")

# Convert date column to datetime and sort by date
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsels Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Total Sales"
    }
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(
            "Pink Morsels Sales Visualiser",
            style={"textAlign": "center"}
        ),
        dcc.Graph(figure=fig)
    ]
)

if __name__ == "__main__":
    app.run(debug=True)

