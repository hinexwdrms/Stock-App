from flask import Blueprint, render_template, request
import yfinance as yf

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def home():
    stock_data = None
    error = None

    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            stock_data = {
                "name": info.get("longName", "N/A"),
                "symbol": symbol,
                "price": info.get("regularMarketPrice", "N/A"),
                "sector": info.get("sector", "N/A"),
                "market_cap": info.get("marketCap", "N/A"),
            }
        except Exception as e:
            error = f"Could not fetch data for '{symbol}'. Please try again."

    return render_template("home.html", stock=stock_data, error=error)