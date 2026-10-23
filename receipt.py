coffee_name = "Kofe"
coffee = 4.5

cake_name = "Cizkeyk"
cake = 6.0

water_name = "Su"
water = 1.0

total = coffee + cake + water
vat = total * 0.18
final_total = total + vat


print("-----KAFE-----")
print(coffee_name, coffee, "AZN")
print(cake_name, cake, "AZN")
print(water_name, water, "AZN")
print("----------------")
print("Cemi:", round(total, 2), "AZN")
print("EDV 18%:", round(vat, 2), "AZN")
print("Yekun:", round(final_total, 2), "AZN")

      
