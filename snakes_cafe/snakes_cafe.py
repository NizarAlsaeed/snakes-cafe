
menu = [
    {
        'type':'Appetizers',
        'items':['Wings','Cookies','Spring Rolls']   
    },
    {
        'type': 'Entrees',
        'items':['Salmon','Steak','Meat Tornado','A Literal Garden']
    },
    {
        'type':'Desserts',
        'items':['Ice Cream','Cake','Pie']
    },
    {
        'type':'Drinks',
        'items':['Coffee','Tea','Unicorn Tears']
    }
]
order=[]

def intro():
    print(
    """
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **
    ** To quit at any time, type "quit" **
    **************************************
    """)
    for obj in menu:
        print(obj['type']+'\n'+'-'*10)
        for item in obj['items']:
            print(item)
        print('\n')
    get_inputs()


def get_inputs():

    user_input = input(
"""
***********************************
** What would you like to order? **
***********************************
> """)
    while user_input.lower() != 'quit':
        add_to_order(user_input)
        user_input = input('\n> ')

    print('**Thanks for visiting snakes cafe.**\nYour Order summary:')
    order_set = set(order) #set does not contain duplicated items
    for item in order_set:
        print(order.count(item),item)

def add_to_order(user_input):
    order.append(user_input)
    print(f'** {order.count(user_input)} order of {user_input} have been added to your meal **')


intro()

