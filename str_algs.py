def reverce (message):
    letter = ""
    for i in range(len(message)):
        letter = letter + message[len(message) - (i+1)]
    return letter
message = "hello, world"
print (reverce(message))

