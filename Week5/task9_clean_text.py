"""
Task 9: Clean and transform text data using string methods
Run: python task9_clean_text.py
"""

import pandas as pd


def main():
    raw = pd.DataFrame(
        {
            "product_name": ["  10k Resistor  ", "CAPACITOR-100uF", "Ic 555 timer  ", "  usb-c Cable"],
            "description": [
                "High precision resistor. 1% tolerance",
                "Electrolytic capacitor, 100uF/25V",
                "Classic timer IC for oscillators",
                "fast charging cable - 1.5M length ",
            ],
        }
    )

    cleaned = raw.copy()
    cleaned["product_name"] = (
        cleaned["product_name"]
        .str.strip()  # trim spaces
        .str.lower()  # lowercase
        .str.replace(r"\s+", " ", regex=True)  # normalize whitespace
        .str.replace("-", " ")  # replace hyphens with space
    )

    # Create a SKU-like slug
    cleaned["sku_slug"] = cleaned["product_name"].str.replace(r"[^a-z0-9]+", "-", regex=True).str.strip("-")

    # Extract numeric value from description (e.g., capacity or length)
    cleaned["numeric_value"] = cleaned["description"].str.extract(r"(\d+\.?\d*)")

    # Split words into lists (tokenization)
    cleaned["words"] = cleaned["description"].str.lower().str.split()

    print("Original:")
    print(raw, "\n")

    print("Cleaned:")
    print(cleaned, "\n")


if __name__ == "__main__":
    main()

