# -*- coding: utf-8 -*-
def question(question_number, present_c=0):
    for r in range(len(question_number)):
        # If you have reached the last column, print the result and jump out of recursion
        if present_c == len(question_number):
            for i in range(len(question_number)):
                print('. ' * question_number[i] + 'Q ' + '. ' * (len(question_number)-question_number[i]-1))
            input("More?")
            return
        # tag is a feasibility tag
        question_number[present_c] = r
        tag = True
        # Traverse the columns before the present column
        for c in range(present_c):
            # If there is no position on the line and the diagonal, set the tag to False
            if (question_number[c] == r) or ((r - question_number[c]) == present_c - c) or (-(r - question_number[c]) == present_c - c):
                tag = False
                # As long as there is an unsatisfied condition, it will jump out of the traversal
                break
        # If the conditions are met, then recursively call itself to perform the next column of filtering
        if tag:
            question(question_number, present_c + 1)
def solve():
    return question([''] * 8)
