# Taking input for the value of n
n = int(input("Enter a positive integer: "))

# Initialize the sum to 0
sum_even = 0

# Loop through all numbers from 1 to n
for num in range(1, n+1):
    # Check if the number is even
    if num % 2 == 0:
        sum_even += num

# Print the sum of even numbers
print("Sum of all even numbers between 1 and", n, "is:", sum_even)
