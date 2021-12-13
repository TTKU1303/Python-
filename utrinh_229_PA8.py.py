#-------------------------------------------------------------------------------
# Name: Uyen Trinh
# Assignment 8
# Due Date: 11/16/2021
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines set forth by professor and class syllabus.
#-------------------------------------------------------------------------------
# References: (list resources used - remember, assignments are individual effort!)
#-------------------------------------------------------------------------------
# Comments and assumptions: A note to the grader as to any problems or
# uncompleted aspects of the assignment, as well as any assumptions about the
# meaning of the specification.
#-------------------------------------------------------------------------------
# NOTE: width of source code should be <=80 characters to be readable on-screen.
#2345678901234567890123456789012345678901234567890123456789012345678901234567890
# 10 20 30 40 50 60 70 80
#-------------------------------------------------------------------------------

#
def read_csv(file):
    with open(file, 'r') as file:

    result = []

    for line in file.readlines():

        line = line.strip("\n")  # removes \n at the end of line if any

        row = line.split(",") # split by ","

        result.append(row) # add row in the result string

        return result


def locateEmergency(hospFile, polFile):


    hosp = read_csv(hospFile)

    pol = read_csv(polFile)

    zip = []

    hosp_zip = []

    pol_zip = []

    for i in hosp[1:]:

        x = hosp[i][7]

        zip.append(x)  # putting all zip codes into a list

        hosp_zip.append(x)

    for i in pol[1:]:

        y = pol[i][2]

        zip.append(y)

        pol_zip.append(y)

dictionary = {}

    for i in zip:

        key = i

        value = []

        if (key in hosp_zip):  # Enter only if the zip is in hosp zip codes(this increases efficiency)

            for j in hosp:

                if hosp[j][7] == key:

# Appends the required fields if zip matches(you can add any other fields too if required)

                    value.append([hosp[j][0], hosp[j][1], hosp[j][3], hosp[j][4], hosp[j][8]])

        if (key in pol_zip):  # Enter only if the zip is in pol zip codes(this increases efficiency)

            for j in pol:

                if pol[j][2] == key:

# Appends the required fields if zip matches(you can add any other fields too if required)

                    value.append(["Police Station", hosp[j][0], hosp[j][1], hosp[j][3]])

                    dictionary[key] = value

                    return dictionary
