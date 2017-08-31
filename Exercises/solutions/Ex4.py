"""
Exercise 4
"""

DISCOUNT_OVER_50 = 0.1
DISCOUNT_OVER_25 = 0.05

#purchaseValue = float(input("Purchase value?"))
purchaseValue = 110.1

print("Purchase value:", purchaseValue)

discount = 0
if purchaseValue > 50:
    discount = DISCOUNT_OVER_50
elif purchaseValue > 25:
    discount = DISCOUNT_OVER_25

discountValue = purchaseValue * discount
print("Discount ({:.1f}%): {}".format(discount * 100, discountValue))
print("Purchase w/ discount:", purchaseValue - discount)
