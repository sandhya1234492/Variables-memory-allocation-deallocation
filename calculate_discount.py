def calculate_discount(amount):
	if amount >= 5000:
		discount_rate = 0.20
	elif amount >= 3000:
		discount_rate = 0.10
	elif amount < 300:
		discount_rate = 0.05
	else:
		discount_rate = 0

	discount_amount = round(amount * discount_rate, 2)
	final_amount = round(amount - discount_amount, 2)

	return {
		"Discount amount": discount_amount,
		"Final payable amount": final_amount,
	}


purchase_amount = float(input("Enter the purchase amount: "))
result = calculate_discount(purchase_amount)

for label, value in result.items():
	print(f"{label}: {value:.2f}")