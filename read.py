item_cost = float(input("Enter buy cost"))
sell_price = float(input("Enter price to sell: "))
item_quantity = float(input("Enter Amount: "))

buy_total = item_cost * item_quantity
sell_total = sell_price * item_quantity
print("Total buy price is: " + str(buy_total) + " total sell total is: "+str(sell_total))
tax = sell_total * 0.01
total_tax = sell_total - tax
print("Total after tax: " + str(total_tax))
print(sell_total, total_tax)
total_Profit = sell_total - total_tax
print("Total profit: " + str(total_Profit))

print("Calculating: " + str(100 * 100))
# item_price = item_cost * item_quanity
# item_tax = sell_price * 0.01
# print("Item tax cost: " +str(item_tax))
# final_price = item_price - item_tax
# print("total after tax: " +str(final_price))
# profit = item_price


