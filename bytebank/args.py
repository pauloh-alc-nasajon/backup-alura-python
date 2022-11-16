"""
*ARGS:

If you do not know how many arguments that will be passed into your function,
add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
"""

def  my_function(*kids):
    print(f'tupla: {kids}')
    print(f'1 - {kids[0]}')
    print(f'2 - {kids[1]}')
    print(f'3 - {kids[2]}')

my_function('Luma', 'Maria', 'Pedro')