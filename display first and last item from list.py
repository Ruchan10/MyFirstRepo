list0=['blue', 'grey', 'orange', 'olive', 'red', 'violet', 'yellow' , 'ghee']
tuple = (10,20,30,40,50,60)
list1 = [0, 1, 10, 11, 100, 101, 110, 111]
print(list0[0], list0[-1]) # Returns first and last element in the list
list0[0] = 'black' # Replaces the element in 0th index with black
print(list0)
list0[1:3] =['green','brown'] #Replaces the elements in 1th and 2nd index with given items respectively
print(list0)
list0.append('white') #Adds given element in the end of the list
print(list0)
del list0[4] # Deletes the element in 4th index
print(list0)
list0.remove('violet') # Removes the given element fron the list
print(list0)
list0.remove(list0[6]) # Removs the item from given index
print(list0)
print(len(list0)) # Returns the number of elements in the list
print(max(list1)) # Returns maximum value from the list
print(min(list1)) # Returns minimum value in the list
print(list(tuple)) # Converts any other data structures to list
del list0 # Deletes the entire list and returns class
print(list0)