# Task 1

def d_to_b(n):
    if n <= 1:
        return str(n)
    else:
        return d_to_b(n // 2) + str(n % 2)

output = int(input("Enter a decimal number: "))
result = d_to_b(output)
print("Decimal to binary conversion is:",result)


