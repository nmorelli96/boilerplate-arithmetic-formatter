import re
def arithmetic_arranger(problems, answers=False):
    if type(problems) != list:
        return 'Error: Problems should be in a list.'
    if len(problems) > 5:
        return 'Error: Too many problems.'
    problemsLen = list()
    problemsRows = {'row1':'', 'row2':'', 'row3':'', 'row4':''}
    problemsResults = list()
    i = 0
    for operation in problems:
        terms = operation.split()
        #print('len:', len(terms))
        #print('operator check:', terms[1] != "+" and terms[1] != "-")
        #print('digits check', re.match(r"^[0-9]+$",terms[0]), re.match(r"^[0-9]+$",terms[2]))
        #print('4 digits chk', re.match(r"^[0-9][0-9]?[0-9]?[0-9]?$",terms[0]), re.match(r"^[0-9][0-9]?[0-9]?[0-9]?$",terms[2]))
#input checks
        if len(terms) != 3:
            return 'Error: The problem needs to include 2 integers and a + or - operator with a whitespace in the middle (1 + 2).'
        if terms[1] != "+" and terms[1] != "-":
            return "Error: Operator must be '+' or '-'."
        if re.match(r"^[0-9]+$",terms[0]) is None or re.match(r"^[0-9]+$",terms[2]) is None:
            return 'Error: Numbers must only contain digits.'
        if re.match(r"^[0-9][0-9]?[0-9]?[0-9]?$",terms[0]) is None or re.match(r"^[0-9][0-9]?[0-9]?[0-9]?$",terms[2]) is None:
            return 'Error: Numbers cannot be more than four digits.'
#formatting logic
        if len(terms[0]) < 2 and len(terms[2]) < 2:
            problemsLen.append(3)
        elif len(terms[0]) < 3 and len(terms[2]) < 3:
            problemsLen.append(4)
        elif len(terms[0]) < 4 and len(terms[2]) < 4:
            problemsLen.append(5)
        elif len(terms[0]) < 5 and len(terms[2]) < 5:
            problemsLen.append(6)
        whitespacesRow1 = problemsLen[i] - len(terms[0])
        whitespacesRow2 = problemsLen[i] - len(terms[2]) - 1 # - 1 because of the operator sign
        problemsRows['row1'] = problemsRows['row1'] + whitespacesRow1 * " " + terms[0] + "    "
        problemsRows['row2'] = problemsRows['row2'] + terms[1] + whitespacesRow2 * " " + terms[2] + "    "
        problemsRows['row3'] = problemsRows['row3'] + "-" * problemsLen[i] + "    "
        if answers == True:
            problemsResults.append(str(eval(problems[i])))
            whitespacesRow4 = problemsLen[i] - len(problemsResults[i])
            problemsRows['row4'] = problemsRows['row4'] + whitespacesRow4 * " " + problemsResults[i] + "    "
        i += 1
#final format
    if answers == False:
        return problemsRows['row1'].rstrip() + "\n" + problemsRows['row2'].rstrip() + "\n" + problemsRows['row3'].rstrip()
    elif answers == True:
        return problemsRows['row1'].rstrip() + "\n" + problemsRows['row2'].rstrip() + "\n"+problemsRows['row3'].rstrip() + "\n" + problemsRows['row4'].rstrip()
