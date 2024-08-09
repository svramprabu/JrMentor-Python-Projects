price = 10000
has_good_credits = False

if has_good_credits:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"down payment: {down_payment}")