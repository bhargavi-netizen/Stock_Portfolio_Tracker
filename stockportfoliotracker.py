stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 3300
}

portfolio = {}

n = int(input("How many stocks do you want to enter? "))

for i in range(n):
    name = input("Enter stock name: ").upper()
    qty = int(input("Enter quantity: "))
    portfolio[name] = qty

total = 0

for stock, qty in portfolio.items():
    if stock in stock_prices:
        total += stock_prices[stock] * qty
    else:
        print(f"{stock} not found in price list")

print("Total Investment Value:", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: {total}")