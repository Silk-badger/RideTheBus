# four most commmon types of errors in the stack trace.

#1st - Syntax error.
# print(hello world") <-- "unterminated string literal" (basically missing the quotations)

#2nd - Type error.
#x = 2
#y = "Apple"

#sum = x + y <-- the two are different opperand types, as x is an integer and y is a string.
#NOTE: the incorrection wont always been shown, such as this example above. It may not tell you till it's been run.

#3rd - Name error. 
#car_value = 0
#car_speed = 100
#print(car_values) <-- simple mistake, there is no "car_values" but there is a "car_value"

#4th (final) - Value Error
#Math.sqrt(-10) <-- not a full number, so can't be square rooted.