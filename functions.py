def greet():
    """
    This function greets the user
    """
    print("hello User")
print(greet.__doc__)

# Greet

def add_nums(num1, num2):
    print(num1 + num2)

add_nums(6,3)



def my_fuc():
    x = 10
    print("value outside function:",x)

x = 20
my_fuc()
print("value outside function:",x)



#Arguments

def add(x, y):
    """This function adds two numbers"""
    print(x + y)

add(1, 2)


#Variable default argument

def add(x, y=5):
    """This function adds two numbers"""
    print(x + y)

print(add(1))


#Python Keyword Arguments
def login(username, password):
    """This function logs in a user"""
    print(username, password)

login(username='admin', password='1234')
# admin 1234

login(password='1234', username='admin')
# admin 1234



# Python Arbitrary Arguments
def add(*args):
    """This function adds unlimited number of arguments"""
    print(sum(args))

print(add(1, 2, 3, 4, 5))