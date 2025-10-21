#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

def get_terms(terms):
  print("Input number of terms: ")
  terms = int(input())
  while terms <= 0:
    print("Please enter a positive integer.")
    terms = int(input())
  return terms

def generate_numbers():
  terms = 0
  num = get_terms(terms)
  first = 0
  second = 1
  third = 0
  result = ""
  for x in range(num):
    third = first + second
    result = result + "\n" + str(third)
    first = second
    second = third
    third = 0
  return(result)

def print_sequence():
  sequence = generate_numbers()
  print("\nYour Fibonacci Sequence:")
  print(sequence)





print_sequence()
