# format specifiers  = {value:flags} format a value based on what 
# flags are inserted

# :<  = left align
# :>  = right align
# :^  = center
# :=  = pad after the sign but before the digits
# :+  = show the sign for both positive and negative numbers
# :  = no sign for positive 
# :,  = use a comma as a thousand separator
# :_  = use an underscore as a thousand separator
# :b  = binary format
# :c  = convert to the corresponding unicode character
# :d  = decimal format
# :e  = scientific format with a lower case e
# :E  = scientific format with an upper case E
# :f  = fixed point number format
# :F  = fixed point number format, upper case
# :g  = general format
# :G  = general format
# :o  = octal format
# :x  = hexadecimal format, lower case
# :X  = hexadecimal format, upper case
# :n  = number format
# :%  = percentage format
# :.N = round to N decimal places
# :mN = minimum width of N characters
# :0N = pad with zeros to a width of 
# :> = right align
# :< = left align
# :^ = center align

price1 = 1200.34
price2 = -9123.1
price3 = 12300.34

print(f'Price1 is ${price1:0.1f}')#.2f is 2 decimal places
print(f'Price2 is ${price2:0.1f}')
print(f'Price3 is ${price3:0.1f}')

print(f'Price1 is ${price1:0>10.2f}')#10 characters wide, pad with 0s
print(f'Price2 is ${price2:0>10.2f}')
print(f'Price3 is ${price3:0>10.2f}')

print(f'Price1 is ${price1:0<10.2f}')#10 characters wide, pad with 0s           
print(f'Price2 is ${price2:0<10.2f}')
print(f'Price3 is ${price3:0<10.2f}')

print(f'Price1 is ${price1:0^10.2f}')#10 characters wide, pad with 0s
print(f'Price2 is ${price2:0^10.2f}')
print(f'Price3 is ${price3:0^10.2f}')

print(f"Price1 is ${price1:0=+10.2f}")#10 characters wide, pad with 0s, show sign
print(f"Price2 is ${price2:0=+10.2f}") 
print(f"Price3 is ${price3:0=+10.2f}")

