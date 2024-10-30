my_sum = 0
for number in range(1, 101):
    if number % 2 == 0:
        my_sum += number

print(f"Sum of even numbers from 1 to 100 is: {my_sum}")