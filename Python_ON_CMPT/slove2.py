import math

# Read 3 floating-point numbers
a, b, c = map(float, input().split())

# Calculate the discriminant
delta = b**2 - 4*a*c

try:
    # Check if the discriminant is non-negative
    if delta >= 0:
        # Calculate the roots
        root1 = (-b + math.sqrt(delta)) / (2*a)
        root2 = (-b - math.sqrt(delta)) / (2*a)

        # Print the roots in the required format
        
        print(f"R1 = {root1:.5f}")
        print(f"R2 = {root2:.5f}")

    else:
        # Print message for impossible calculation
        print("Impossivel calcular")

except Exception as e:
    # Print an error message if any exception occurs
    print("Impossivel calcular")
