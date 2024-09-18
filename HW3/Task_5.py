from forex_python.bitcoin import BtcConverter
from datetime import datetime


# While testing, I discovered that forex_python may have some bug, I checked in official documentation but stil not
# working (Error: BitCoin Rates Source Not Ready For Given Date).
def get_profit_or_loss(year, month, day, amount_paid):
    b = BtcConverter()

    # date object
    purchase_date = datetime(year, month, day)

    # I'm just retrieving Bitcoin price on specific date
    try:
        price_on_purchase_date = b.get_previous_price('USD', purchase_date)
    except Exception as e:
        print(f"Error while fetching on purchase date: {e}")
        return

    # Convert price to bitcoins based on purchase date
    bitcoins_bought = b.convert_to_btc_on(amount_paid, 'USD', purchase_date)

    # I'm retrieving current price
    try:
        latest_price = b.get_latest_price('USD')
    except Exception as e:
        print(f"Error fetching latest price: {e}")
        return

    # BTC -> $$
    current_value = b.convert_btc_to_cur_on(bitcoins_bought, 'USD', purchase_date)

    # Profit or loss
    profit_or_loss = (latest_price * bitcoins_bought) - amount_paid

    print(f"Amount Paid: ${amount_paid:.2f}")
    print(f"Bitcoin Price on Purchase Date: ${price_on_purchase_date:.2f}")
    print(f"Current Bitcoin Price: ${latest_price:.2f}")
    print(f"Bitcoins Bought: {bitcoins_bought:.8f} BTC")
    print(f"Current Value of Bitcoins: ${latest_price * bitcoins_bought:.2f}")
    print(f"Profit/Loss: ${profit_or_loss:.2f}")


if __name__ == "__main__":
    # Example usage
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))
    amount_paid = float(input("dollar: "))

    get_profit_or_loss(year, month, day, amount_paid)
