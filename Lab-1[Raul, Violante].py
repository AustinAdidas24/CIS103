# Lab 1: Getting Started with Python
# Cis 103: Introduction to Programming
# Instructor: Md.Ali
# Student Name: Raul Violante
# Date: 09/04/2024
# Description:
# This script prints a greeting message
print("Hello, Welcome to CIS 103!")

# Lab 1: Getting Started with Python
# Cis 103: Introduction to Programming
# Instructor: Md.Ali
# Student Name: Raul Violante
# Date: 09/04/2024
# Description:
# This script prints a personalized greeting message
# and demonstrates the use of variables and basic data types.
# ------------------------------------------------------------
# Get the user's name(string) and age (integer)
name =input("Enter Your Name: ")
age =input("Enter Your Age: ")
# Calculate the year the user was born
current_year = 2024
birth_year = current_year - int(age)
#print a personalized greeting message
print(f"Hello,{name}! You were born in {birth_year}.")
