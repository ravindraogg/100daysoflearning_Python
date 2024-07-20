# 100DaysOfLearning_Python

Welcome to my 100 Days of Learning Python journey! In this repository, I'll document my progress and share what I've learned each day. Follow along and learn with me!

## Day 1: Introduction to Python

Today, I started my Python learning journey. Here's what I covered:

### Introduction to Python
- Learned about the history and significance of Python.
- Understood why Python is popular and widely used.

### Data Types
- **Integers**: Whole numbers, e.g., `5`, `-10`
- **Strings**: Sequence of characters, e.g., `"Hello, World!"`
- **Booleans**: Represents `True` or `False`
- **None**: Special data type to denote the absence of a value
- **Float**: Numbers with a decimal point, e.g., `3.14`, `-2.0`

### Variables
- Learned how to create variables and assign values to them.
- Understood the rules for naming variables.
- Practiced using variables in simple Python scripts.

## Day 2: Conditional Statements

Today, I focused on conditional statements and wrote some programs. Here's what I learned:

Conditional Statements
- Used if, else, and elif statements to make decisions in Python programs.
- Understood how to use comparison operators (<, >, ==, !=, <=, >=) in conditionals.
- Practiced writing conditional statements to control the flow of my programs.

### Example 1 
Grade sorting using if, elif, else.
- Condition_1 if marks has been awarded as 99 it gives output as A Grade.
- Condition_2 if marks has been awarded as 54 it gives output as F Grade.
- Condition_3 if marks has been awarded as 80 it gives output ad B Grade.

### Example 2 
The program checks the following conditions:
- If the age is between 20 and 60 (inclusive) and the gender is "M" (Male), the fee is 100.
- If the age is between 20 and 60 (inclusive) and the gender is "F" (Female), the fee is 200.
- If neither condition is met, the program prints "Not Applicable".

## Day 3: Terenary operation

### Topics Covered
1. Single Line If / Ternary Operation
2. Clever If Ternary Operation
3. Operators


1. Single Line If / Ternary Operation

The ternary operation in Python allows you to write a simple if-else statement in a single line.

### Syntax
<var> = <val1> if <condition> else <val2>

2. Clever If Ternary Operation

A clever way to use a ternary-like operation is by using tuple indexing. This is less common but can be useful in some cases.

### Syntax
<var> = (False_val, True_val)[<condition>]

## Day 4: Pactice Question

## Practice Questions

### Question 1
Write a program to input the user's first name and print its length.

### Question 2
Wite a program to find the occurance of '$' in an string. 

## Day 5: List & Tuples 

### Topics Covered
1. List
2. Tuples
3. Practice Questions

### Learning Objectives
- Understand and implement Python lists and tuples.

### List 
- A data structure in Python that is a mutable, or changeable, ordered sequence of elements.

### Tuple 
- A data structure in Python which is immutable, or unchangable, ordered sequence of element.

### Practice Question

- Question 1
  Adding movie list from user!!

        movie = []
        movie.append(input("Enter first Movie Name: "))
        movie.append(input("Enter Second Movie Name: "))
        movie.append(input("Enter Third Movie Name: "))
        print(movie)

- Question 2 
  1. Count the number of students with the "A" grade in the following tuple and store the tuple in a list and sort them from A to D:

         tuple = ("C","B","A","A","C","D","A")
         print(tuple.count("A"))
     
  3. Store the above tuple in a list and sort them from A to D

         list1 = list(tuple)
         list1.sort()
         print(list1)

## Day 6: Learning Dictionaries

Today, I learned about dictionaries in Python. Here is an example demonstrating the basics of creating, accessing, and updating a dictionary:

# Creating a dictionary
````PYTHON
menu = {
    "Name": "Ravindra",
    "Class": "BE 2nd Year",
    "DOB": "07/09/2005"
}
`````
### Printing the entire dictionary
print(menu)

### Accessing values using keys
print(menu.get("Name"))
print(menu.get("Name2"))  # This will return None since "Name2" is not a key in the dictionary

#$$ Updating the dictionary by adding a new key-value pair
menu.update({"Gender": "Male"})
print(menu)

# Stay tuned for more updates as I continue my learning journey!
