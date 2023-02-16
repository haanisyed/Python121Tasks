'''
CISC-121 2023W
Name: Haani Syed
Student Number: 20331181
Email: 21ahs7@queensu.ca
Date: 2023-02-01
I confirm that this assignment solution is my own work and conforms to Queen’s standards of Academic Integrity
'''
from functions import all_odd_or_even #import statement for my function.
def main(): #main function/main program
    '''
    description: this is the main function/program.
    parameters: none. Call to all odd/even function in functions.py is made.
    :return: no return in the main function. But there are some returns in all odd/even function.
    '''
    user_response = input('Would you like to participate in the activity (yes or no): ') #lets user respond with yes or no.
    list_numbers = [] #empty list initialized
    if user_response == 'yes': #if the user's response is yes
        possible_input = True #setting flag called "possible_input" to True. Will assist in "exiting the program parts."
        while possible_input == True: #while the flag is True
            amount = int(input('Enter a positive integer to add to this function: ')) #input statement for the user to end
            try: #try/except to ensure that the program functions properly.
                list_numbers.append(amount)
                user_response = input('Would you like to add another integer (yes or no): ')
                if user_response != 'yes':
                    possible_input = False #ends the while loop.
            except:
                print('This is an invalid input unfortunately.')
                possible_input = False
        the_result = all_odd_or_even(*list_numbers) #variable saving the all odd/even function's return
        if the_result: #if statement for when integers entered properly
            print('The positive integers entered and mentioned are all even or all odd')
        else: #if positive integers were not entered.
            print('The positive integers entered and mentioned are NOT all even or all odd')
    else:
        print('The program will be exiting since the requirement was not fulfilled.') #exits the program

main() #call to main
