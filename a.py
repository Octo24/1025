print('Opening a txt file for writing')
f_obj = open('test.txt', mode='w')
print('Opening a txt file for reading')
f_obj = open('test.txt', mode='r') # overwrites writing mode
# f_obj.close()   #make sure to close files      # look at error below

# uncomment below, will result in error
# f_obj.write("hi")
