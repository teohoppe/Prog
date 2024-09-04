num_2 = int(input("Entar a number between 1 and 9: "))
num_1 = int(input("Enter another number between 1 and 9: "))
i = 1

print(" ", end="\t")
while i <= num_1:
    print(i, end="\t")
    i += 1
print()

n = 1
while n <= num_2:
    print(n, end='\t')

    k = 1
    while k <= num_1:
        print(n * k, end='\t')
        k += 1

    print()
    n += 1