# The census dataset provided in a CSV file consists of the attributes
# age, sex, education, native-country, race, marital-status workclass,
# occupation, hours-per-week, income, capital-gain, and capital-loss.
# The CSV file census.csv contains exactly 30162 rows and each row
# contains exactly 12 comma-separated values in the form
# attribute=value. It can be downloaded for local testing at the link
# above, and is in the current directory on the Hackerrank server for
# use in your code.

# Use this data to find patterns which would help make important
# data-driven decisions.

# The support of the set of attributes is defined as the ratio of "total
# number of records with the given attributes" to "total number of
# records in the dataset".

# We can now derive some rules X => Y, where Xand Y describe the
# attributes set. The confidence of the rule is defined as the ratio of
# "total number of records with the given unique attributes in X and Y'
# to "total number of records with the given attributes in X", i.e., the
# ratio of 'Support of X u to "support of X".

# Rearrange the given set of rules X=>Yin descending order of
# confidence. It is guaranteed that no two rules have the same
# confidence. Also, the support of the attributes sets Xand Yin each
# of the rules is greater than or equal to 0.3.


import pandas as pd


def arrangingRules(rules):
    # Write your code here
    ratios_xy = []
    ratios_x = []
    support_xy = []
    support_x = []
    df = pd.read_csv("census.csv", header=None, names=['age', 'sex', 'education', 'native-country', 'race', 'marital-status',
    'workclass','occupation','hours-per-week', 'income','capital-gain', 'capital-loss'])
    for rule in rules:
        splitted = rule.split("=>")
        xy = splitted[0].replace('{', '')
        xy = xy.replace('}', '')
        xy = xy.split(',')
        x = splitted[1].replace('{', '')
        x = x.replace('}', '')
        support_xy.append(xy)
        support_x.append(x)
    
    for r in support_xy:
        attributes = []
        for i in r:
            attributes.append([i.split('=')[0], i])
        l = match(len(attributes), attributes, df)
        ratio = l/len(df)
        ratios_xy.append(ratio)

    for r in support_x:
        attribute = [r.split('=')[0], r]
        l = len(df[df[attribute[0]] == attribute[1]])
        ratio = l/len(df)
        ratios_x.append(ratio)
    
    final_ratios = []
    for i in range (len(ratios_x)):
        if (ratios_x[i] == 0):
            final_ratios.append(0)
        else:
            final_ratios.append(ratios_xy[i]/ratios_x[i])
    
    rules_ratios = []
    for i in range(len(rules)):
        rules_ratios.append([rules[i], final_ratios[i]])
    
    sorted_arr = sorted(rules_ratios ,key=lambda x: x[1])
    print(sorted_arr)
    final_arr = []
    for i in sorted_arr:
        final_arr.append(i[0])
    return final_arr
        
# really ugly function (hate having to do this but right now this is the only thing I can think of)
def match(n, attributes, df):
    l = 0
    if (n == 1):
        l = len(df[df[attributes[0][0]] == attributes[0][1]])
    elif(n == 2):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1])])
    elif(n == 3):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1])])
    elif(n == 4):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1]) & (df[attributes[3][0]] == attributes[3][1])])
    elif(n == 5):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1]) & (df[attributes[3][0]] == attributes[3][1]) & (df[attributes[4][0]] == attributes[4][1])])
    elif(n == 6):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1]) & (df[attributes[3][0]] == attributes[3][1]) & (df[attributes[4][0]] == attributes[4][1]) & (df[attributes[5][0]] == attributes[5][1])])
    elif(n == 7):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1]) & (df[attributes[3][0]] == attributes[3][1]) & (df[attributes[4][0]] == attributes[4][1]) & (df[attributes[5][0]] == attributes[5][1]) & (df[attributes[6][0]] == attributes[6][1])])
    elif (n == 8):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1]) & (df[attributes[3][0]] == attributes[3][1]) & (df[attributes[4][0]] == attributes[4][1]) & (df[attributes[5][0]] == attributes[5][1]) & (df[attributes[6][0]] == attributes[6][1]) & (df[attributes[7][0]] == attributes[7][1])])
    elif (n == 9):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1]) & (df[attributes[3][0]] == attributes[3][1]) & (df[attributes[4][0]] == attributes[4][1]) & (df[attributes[5][0]] == attributes[5][1]) & (df[attributes[6][0]] == attributes[6][1]) & (df[attributes[7][0]] == attributes[7][1]) & (df[attributes[8][0]] == attributes[8][1])])
    elif (n == 10):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1]) & (df[attributes[3][0]] == attributes[3][1]) & (df[attributes[4][0]] == attributes[4][1]) & (df[attributes[5][0]] == attributes[5][1]) & (df[attributes[6][0]] == attributes[6][1]) & (df[attributes[7][0]] == attributes[7][1]) & (df[attributes[8][0]] == attributes[8][1]) & (df[attributes[9][0]] == attributes[9][1])])
    elif (n == 11):
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1]) & (df[attributes[3][0]] == attributes[3][1]) & (df[attributes[4][0]] == attributes[4][1]) & (df[attributes[5][0]] == attributes[5][1]) & (df[attributes[6][0]] == attributes[6][1]) & (df[attributes[7][0]] == attributes[7][1]) & (df[attributes[8][0]] == attributes[8][1]) & (df[attributes[9][0]] == attributes[9][1]) & (df[attributes[10][0]] == attributes[10][1])])
    else:
        l = len(df[(df[attributes[0][0]] == attributes[0][1]) & (df[attributes[1][0]] == attributes[1][1]) & (df[attributes[2][0]] == attributes[2][1]) & (df[attributes[3][0]] == attributes[3][1]) & (df[attributes[4][0]] == attributes[4][1]) & (df[attributes[5][0]] == attributes[5][1]) & (df[attributes[6][0]] == attributes[6][1]) & (df[attributes[7][0]] == attributes[7][1]) & (df[attributes[8][0]] == attributes[8][1]) & (df[attributes[9][0]] == attributes[9][1]) & (df[attributes[10][0]] == attributes[10][1]) & (df[attributes[11][0]] == attributes[11][1])])
    return l