bf = 0 # Bränsleförbrukning
km = float(input("Hur många kilometer har du kört?"))
liter = float(input("Hur många liter bensin har du förbrukat?"))

bf = round(100 * liter / km, 3)
print(f"Din bränsleförbrukning är {bf} l/100 km")