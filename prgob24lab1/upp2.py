# Ask user for weight of package
weight = float(input("Hur mycket väger paketet?"))

# Calculate the price of the shipment
if weight < 2:
    ship_price = weight * 30
    print(f"Det kostar {ship_price} att skicka paketet")

elif weight <= 6:
    ship_price = weight * 28
    print(f"Det kostar {ship_price} att skicka paketet")

elif weight <= 12:
    ship_price = weight * 25
    print(f"Det kostar {ship_price} att skicka paketet")

else:
    ship_price = weight * 23
    print(f"Det kostar {ship_price} att skicka paketet")