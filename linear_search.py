var = 0
def search(lst,num): # Function: Used to perform linear search.
    global var
    for i in range(len(lst)):
       var = i
       if lst[i] == num:
            return True
    return False


lst = [3,2,4,1,6]
num = 4

if search(lst,num):
    print(f'Number is found at {var}')
else:
    print('Not found.')
