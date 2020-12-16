# first question that is asked
question_1 = input('Does the compound have metals? (y/n): ')

# displays for different types of compounds after user has answered questions
ionic = 'Your compound is ionic. \n' \
        'Put -ide as your suffix. \n' \
        'No prefix'

covalent = 'Your compound is covalent. \n' \
           'Put -ide as your suffix. \n' \
           'Prefix is numerical for both elements'

hydrocarbon = 'Your compound is hydrocarbon. \n' \
              'Put -ane as your suffix. \n' \
              'Prefix is dependent on the number of carbon atoms'


# (RESOLVED) PROBLEM: When user inputs 'y' for question_1, it does not prompt them with ionic.
# Instead, it gives them question_2 before it gives them ionic.
# Resolved by moving question_2 down to the else statement

# if else statements for yes/no responses
if question_1 == 'y':
    print(ionic)

else:
    question_2 = input('Does the compound contain just carbon and hydrogen? (y/n): ')
    if question_2 == 'n':
        print(covalent)
    else:
        print(hydrocarbon)
