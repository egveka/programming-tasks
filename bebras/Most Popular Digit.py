# A statistics team ask group of students to each provide a random 3 digit number.
# Task
# Write a program that outputs the most popular digit used by all of the students.
###############
# Input format
# An integer n representing the number of students, followed by n rows of 3 digit numbers.
###############
# Output format
# An integer representing the most popular digit used by the students.

n = int(input())
counters = [0,0,0,0,0,0,0,0,0,0]

for i in range(n):
    number = input()
    for x in number:
        counters[int(x)]+=1

print(counters.index(max(counters)))