import time
def show_border(message, border="+"):
    print(border * len(message))
    print(message)
    print(border * len(message))

# continuously appends default value for each function call
def menu(menu=[]):
    menu.append('spam')
    return menu
# Aonther approach is to use immutable objects
def menu_another(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    return menu

# get time function
def show_time():
    return time.ctime()

#  variable scopes LEGB
count = 0
def show_counter():
    print("count= ", count)

def count(c):
    global count
    count = c
    print(count)
