# Generate a list of numbers from 1 to 10.
numbers=[n for n in range(1,11)]
print(numbers)
# Generate a list of even numbers from 1 to 20.
evenumbers=[a for a in range(1,21) if a%2==0]
print(evenumbers)
# Generate a list of squares of numbers from 1 to 10.
oddnumbers=[a**2 for a in range(1,11) ]
print(oddnumbers)
# Generate a list of cubes of numbers from 1 to 10.
cubenumbers=[a**3 for a in range(1,21)]
print(cubenumbers)
# Extract all vowels from a given string "hello world".
stri="hello world"
vowel=[a for a in stri if a in 'aeiou']
print(vowel)
# Extract all consonants from "python".
consontants=[a for a in stri if a not in 'aeiou']
print(consontants)

# Create a list of characters in "datascience".
charac=[a for a in "datascience"]
print(charac)


# Get ASCII values of characters in "ABCxyz".

# Generate a list of numbers divisible by 3 between 1–30.
divisib3=[a for a in range(1,31) if a%3==0]
print(divisib3)
# Generate a list of numbers divisible by both 3 and 5 (1–50).

# Generate a list of first letters of words in ["apple", "banana", "cherry"].

# Generate a list of last letters of words in ["python", "java", "golang"].

# Given [1, 2, 3, 4], generate [2, 4, 6, 8].

# Reverse each word in a list ["cat", "dog", "bird"]