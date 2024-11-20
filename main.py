import customtkinter as ctk
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def fetch_stock_data(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1d', interval='1m')
        if data.empty:
            print(f"No data available for ticker: {ticker}")
            return None
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def process_data(data):
    if data is None or data.empty:
        return None, None
    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()
    latest_data = data.iloc[-1]
    return latest_data, data

def update_stock_info():
    ticker = ticker_entry.get().strip().upper()
    if not ticker:
        current_price_label.configure(text="Please enter a valid ticker symbol.")
        open_price_label.configure(text="")
        high_price_label.configure(text="")
        low_price_label.configure(text="")
        volume_label.configure(text="")
        ma20_label.configure(text="")
        ma50_label.configure(text="")
        plot_data(None)
        return

    data = fetch_stock_data(ticker)
    if data is not None:
        latest_data, processed_data = process_data(data)
        if latest_data is not None:
            current_price_label.configure(text=f"Current Price: ${latest_data['Close']:.2f}")
            open_price_label.configure(text=f"Open Price: ${latest_data['Open']:.2f}")
            high_price_label.configure(text=f"High Price: ${latest_data['High']:.2f}")
            low_price_label.configure(text=f"Low Price: ${latest_data['Low']:.2f}")
            volume_label.configure(text=f"Volume: {latest_data['Volume']}")
            ma20_label.configure(text=f"20-Day MA: ${latest_data['MA20']:.2f}")
            ma50_label.configure(text=f"50-Day MA: ${latest_data['MA50']:.2f}")
            plot_data(processed_data)
        else:
            current_price_label.configure(text="No data available")
            open_price_label.configure(text="")
            high_price_label.configure(text="")
            low_price_label.configure(text="")
            volume_label.configure(text="")
            ma20_label.configure(text="")
            ma50_label.configure(text="")
            plot_data(None)
    else:
        current_price_label.configure(text="Error fetching data")
        open_price_label.configure(text="")
        high_price_label.configure(text="")
        low_price_label.configure(text="")
        volume_label.configure(text="")
        ma20_label.configure(text="")
        ma50_label.configure(text="")
        plot_data(None)

def plot_data(data):
    for widget in plot_frame.winfo_children():
        widget.destroy()
    if data is not None:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(data['Close'], label='Close Price', color='blue')
        ax.plot(data['MA20'], label='20-Day MA', color='green')
        ax.plot(data['MA50'], label='50-Day MA', color='red')
        ax.set_title(f'{ticker_entry.get().strip().upper()} Stock Price and Moving Averages')
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.legend()
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)
    else:
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.set_title('No Data Available')
        canvas = FigureCanvasTkAgg(fig, master=plot_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(side=ctk.TOP, fill=ctk.BOTH, expand=1)

def live_update():
    update_stock_info()
    root.after(5000, live_update)  # Schedule the next update in 5000 milliseconds (5 seconds)

# Initialize CustomTkinter
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Create the main window
root = ctk.CTk()
root.title("Real-Time Stock Market Screener")
root.geometry("1280x720")

# Create a main frame to hold the two sections
main_frame = ctk.CTkFrame(root)
main_frame.pack(fill=ctk.BOTH, expand=1)

# Create a frame for the stock details
details_frame = ctk.CTkFrame(main_frame)
details_frame.pack(side=ctk.LEFT, fill=ctk.Y, expand=0, padx=20, pady=20)

# Create and place the ticker entry
ticker_label = ctk.CTkLabel(details_frame, text="Enter Stock Ticker:")
ticker_label.pack(pady=5)

ticker_entry = ctk.CTkEntry(details_frame, placeholder_text="Enter Ticker Symbol (e.g., AAPL, 0700.HK)")
ticker_entry.pack(pady=5)

# Create and place the update button
update_button = ctk.CTkButton(details_frame, text="Update", command=update_stock_info)
update_button.pack(pady=10)

# Create and place the information labels
current_price_label = ctk.CTkLabel(details_frame, text="Current Price: $0.00")
current_price_label.pack(pady=5)

open_price_label = ctk.CTkLabel(details_frame, text="Open Price: $0.00")
open_price_label.pack(pady=5)

high_price_label = ctk.CTkLabel(details_frame, text="High Price: $0.00")
high_price_label.pack(pady=5)

low_price_label = ctk.CTkLabel(details_frame, text="Low Price: $0.00")
low_price_label.pack(pady=5)

volume_label = ctk.CTkLabel(details_frame, text="Volume: 0")
volume_label.pack(pady=5)

ma20_label = ctk.CTkLabel(details_frame, text="20-Day MA: $0.00")
ma20_label.pack(pady=5)

ma50_label = ctk.CTkLabel(details_frame, text="50-Day MA: $0.00")
ma50_label.pack(pady=5)

# Create a frame for the plot
plot_frame = ctk.CTkFrame(main_frame)
plot_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=1, padx=20, pady=20)

# Start the live update
live_update()
# Run the application
root.mainloop()