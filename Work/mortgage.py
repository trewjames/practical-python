# mortgage.py
#
# Exercise 1.7
principal = 500_000
rate = 0.05
payment = 2684.11
total = 0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    payment = 2684.11
    if months >= extra_payment_start_month and \
            months <= extra_payment_end_month:
        payment += extra_payment

    months += 1
    total += payment
    principal = principal * (1 + rate / 12) - payment

    if principal < 0:
        total += principal
        principal = 0

    print(f'{months:3d} {total:>10.2f} {principal:>10.2f}')


print("Total paid", round(total, 1))
print("Months", months)
