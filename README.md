# AAPL-Stock-Analysis-2023
Analysis of Apple Inc.'s stock performance in 2023 using Python and Power BI.

## Table of Contents
- [Overview](#overview)
- [Data](#data)
- [Scripts](#scripts)
- [Power BI Dashboard](#power-bi-dashboard)
- [How to Use](#how-to-use)
- [Key Insights](#key-insights)
- [Future Work](#future-work)
- [Contact](#contact)

## Overview
This project demonstrates the analysis of Apple's stock performance throughout 2023. The analysis includes data extraction using Python, processing, and visualization using Power BI. The project is designed to showcase my ability to work with financial data and create insightful dashboards.

## Data
The dataset `AAPL_historic_data.csv` contains daily stock prices and volume traded for Apple Inc. from January 1, 2023, to August 1, 2023. This data was extracted using the Yahoo Finance API.

## Scripts
The `script.py` file contains the Python code used to fetch and preprocess the data. The key steps include:

- Fetching historical data using the yFinance library.
- Saving the data to a CSV file.
- Storing the data in a SQLite database for further analysis.

## Power BI Dashboard
The `Dashboard.pbix` file is the Power BI report that visualizes the data. The dashboard includes:

- A line chart showing the trend of Apple's closing prices over 2023.
- A bar chart illustrating the volume traded over the same period.
- Cards displaying the highest and lowest closing prices with their respective dates.
- A date slicer for interactive filtering.

## How to Use
1. **Python Script:**
   - Clone this repository.
   - Run `script.py` to fetch and save the data.

2. **Power BI Dashboard:**
   - Download and open the `Dashboard.pbix` file using Power BI Desktop.
   - Explore the visualizations and interact with the data using the slicer.

## Key Insights
- Apple's stock showed significant volatility during 2023.
- The highest closing price was on 14/12/2023, while the lowest was on 05/01/2023.
- Volume traded had several spikes, correlating with market events.

These insights can help investors understand market trends and make informed decisions.

