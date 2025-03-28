#Ticket Challenge

'''
Ticket Office

You are analyzing sales data from a ticket office. 
The ticket for an adult is $20, while the ticket for a child under 18 is $5.
The data you are given is in a dictionary format, where the keys are the sold ticket numbers, and the values are the customer ages.
For example, "123-08": 24 means that the ticket was bought a 24 year old.
Your goal is to calculate how much more money the office would make if it would change the ticket discount age to the given input.
So, your program needs to take an integer as input and output the percentage of revenue growth, if the discount was given to people under that age.

For example, if the office made $15000 with the original discount age, and would make $18000 with 14 as the discount age, then the growth would be ((18000-15000)/15000)*100 = 20%

Test data
data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}
'''



data = {
    "100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40
}

discount_age = 18
new_discount_age = int(input("WHAT IS THE NEW DISCOUNT AGE?\n"))

def revenue_calc(data, disc_age):
    count_adult = 0
    count_child = 0
    for i in data.values():
        if (i >= disc_age):
            count_adult += 1
        else:
            count_child += 1

    rev_adult = count_adult * 20
    rev_child = count_child * 5

    total_rev = rev_adult + rev_child

    return total_rev

current_rev = revenue_calc(data, discount_age)
new_rev = revenue_calc(data, new_discount_age)

rev_percent_increase = ((new_rev - current_rev)/ current_rev) * 100

print(round(rev_percent_increase),"%")
