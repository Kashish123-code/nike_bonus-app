from flask import Flask, render_template
import pandas as pd
import os
from pandas.errors import EmptyDataError

app = Flask(__name__)

@app.route("/")
def home():
    # Case 1: CSV file hi nahi hai
    if not os.path.exists("nike_products.csv"):
        return "nike_products.csv file not found. App is running correctly."

    try:
        # Case 2: CSV empty hai
        df = pd.read_csv("nike_products.csv")

        if df.empty:
            return "CSV file is empty, but Flask app is working correctly."

        # Case 3: CSV me data hai
        return render_template(
            "index.html",
            tables=[df.to_html(index=False)]
        )

    except EmptyDataError:
        # CSV bilkul empty (no headers)
        return "CSV file has no columns, but Flask app is running correctly."

    except Exception as e:
        # Any unexpected error
        return f"Unexpected error: {e}"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

