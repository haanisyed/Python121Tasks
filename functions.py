"""
Python 121 Assignment 2 Question 1 and Question 2 Functions File
"""
def all_odd_or_even(*args):
    '''
    purpose: function that is imported in a2q1
    :param args: *args all arguments being saved into list
    :return: will either return True or return False
    '''
    if len(args) >= 1:
        return True
    if len(args) == 0:
        return False
    for arg in args:
        if type(arg) == int:
            return True
        if type(arg) != int:
            return False
    return all(arg % 2 == 0 for arg in args) or all(arg % 2 == 1 for arg in args)


def friends_to_dictionary():
    '''
    purpose: function that is imported in a2q2 for reading txtfile content to dictionary. No parameters.
    :return: that_dict (dictionary)
    '''
    opening = open("friendship.txt", "r")
    y = (opening.readlines())
    list = []
    r = 0
    for i in y:
        s = y[r].split()
        list.append(s)
        r += 1
    count = 0
    that_dict = dict()
    for i in list:
        if list[count][0] not in that_dict:
            that_dict.update({list[count][0]: list[count][1]})
        else:
            that_dict[list[count][0]] = [that_dict[list[count][0]], list[count][1]]
        count += 1
    return that_dict


def all_my_friends(friend):
    '''
    purpose: function imported in a2q2 with purpose of taking a friend in list as input + returns list of friends that are friends with that given name
    :param friend: a friend in list as taken as input
    :return: list of friends for the friend taken as input
    '''
    x = friends_to_dictionary()
    return [x[friend]]
def friendship_degree(x):
    '''
    purpose: uses previous functions to state the friends that each 'friend' has
    :param x: variable for dictionary returned by friends_to_dictionary
    :return: returns the amount of friends+friends each person from dictionary has
    '''
    for friend in x:
        values = all_my_friends(friend)
        print(f"{friend}" ' has', len(x[friend]), 'friends: (', (str(values).strip('[]')) + ')' )
