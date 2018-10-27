"""
Exercise 5
"""

EU = ["SPAIN", "FRANCE", "GERMANY"]

purchaseValue = float(input("Purchase value? "))
country = input("Where are you from? ").strip()

shipping = 0
if country.upper() == "PORTUGAL":
    if input("Are you from Azores or Madeira? [Y/N] ").strip().upper() == "Y":
        shipping = 5
elif country.upper() in EU and purchaseValue > 50:
    shipping = 15
else:
    shipping = 25

print("Purchase value: {}".format(purchaseValue))
print("Shipping: {}".format(shipping))
print("Purchase w/ shipping: {}".format(purchaseValue + shipping))
