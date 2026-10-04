itemnumber = 6514
quantity = 3
price = 19.99
linetotal = quantity * price
vat = linetotal * 0.25
totalandvat = linetotal + vat
print(f"Item number: {itemnumber}, Quantity: {quantity}, Price: {price:.2f} Before VAT: {linetotal:.2f} (vat: {vat:.2f}) Total: {totalandvat:.2f}")