print("CURRENCY CONVERSION")
print("===========================")
#print({num:num for  num in range(1,5)})
price={'milk':20,'cookies':30,'tea':40}
dhm_inr=200
#for i in price.items():
#print(i)
new_price={item:value*dhm_inr for item, value in price.items()}
print(new_price)

