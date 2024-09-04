# Inizilize variables
weight = 0
n = 0
ship_price = 0

# Get input from user
amount = int(input("Hur många paket har du? "))
# for i in range(amount):
#     weight += int(input("Hur mycket väger paketet? "))

# Calculate the price of the shipment
while n < amount:
    n += 1
    weight = float(input("Hur mycket väger paketet? "))

    if weight < 2:
        ship_price += weight * 30

    elif weight <= 6:
        ship_price += weight * 28

    elif weight <= 12:
        ship_price += weight * 25

    else:
        ship_price += weight * 23

# Print the price of the shipment
print(f"Det kostar {ship_price} att skicka paketet")
    


    