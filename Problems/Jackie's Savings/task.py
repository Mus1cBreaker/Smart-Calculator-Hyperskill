def final_deposit_amount(*interest, amount=1000):
    for n in interest:
        amount *= ((n / 100) + 1)
    return round(amount, 2)