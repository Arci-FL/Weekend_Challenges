#Paint

import math

canvs_brushs = 40.0
color = 5.0
tax = 0.1

num_of_col = int(input("Enter the number of colors to be bought: "))

#before tax
total_cost = canvs_brushs + (color * num_of_col)

#taxed amount
taxed = total_cost * tax

#after tax
proj_cost = total_cost + taxed
print(math.ceil(proj_cost))
