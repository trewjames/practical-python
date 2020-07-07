bill_thickness = 0.11 * 0.001  # Meters (0.11 mm)
sears_height = 442  # Height (meters)
num_bills = 1
days = 1

while (num_bills * bill_thickness) < sears_height:
    days += 1
    num_bills *= 2

print(days, end='\r')
