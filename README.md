# Real-Time Stock Market Screener

## Overview
The Real-Time Stock Market Screener is a Python application that allows users to fetch and display real-time stock data, including current price, open price, high price, low price, volume, and moving averages (20-Day and 50-Day). The application uses the `yfinance` library to fetch stock data and `matplotlib` to plot the stock prices and moving averages. The user interface is built using `customtkinter`, providing a modern and visually appealing design.

## Features
- Fetch real-time stock data using the `yfinance` library.
- Display current price, open price, high price, low price, and volume.
- Calculate and display 20-Day and 50-Day moving averages.
- Plot the stock prices and moving averages using `matplotlib`.
- Update the stock information every 5 seconds.
- User-friendly interface built with `customtkinter`.

## Requirements
- Python 3.6 or higher
- `yfinance` library
- `pandas` library
- `matplotlib` library
- `customtkinter` library

## Requirements

To run this project, you need to have the following dependencies installed. You can install them using `pip`:

```sh
pip install -r requirements.txt
```

## The requirements.txt file includes:

- `pandas`
- `matplotlib`
- `customtkinter`
- `yfinance`

# How to Use
Clone the Repository

First, clone this repository to your local machine:
```sh
git clone https://github.com/onyxfuzzx/Live-Stock-Screener.git
```
```sh
cd live-stock-screener
```
Install Dependencies

Navigate to the project directory and install the required dependencies:
```sh
pip install -r requirements.txt
```
Run the Application

Execute the script to start the GUI application:

```sh
python main.py
```

- Enter a stock ticker symbol (e.g., AAPL, 0700.HK) in the "Enter Stock Ticker" field.

- Click the "Update" button to fetch and display the stock information.

- The stock information and plot will be updated every 5 seconds.



Contributing
Contributions are welcome! Please feel free to fork the repository and submit pull requests with any improvements or new features.

License
This project is licensed under the MIT License - see the LICENSE file for details.

