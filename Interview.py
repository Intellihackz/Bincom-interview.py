import re
from collections import Counter
import psycopg2
from random import randint
import math


# Function to convert binary to decimal
def binary_to_decimal(binary_str):
    return int(binary_str, 2)


# Function to calculate the mean color
def calculate_mean_color(colors):
    total_colors = len(colors)
    total_sum = sum(colors.values())
    mean_color = total_sum / total_colors
    return mean_color


# Function to calculate the median color
def calculate_median_color(colors):
    sorted_colors = sorted(colors.values())
    middle_index = len(sorted_colors) // 2


    if len(sorted_colors) % 2 == 0:
        median_color = (sorted_colors[middle_index - 1] + sorted_colors[middle_index]) / 2
    else:
        median_color = sorted_colors[middle_index]


    return median_color


# Function to calculate the variance of colors
def calculate_variance(colors):
    mean_color = calculate_mean_color(colors)
    variance = sum((value - mean_color) ** 2 for value in colors.values()) / len(colors)
    return variance


# Function to calculate the probability of choosing red color
def calculate_red_probability(colors):
    total_colors = sum(colors.values())
    red_count = colors.get("red", 0)
    red_probability = red_count / total_colors
    return red_probability


# Function to save colors and their frequencies to PostgreSQL database
def save_to_database(colors):
    conn = psycopg2.connect("dbname=your_db_name user=your_db_user password=your_db_password")
    cur = conn.cursor()


    for color, frequency in colors.items():
        cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, frequency))


    conn.commit()
    cur.close()
    conn.close()


# Function for recursive searching algorithm
def recursive_search(lst, target, index=0):
    if index == len(lst):
        return -1
    if lst[index] == target:
        return index
    return recursive_search(lst, target, index + 1)


# Function to sum the first 50 Fibonacci sequence
def sum_fibonacci(n):
    a, b = 0, 1
    total_sum = 0


    for _ in range(n):
        total_sum += a
        a, b = b, a + b


    return total_sum


# Specify the path to your local HTML file
html_file_path = "path/to/your/file.html"


# Read HTML content from the file
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()


# Extract colors from the HTML table
color_pattern = re.compile(r'\b\w+\b', re.IGNORECASE)
colors_list = color_pattern.findall(html_content)


# Count the frequency of each color
colors_frequency = Counter(colors_list)


# Answering the questions
mean_color = calculate_mean_color(colors_frequency)
median_color = calculate_median_color(colors_frequency)
variance = calculate_variance(colors_frequency)
red_probability = calculate_red_probability(colors_frequency)


# Saving to PostgreSQL database
# Uncomment the line below and provide your PostgreSQL database details
# save_to_database(colors_frequency)


# Generating random 4-digit binary number and converting to decimal
random_binary_number = ''.join(str(randint(0, 1)) for _ in range(4))
random_decimal_number = binary_to_decimal(random_binary_number)


# Summing the first 50 Fibonacci sequence
fibonacci_sum = sum_fibonacci(50)


# Displaying the results
print(f"Mean Color: {mean_color}")
print(f"Most Worn Color: {colors_frequency.most_common(1)[0][0]}")
print(f"Median Color: {median_color}")
print(f"Variance: {variance}")
print(f"Probability of choosing red color: {red_probability}")
print(f"Random 4-digit Binary Number: {random_binary_number}")
print(f"Converted to Decimal: {random_decimal_number}")
print(f"Sum of the first 50 Fibonacci sequence: {fibonacci_sum}")