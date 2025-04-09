project:
  title: **Stock Market Interactive Dashboard**
  description:
    This project visualizes **stock market index data** using an interactive **Plotly-based dashboard**.
    It allows users to explore the **opening prices over time** for multiple indices using **dropdown selection** and **date range filtering**.
    The chart is clean, responsive, and highlights **stock trends over time**.

technologies:
  language: **Python**
  libraries:
    - **pandas**: Data manipulation and cleaning
    - **plotly**: Interactive plotting and charting

features:
  - Load and clean **large stock index datasets** from CSV
  - Display **line chart** of opening prices over time
  - **Dropdown filter** to view individual stock indices
  - **Date filtering** with zoom and range selector
  - **Dynamic and responsive UI** powered by Plotly

data:
  source: **Kaggle** or open stock index datasets
  file_used: **indexData.csv**
  columns_required:
    - **Date**
    - **Index**
    - **Open**
    - **Close**
    - **High**
    - **Low**
    - **Volume**

how_to_run:
  steps:
    - Ensure **Python 3.10+** is installed
    - Clone this repository
    - Install dependencies using: `pip install -r requirements.txt`
    - Place **indexData.csv** in the project root directory
    - Run the app using: `python Interactive_Stock_Plot.py`

output:
  type: **Interactive Line Chart**
  tool: **Plotly**
  interactivity:
    - **Dropdown menu** to toggle indices
    - **Date range selector** for zooming
    - **Hover tooltips** showing date and price details
 screenshot:
 [![image](https://github.com/user-attachments/assets/0531084c-8f2b-4ef8-81ec-80d3ebd7329f)](https://github.com/vineeth-neeli7/Stock-Index-Dashboard/blob/main/Stock%20Dashboard%20Screenshot.jpg)


author:
  name: **Sai Vineeth Neeli**
  note: >
    This project was developed as part of an **assessment** to demonstrate real-world data visualization using **Python**.

