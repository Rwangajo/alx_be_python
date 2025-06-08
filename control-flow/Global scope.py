count = 0 # Global variable
def increment():
    count += 1 # This refers to the local count within the function
    increment()
print(count)  #Output: 0 (Global count remains unchanged)