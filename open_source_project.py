from datetime import datetime
from tzlocal import get_localzone
import os


#   functions to be used as commands later
def clear():
    os.system('cls clear')

def help():
    print('\n——————————help——————————\nclear: clears the console\n\nquit: ends the program\n\ntime: displays the current time in your time zone\n\ntime (state): shows you what time it is in other US states\n\nmilitary time: displays the current time in your time zone in military time\n\nmilitary time (state): shows you what time it is in other US states in military time\n\nhelp zones: gives a list of abbreviated time zones with their full names\n——————————help——————————\n')

def help_zones():
    print('\n———————help zones———————\nHST: hawaii-aleutian standard time\n\nAKST: alaska standard time\n\nPST: pacific standard time\n\nEST: eastern standard time\n\nMST: mountain standard time\n———————help zones———————\n')

#   this function calculates the current time from military time (default, given by datetime module) and gives AM or PM
def time(offset=None, zone=None):
    global milit_time

    #   checks if there is an offset
    if offset == None:
        #   checks for AM and PM
        if int(milit_time[0:2]) > 12:
            return print(f'\n{int(milit_time[0:2]) - 12}{milit_time[2:5]} PM {zone}\n')
        else:
            return print(f'\n{milit_time} AM {zone}\n')
    else:
        #   checks for AM and PM, applies offset
        if (int(milit_time[0:2]) + offset) > 12:
            return print(f'\n{int(milit_time[0:2]) + offset - 12}{milit_time[2:5]} PM {zone}\n')
        else:
            return print(f'\n{int(milit_time[0:2]) + offset}{milit_time[2:5]} AM {zone}\n')


#   intro message
clear()
print('\nWelcome to the time zone converter!\n\nFor a list of commands, type \'help\'\n')


#   the actual program
while True:
    #   changes the time to add a 0 if the minute is a single digit
    if len(str(datetime.now().minute)) == 2:
        milit_time = f'{str(datetime.now().hour)}:{str(datetime.now().minute)}'
    else:
        milit_time = f'{str(datetime.now().hour)}:0{str(datetime.now().minute)}'
    
    #   user command input
    command = input().lower()

    #   decision structure that checks for all possible command entries
    #   runs clear command
    if command == 'clear':
        clear()

    #   runs help command
    elif command == 'help':
        help()

    #   runs help zones command
    elif command == 'help zones':
        help_zones()

    #   quits program
    elif command == 'quit':
        break

    #   runs time command
    elif command == 'time':
        time(None, 'EST')

    #   runs military time command
    elif command == 'military time':
        print(f'\n{milit_time} EST\n')

    #   checks if the first part of the command is military time
    elif command[0:13] == 'military time':

        #   checks if user is outside of EST (non EST functionality is not implimented yet)
        if str(get_localzone()) != 'America/New_York':
            print('\nYour time zone is not supported for this command\n')

        #   checks which state the user is running the military time command for
        elif command[14:len(command)] in ['ct', 'connecticut', 'de', 'delaware', 'ga', 'georgia', 'me', 'maine', 'md', 'maryland', 'ma', 'massachusetts', 'nh', 'new hampshire', 'nj', 'new jersey', 'ny', 'new york', 'nc', 'north carolina', 'oh', 'ohio', 'pa', 'pennsylvania', 'ri', 'rhode island', 'sc', 'south carolina', 'vt', 'vermont', 'va', 'virginia', 'wv', 'west virginia', 'tn', 'tennessee', 'ky', 'kentucky', 'fl', 'florida', 'in', 'indiana', 'mi', 'michigan']:
            print(f'{milit_time} EST')
        elif command[14:len(command)] in ['al', 'alabama', 'ar', 'arkansas', 'il', 'illinois', 'ia', 'iowa', 'la', 'louisiana', 'mn', 'minnesota', 'ms', 'mississippi', 'mo', 'missouri', 'ok', 'oklahoma', 'wi', 'wiconsin', 'sd', 'south dakota', 'ks', 'kansas', 'ne', 'nebraska', 'nd', 'north dakota', 'tx', 'texas']:
            print(f'\n{int(milit_time[0:2])-1}{milit_time[2:5]} PM CST\n')
        elif command[14:len(command)] in ['id', 'idaho', 'az', 'arizona', 'co', 'colorado', 'mt', 'montana', 'nm', 'new mexico', 'ut', 'utah', 'wy', 'wyoming']:
            print(f'\n{int(milit_time[0:2])-2}{milit_time[2:5]} PM MST\n')
        elif command[14:len(command)] in ['nv', 'nevada', 'or', 'oregon', 'ca', 'california', 'wa', 'washington']:
            print(f'\n{int(milit_time[0:2])-3}{milit_time[2:5]} PM PST\n')
        elif command[14:len(command)] in ['ak', 'alaska']:
            print(f'\n{int(milit_time[0:2])-4}{milit_time[2:5]} PM AKST\n')
        elif command[14:len(command)] in ['hi', 'hawaii']:
            print(f'\n{int(milit_time[0:2])-6}{milit_time[2:5]} PM HST\n')

    #   checks if the first part of the command is time
    elif command[0:4] == 'time':

        #   checks if user is outside of EST (non EST functionality is not implimented yet)
        if str(get_localzone()) != 'America/New_York':
            print('\nYour time zone is not supported for this command\n')

        #   checks which state the user is running the time command for
        elif command[5:len(command)] in ['ct', 'connecticut', 'de', 'delaware', 'ga', 'georgia', 'me', 'maine', 'md', 'maryland', 'ma', 'massachusetts', 'nh', 'new hampshire', 'nj', 'new jersey', 'ny', 'new york', 'nc', 'north carolina', 'oh', 'ohio', 'pa', 'pennsylvania', 'ri', 'rhode island', 'sc', 'south carolina', 'vt', 'vermont', 'va', 'virginia', 'wv', 'west virginia', 'tn', 'tennessee', 'ky', 'kentucky', 'fl', 'florida', 'in', 'indiana', 'mi', 'michigan']:
            time(None, 'EST')
        elif command[5:len(command)] in ['al', 'alabama', 'ar', 'arkansas', 'il', 'illinois', 'ia', 'iowa', 'la', 'louisiana', 'mn', 'minnesota', 'ms', 'mississippi', 'mo', 'missouri', 'ok', 'oklahoma', 'wi', 'wiconsin', 'sd', 'south dakota', 'ks', 'kansas', 'ne', 'nebraska', 'nd', 'north dakota', 'tx', 'texas']:
            time(-1, 'CST')
        elif command[5:len(command)] in ['id', 'idaho', 'az', 'arizona', 'co', 'colorado', 'mt', 'montana', 'nm', 'new mexico', 'ut', 'utah', 'wy', 'wyoming']:
            time(-2, 'MST')
        elif command[5:len(command)] in ['nv', 'nevada', 'or', 'oregon', 'ca', 'california', 'wa', 'washington']:
            time(-3, 'PST')
        elif command[5:len(command)] in ['ak', 'alaska']:
            time(-4, 'AKST')
        elif command[5:len(command)] in ['hi', 'hawaii']:
            time(-6, 'HST')
    
    #   if user input is not recognized as a command, the error message will display
    else:
        print('\nCommand not recognized, try again\n')