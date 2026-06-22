stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 320
}

total_investment = 0

num = int(input("How many stocks do you want to enter? "))

for i in range(num):
    stock = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock in stock_prices:
        value = stock_prices[stock] * quantity
        total_investment += value
    else:
        print("Stock not found!")

print("\nTotal Investment Value =", total_investment)