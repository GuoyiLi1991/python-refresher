name = input("Enter your name: ")
print(name)

# -- Mathematics on user input --

size_input = input("How big is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet / 10.8  # Make sure this is correct

# by this way the decimal issue can fixed
# find the link here: https://blog.tecladocode.com/python-formatting-numbers-for-printing/
square_metres_formatted = f"{square_metres: .2f}"
print(square_metres_formatted)
print(f"{square_feet} square feet is {square_metres} square metres.")
