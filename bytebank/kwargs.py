"""
**kwargs

If you do not know how many keyword arguments that will be passed into your function,
add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
"""

def my_function(**kwargs):
    print(f'dict: {kwargs}')
    print(kwargs['chave1'])
    print(kwargs['chave2'])
    print(kwargs['chave3'])


my_function(chave1='valor1', chave2='valor2', chave3='valor3')