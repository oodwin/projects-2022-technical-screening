"""
Inside conditions.json, you will see a subset of UNSW courses mapped to their 
corresponding text conditions. We have slightly modified the text conditions
to make them simpler compared to their original versions.

Your task is to complete the is_unlocked function which helps students determine 
if their course can be taken or not. 

We will run our hidden tests on your submission and look at your success rate.
We will only test for courses inside conditions.json. We will also look over the 
code by eye.

NOTE: We do not expect you to come up with a perfect solution. We are more interested
in how you would approach a problem like this.
"""
from ast import operator
import json
import re

courseCodes = ["comp", "dpst", "elec", "math", "mtrn"]
operators = ["and", "or", "(", ")"]

# NOTE: DO NOT EDIT conditions.json
with open("./conditions.json") as f:
    CONDITIONS = json.load(f)
    f.close()

def is_unlocked(courses_list, target_course):
    """Given a list of course codes a student has taken, return true if the target_course 
    can be unlocked by them.
    
    You do not have to do any error checking on the inputs and can assume that
    the target_course always exists inside conditions.json

    You can assume all courses are worth 6 units of credit
    """
    
    # TODO: COMPLETE THIS FUNCTION!!!
    if not courses_list:
        return target_course == "COMP1511"
        
    elif target_course in courses_list:
        print("You have already taken {target_course}!")
        return
    array = normalise(CONDITIONS[target_course]).split()
    for i in array:
        if (not isCourseCode(i)) and i not in operators:
            return
        elif isCourseCode(i):
            if done(i.upper(), courses_list):
                array[array.index(i)] = "True"
            else:
                array[array.index(i)] = "False"
    #print(array)
    #print("{}: {}".format(target_course, normalise(CONDITIONS[target_course])))
    #print(eval(" ".join(array)))
    return eval(" ".join(array))

def normalise(conditions):
    # Remove irregular spacing
    conditions = " ".join(conditions.split())
    # Remove punctuation
    conditions = conditions.strip(".")
    # remove prerequsite word and variants
    conditions = re.sub(r'^.*?: ', '', conditions)
    # add spacing around ( and )
    conditions = conditions.replace("(", "( ")
    conditions = conditions.replace(")", " )")
    # Uncapitalise everything
    conditions = conditions.lower()
    return conditions

def done(course, courses_list):
    return course in courses_list

def isCourseCode(code):
    return len(code) == 8 and code[0:4] in courseCodes and code[4:8].isdigit()

# Empty
# Irregular spacing, fullstops, capitalisation, prerequisite prefix, 
# logical operators
# Bracketing
# Non COMP courses
# X UOC in Level X COMP courses
# 
#is_unlocked(["COMP1511"], "COMP1521")