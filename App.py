import pandas as pd
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load data
df = pd.read_csv("formatted_data.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Create Dash app
app = Dash(__name__)

# App layout
app.layout = html.Div(
    style={
        "fontFamily": "Arial",
        "backgroundColor": "#f4f6f8",
        "padding": "30px"
    },
    children=[
        html.H1(
            "Pink Morsels Sales Visualiser",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        html.Div(
            style={
                "width": "50%",
                "margin": "auto",
                "padding": "20px",
                "backgroundColor": "white",
                "borderRadius": "10px",
                "boxShadow": "0 4px 8px rgba(0,0,0,0.1)"
            },
            children=[
                html.Label(
                    "Select Region:",
                    style={
                        "fontWeight": "bold",
                        "marginBottom": "10px",
                        "display": "block"
                    }
                ),

                dcc.RadioItems(
                    id="region-selector",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    style={"marginBottom": "20px"}
                ),

                dcc.Graph(id="sales-line-chart")
            ]
        )
    ]
)

# Callback to update graph
@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Sales Over Time",
        labels={
            "date": "Date",
            "sales": "Total Sales"
        }
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="white",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)


