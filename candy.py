#Candy Challenge

'''
You go trick or treating with a friend and all but three of the houses that you visit are giving out candy. One house that you visit is giving out toothbrushes and two houses are giving out dollar bills. 

Task
Given the input of the total number of houses that you visited, what is the percentage chance that one random item pulled from your bag is a dollar bill? 

Input Format 
An integer (>=3) representing the total number of houses that you visited. 

Output Format
A percentage value rounded up to the nearest whole number.

Sample Input
4

Sample Output 
50
'''
dollar_bill = 2
total_house = 0

while (total_house < 3):
    total_house = int(input("How many houses did you visit?\n"))
    if (total_house < 3):
        print("Number of Houses visited must be under 3!\n")
    else:
        break

percent_chance_dollarB = round((dollar_bill/total_house) * 100)

print(percent_chance_dollarB,"%")
