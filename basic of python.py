# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 12:48:06 2024

@author: Engga
"""
"""
Q1:Write a Python program that checks whether a given
number is prime or not. A prime number is a natural
number greater than 1 that has no positive divisors
other than 1 and itself.
"""
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Enter a number to check if it is prime: "))
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
    
#

"""Q2:Develop a Python program that generates two random
 numbers and asks the user to enter the product of these
 numbers. The program should then check if the user's
 answer is correct and display an appropriate message."""
 
 
import random

# Generate two random numbers
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# Ask the user to enter the product
print("What is the product of", num1, "and", num2, "?")
answer = int(input("Enter your answer: "))

# Check if the answer is correct
if answer == num1 * num2:
  print("Correct!")
else:
  print("Incorrect. The correct answer is", num1 * num2)

"""Q3:Create a Python script that prints the squares of
 all even or odd numbers within the range of 100 to 200.
 Choose either even or odd numbers and document your
 choice in the code."""
choice=(input("Enter odd or even:"))
choice             
for num in range(100, 201):
  if choice == 'even' and num % 2 == 0:
    square = num ** 2
    print(f"{num}^2 = {square}")
  elif choice == 'odd' and num % 2 != 0:
    square = num ** 2
    print(f"{num}^2 = {square}")
 
"""Q4:write a program to count the number of words in a given text."""


def count_words(text):
  """Counts the number of words in a given text.

  Args:
    text: The input text.

  Returns:
    A dictionary where keys are words and values are their counts.
  """
  words = text.lower().split()
  word_counts = {}
  for word in words:
    if word in word_counts:
      word_counts[word] += 1
    else:
      word_counts[word] = 1
  return word_counts

inp = input('STATEMENT:')
input_text = inp
word_counts = count_words(input_text)
for word, count in word_counts.items():
  print(f"'{word}': {count}")
 
"""Q5:Write a Python function called is_palindrome that takes
 a string as input and returns True if the string is a
 palindrome, and False otherwise. A palindrome is a word,
 phrase, number, or other sequence of characters that reads
 the same forward and backward, ignoring spaces, punctuation,
 and capitalization. """
 
def is_palindrome(s):
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
a=str(input("Enter string:"))
if(is_palindrome(a)==True):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
 
 
 
 
 
 
 
 
 
 