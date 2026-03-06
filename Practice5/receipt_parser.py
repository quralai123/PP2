import re
import json
with open("raw.txt", encoding="utf-8") as f:
    text = f.read()

#1 Extract all prices from the receipt
prices = re.findall(r"\d{1,3}(?: \d{3})*,\d{2}", text)
prices_numeric = [float(p.replace(" ", "").replace(",", ".")) for p in prices]

#2 Find all product names
product_lines = re.findall(r"\d+\.\n(.+?)\n\d+,\d+ x", text, re.DOTALL)
products = [p.replace("\n", " ").strip() for p in product_lines]

#3 Calculate total amount
total_amount_match = re.search(r"ИТОГО:\s*(\d{1,3}(?: \d{3})*,\d{2})", text)
total_amount = float(total_amount_match.group(1).replace(" ", "").replace(",", ".")) if total_amount_match else None

#4 Extract date and time information
datetime_match = re.search(r"Время:\s*([\d\.]+ \d{2}:\d{2}:\d{2})", text)
datetime_info = datetime_match.group(1) if datetime_match else None

#5 Find payment method
payment_match = re.search(r"Банковская карта:\s*([\d \.,]+)", text)
payment_amount = float(payment_match.group(1).replace(" ", "").replace(",", ".")) if payment_match else None

#6 Create a structured output (JSON or formatted text)
receipt_data = {
    "products": [{"name": p, "price": prices_numeric[i]} for i, p in enumerate(products)],
    "total_amount": total_amount,
    "payment_amount": payment_amount,
    "date_time": datetime_info,
}

print(json.dumps(receipt_data, ensure_ascii=False, indent=4))
