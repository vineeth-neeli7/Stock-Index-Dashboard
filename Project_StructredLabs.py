from preswald import text, plotly, connect, get_df, table, slider, daterange
import pandas as pd
import plotly.express as px

text("# Stock Dashboard")
text("This is my first app Analyze and explore stock data. 🎉")

# Load the CSV
connect() # load in all sources, which by default is the sample_csv
df = get_df('indexData.csv')

text("# data overview")
table(df.head())

df.dropna(inplace=True)

# Adjusting date formate if any
df["Date"] = pd.to_datetime(df["Date"])

#Filter(Volume)
volume_threshold = slider("Minimum Volume",min_val=0,max_val=int(df["Volume"].max()),default=100000)

# Filter (Date Range)
date_start, date_end = daterange("Select Date Range",min_date=df["Date"].min(),max_date=df["Date"].max())
df_filtered = df[(df["Volume"] >= volume_threshold) & (df["Date"] >= date_start) & (df["Date"] <= date_end)]

# Create a scatter plot
fig = px.scatter(df_filtered, x='Open', y='Close', color = "Index Name", hover_data=["Date","Volume"],
                 title='Open vs. Close Prices',
                 labels={'Open': 'Opening  Price', 'Close': 'Closing Price'})

fig.update_layout(template='plotly_white')
# Show the plot
plotly(fig)

# Show the data
table(df_filtered,title="Stock Data - Filtered") 