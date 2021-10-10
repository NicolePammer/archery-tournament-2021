

"""
BOW TOURNAMENT

I had a bow tournament with the rating "double hunter according to WA".
In this program the archer can enter the shots. The score of the shots is added up.
At the end the data is stored as a table in a CSV-File (comma separated).
"""

# IMPORT MODULES / LIBRARIES
import numpy as np
import pandas as pd
from datetime import date

# CREATE DATAFRAME WITH COLUMN HEADERS ONLY
df = pd.DataFrame(columns = "target arrow_01 arrow_02 value total".split())

# USER INPUT: WHAT'S YOUR NAME?
archer = input("Enter your name: ").replace(" ", "_").casefold() # casefold equals lower but is more aggressive

# USER INPUT: WHICH CLASS DO YOU SHOOT?
while True:
    bowclass = input ("\nChose your bowclass\
        \nLB ... long bow\
        \nIB ... intuitive bow\
        \nBB ... bare bow\
        \nCO ... compound bow\
        \nYour bowclass ( LB | IB | BB | CO): ").upper()
    if bowclass == "LB" or "IB" or "BB" or "CO": 
        break

# CREATING THE CSV-FILE NAME
today = date.today()
filename = str(today.year)[-2:] + str(today.month) + str(today.day) + "_" + archer + "_" + bowclass + ".csv"

# USER INPUT: HOW MANY TARGETS DOES YOUR COURSE HAVE?
number_of_targets = int(input("\nEnter number of targets: "))
target_possibilities = np.arange(1,number_of_targets+1)

# GIVEN: POINT POSSIBILITES ("TYPE: DOPPELHUNTER NACH WA (GER)")
point_possibilities = "11 10 8 5 0 M".split()

# INITAL VALUES
value = 0
total = 0
t = 1  #target
arrow_01 = 'M' # M ... miss (zero points)
arrow_02 = 'M' 
total_max = (11 * 2) * number_of_targets


#while True:
#     target = int(input("Enter target number: "))
#     if target in target_possibilities:
#         break
#     else:
#         print("Chosen target number not possible. Enter again.")



# ENTER THE SHOTS
while t in target_possibilities:
    while True:
        arrow_01 = input("\nTaget %s / Arrow 1: " %t)
        if arrow_01 in point_possibilities:
            break
        elif arrow_01 == "/back":
            t -= 1
        else:
            print("Chosen value not possible. Enter again.")

    while True:
        arrow_02 = input("Target %s / Arrow 2: " %t)
        if arrow_02 in point_possibilities:
            break
        elif arrow_02 == "/back":
            t -= 1
        else:
            print("Chosen value not possible. Enter again.")


    # INTERPRET SHOTS AS VALUES
    int_arrow_01 = 0 if arrow_01 == 'M' else int(arrow_01)
    int_arrow_02 = 0 if arrow_02 == 'M' else int(arrow_02)
    
    # POINTS REACHED AT THIS TARGET
    value = int_arrow_01 + int_arrow_02
    
    # POINTS REACHED IN TOTAL
    if t == 1:
        total = value # for the first line
    else:
        total = value + df.loc[t-1]["total"] # points reached at this target + total reached before

    # ADD THE NEW DATA TO THE DATAFRAME
    df_t = df.T # transpose
    df_t[t] = [t, int_arrow_01, int_arrow_02, value, total] # add a new line to the transposed dataframe
    df = df_t.T # tranpose back to original dataframe

    # PRINT THE CURRENT DATAFRAME
    print(df)

    # NEXT TARGET NUMBER
    t += 1
            
# REACHED PERCENTAGE
percent = float(total) / float(total_max)
#print("\n{} = {} / {}".format(percent, total, total_max))

# PRINT INFORMATION FOR ARCHER
print("\nYou reached a total of {} points! This is {:.2%} of the maximum achievable score.".format(total, percent))


# SAFE THE DATAFRAME TO A CSV-FILE
df.set_index("target", inplace = True)
df.to_csv(filename, sep=",")
print("\nScore-Board got saved into %s" %filename)
