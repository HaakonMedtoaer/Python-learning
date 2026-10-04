itemnumber = "6514"
quantity = 3
price = 19.99
line_total = quantity * price
vat_rate = 0.25
vat = line_total * vat_rate
totalandvat = line_total + vat
print(f"Item number: {itemnumber}, Quantity: {quantity}, Price: {price:.2f}, Before VAT: {line_total:.2f} (vat: {vat:.2f}) Total: {totalandvat:.2f}")