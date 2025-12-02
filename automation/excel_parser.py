import pandas as pd
from automation.utils import log

def parse_excel(file_path):
    log("Parsing Excel file...")

    df = pd.read_excel(file_path)

    # Example: show rows with low stock (if part of inventory)
    if "Quantity" in df.columns:
        low_stock = df[df["Quantity"] < 10]
        log(f"Low stock items ({len(low_stock)} found):\n{low_stock}")

    log("Excel parsing completed.")
