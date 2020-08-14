#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# While Loop
# When the condition is true, the body of the loop is executed.
# When the body is complete, the condition is tested again.
# And if the condition is still true, the body is executed again.
# The loop continues as long as the condition is true,
secret = 'swordfish'
pw = ''

auth = False
count = 0
maxAttempt = 5

while pw != secret:     # uses conditional expression
    count += 1
    if count > maxAttempt:
        break   # additional control
    if count == 3:
        continue    # will go back to start
    pw = input(f"{count}: What's the secret word? ")
else:   # else control / execute if loop ends normally
    auth = True
print("Authorized" if auth else "Calling the FBI..")
