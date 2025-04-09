import pandas as pd
import plotly.graph_objects as go

# Loading the data from CSV file
df = pd.read_csv("indexData.csv")

# Removing rows that have missing values
df.dropna(inplace=True)

# Changing the Date column to date format
df["Date"] = pd.to_datetime(df["Date"])

# Getting all unique index names
index_names = df["Index"].unique()

# Making an empty figure to draw the chart
fig = go.Figure()

# Adding lines for each index one by one
for index in index_names:
    df_index = df[df["Index"] == index]  # Only data for one index
    fig.add_trace(
        go.Scatter(
            x=df_index["Date"],       # X-axis is the date
            y=df_index["Open"],       # Y-axis is the opening price
            mode="lines",             # Line chart
            name=index,               # Name in legend
            visible=(index == index_names[0])  # Show only the first one by default
        )
    )

# Making dropdown to choose between different indices
dropdown_buttons = [
    {
        "label": index,  # Button name
        "method": "update",
        "args": [
            {"visible": [i == j for j in range(len(index_names))]},  # Show only the selected one
            {"title": f"Opening Prices --------------   for {index}"}  # Change title
        ]
    }
    for i, index in enumerate(index_names)
]

# Designing how the chart looks
fig.update_layout(
    title=f"Opening Prices  -------------   for {index_names[0]}",
    xaxis_title="Date",
    yaxis_title="Opening Price",
    template="plotly_white",

    # Putting the dropdown on the chart
    updatemenus=[{
        "buttons": dropdown_buttons,
        "direction": "down",
        "showactive": True,
        "x": 0.1,
        "xanchor": "left",
        "y": 1.15,
        "yanchor": "top"
    }],

    # Adding a date range slider and zoom options
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(visible=True),
        type="date"
    )
)

# Hiding the small slider below the chart
fig.update_layout(xaxis_rangeslider_visible=False)

# Showing the chart
fig.show()
