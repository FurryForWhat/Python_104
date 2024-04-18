fuel_in_liters = int(input("Enter fuel "))    
distance_in_km = int(input("Enter killometers "))
fuel_to_km = fuel_in_liters  * 12.5         


print(str(fuel_in_liters) + ' liters'+' can go about '+str(fuel_to_km) +' km')
print(f"{fuel_in_liters} liters can go about {fuel_to_km} km")
