#!/usr/bin/python3
import sys
import math

def calculate_statistics(numbers):
    if not numbers:
        print("Error: No numbers provided.")
        return
num_count = len(numbers)
    sum_numbers = sum(numbers)
    mean = sum_numbers / num_count

squared_diff_sum = sum((num - mean) ** 2 for num in numbers)
    variance = squared_diff_sum / num_count
    std_deviation = math.sqrt(variance)
sorted_numbers = sorted(numbers)
if num_count % 2 == 0:
        median = (sorted_numbers[num_count // 2 - 1] + sorted_numbers[num_count // 2]) / 2
    else:
        median = sorted_numbers[num_count // 2]
print(f"Count: {num_count}")
    print(f"Sum: {sum_numbers}")
    print(f"Mean: {mean}")
    print(f"Variance: {variance}")
    print(f"Standard Deviation: {std_deviation}")
    print(f"Median: {median}")

def main():

try:
    numbers = [float(num) for num in sys.stdin.read().strip().split()]
        calculate_statistics(numbers)
    except ValueError:
	print("Error: Invalid input. Please provide a space-separated list of numbers.")

if __name__ == "__main__":
    main()




