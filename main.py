#Open and Read the survey file
survey_file = open('survey-results.txt', 'r')

#Open and Read the number file
number_file = open('number-data.txt', 'r')

#Open and Read the age file
age_file = open('age-data.txt', 'r')


#Output Survey Data
yes_count = 0
no_count = 0
maybe_count = 0
for line in survey_file:
    if 'Yes' in line:
        yes_count+=1
    elif 'Maybe' in line:
        maybe_count+=1
    elif 'No' in line:
        no_count+=1
print("Yes: (" + str(yes_count) + "), No: (" + str(no_count) + "), Maybe: (" + str(maybe_count) + ")")


#Output Age Data
under_18 = 0
between_18_35 = 0
between_36_65 = 0
above_65 = 0
for age in age_file:
    if int(age) < 18:
        under_18 +=1
    elif int(age) >= 18 and int(age) <= 35:
        between_18_35 +=1
    elif int(age) >= 36 and int(age) <= 65:
        between_36_65 +=1
    else:
        above_65 +=1
print("Under 18 (" + str(under_18) + "), 18 to 35 (" + str(between_18_35) + "), 36 to 65 (" + str(between_36_65) + "), Above 65 (" + str(above_65) + ")")


#Output Number Data
even = 0
odd = 0
for data in number_file:
    if int(data) % 2 == 0:
        even+=1
    else:
        odd+=1
print("Even (" + str(even) + "), Odd (" + str(odd) + ")")