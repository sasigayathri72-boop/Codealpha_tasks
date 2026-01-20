def portfolio_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 258,
        "GOOG": 135,
        "MSFT": 310
    }

    portfolio = {}
    total_value = 0

    # Get number of stocks
    num_stocks = int(input("Enter the number of stocks: "))

    for i in range(num_stocks):
        stock = input(f"\nEnter stock symbol {i + 1}: ").upper()

        if stock not in stock_prices:
            print("Stock not available!")
            continue

        quantity = int(input(f"Enter quantity of {stock}: "))

        value = stock_prices[stock] * quantity
        portfolio[stock] = {
            "Quantity": quantity,
            "Price": stock_prices[stock],
            "Value": value
        }

        total_value += value

    # Display portfolio summary
    print("\n----- Portfolio Summary -----")
    for stock, details in portfolio.items():
        print(f"{stock} | Quantity: {details['Quantity']} | "
              f"Price: ${details['Price']} | Value: ${details['Value']}")

    print(f"\nTotal Portfolio Value: ${total_value}")

    # Optional: Save to file
    save = input("\nDo you want to save the result to a file? (yes/no): ").lower()

    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("Stock Portfolio Summary\n")
            file.write("-----------------------\n")
            for stock, details in portfolio.items():
                file.write(f"{stock}, {details['Quantity']}, "
                           f"{details['Price']}, {details['Value']}\n")
            file.write(f"\nTotal Value: ${total_value}")

        print("Portfolio saved to portfolio.txt")

# Run the program
portfolio_tracker()