# factorial_calculator.py
# Exercise selected: Chapter 5 program 12
# Name of program: Factorial Calculator
# Description of program: this program will calculate n! where n is some
#   nonnegative integer input by the user.
# Ivan Boatwright
# February 18, 2016 (doomsday tomorrow)

# textwrap is used to wrap integers larger that 70 characters.
import textwrap

def main():
    # Variable definitions
    nObjectCount = 0    # Nonnegative number (the n for n!)
    nFactorial = 0      # Resulting permutation count (n!)
    
    # Call the user introduction module
    fluffy_intro()
    
    # Get the a non-negative number of Objects from the user
    nObjectCount = get_valid_inputs([['nonnegative integer',
                   'nonnegative number to calculate']])

    # Calculate the factorial of nObjectCount
    nFactorial = calc_factorial(nObjectCount)

    # Display calculated factorial to user
    display_results(nObjectCount, nFactorial)

    # End of main.
    return None


# Displays an introduction to the program and describes what it does.
def fluffy_intro():
    print('\nWelcome to the n! Factorial Calculator.')
    print('This program will calculate factorials of nonnegative integers.')
    print('It then displays the results for your viewing pleasure.\n')
    print('  *Note: Due to unforseen limitations and time constraints')
    print('         any n! > ~989 will cause an error.  Please enter any')
    print('         integer from 0 to 989.\n')
    return None


# get_valid_inputs requests input from the user then tests the input.
#   If invalid, it will alert the user and request the correct input.
# The parameter is a nested List of ordered pair Lists.
#   First value is the validation test and second is the user prompt.
def get_valid_inputs(requestsList):
    # local List to hold user inputs for return to calling module
    userInputs = []

    # Loop through each entry in requestList assigning each List pair
    #  to request.
    for request in requestsList:
        # untestedInput is a holding variable for testing user input validity.
        # First user prompt before testing loop
        untestedInput = int(prompt_user_for_input(request[1]))

        # If test_value returns True, Not converts it to False and the While
        #  Loop will not execute.
        # If test_value returns False, the While executes and the user is
        #  prompted to enter a valid value.
        while (not test_value(request[0], untestedInput)):

            print('!!! Error: {} is not a valid value.'.format(untestedInput))
            untestedInput = (prompt_user_for_input(request[1]))

        # The user input tested valid and is appended to the userInputs List.
        userInputs.append(untestedInput)
    # for loop terminates and userInputs are returned to calling Module
    return userInputs[0]  # Only one value to return in this program.


# prompt_user_for_item is passed a String to print to screen as part of a user
#   prompt.  Then it converts the user input into a real number and returns
#   it to the calling module.
def prompt_user_for_input(promptTerm):
    # promptTerm is a local variable to hold the value passed from the
    #   calling module.
    print('Please enter your {}.'.format(promptTerm))
    return int(input('  >> '))


# test_value uses the testCondition to select the proper test.
# It returns True or False to the calling Module.
def test_value(testCondition, testItem):
    # The If-Then-Else structure functions as a Switch for test selection.
    if testCondition == 'nonnegative integer':
        # Is testItem an Integer? If so, then is it also greater than
        #  or equal to 0?
        # Last minute addition of 989 upper limit.
        if isinstance(testItem, int) and 990 > testItem >= 0:
            return True
        else:
            return False
    else:
        return None


# calc_factorial uses recursion to repeatedly call itself while decrementing
#  nCount and multiplying fValue by nCount.  When nCount is less than or
#  equals 1 only fValue is returned.  nCount can equal 0 because 0! equals 1.
#  Recursion isn't very efficient in Python and has a limit to the number of
#  recursive calls that can be made.
def calc_factorial(nCount, fValue=1):
    if nCount <= 1:
        return fValue
    else:
        return calc_factorial(nCount - 1, fValue * nCount)


# display_results is passed values used in print statements to display
#  the results of the program to the user.
def display_results(nObjects, nFactorial):
    # There are 3 different printouts depending on the size of nFactorial.
    #  First is the whole number, second is in exponential form, and third
    #  is wrapped every 70 characters.
    if nObjects < 10:
        print('The factorial of {} is {}.'.format(nObjects, nFactorial))
    elif nObjects < 171:
        print('The factorial of {} is {:E}.'.format(nObjects, nFactorial))
    else:
        print('The factorial of {} is:'.format(nObjects))
        for line in textwrap.wrap(str(nFactorial),70):
            print(line)
    return None


# Call the main function to run the program.
main()