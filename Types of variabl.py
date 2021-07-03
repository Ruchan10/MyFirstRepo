def outer_function():
    a = 20
    def inner_function():
        a = 30
        print('Local Variable: ', a)
    inner_function()
    print('Non-Local Variable: ', a)
a = 10
outer_function()
print('Global Variable: ', a)