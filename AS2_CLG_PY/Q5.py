# calculate gratuity and total
subtotal=eval(input("Enter subtotal: "))
gratuity_rate=eval(input("Enter gratuity(%):"))
gratuity = subtotal*(gratuity_rate/100)
total=subtotal+gratuity
print(f"Gratuity is: {gratuity} and total is: {total}")
