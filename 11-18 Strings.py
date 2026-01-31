# ---------------------
# -- Strings Methods --
# ---------------------

#? strip() rstrip() lstrip()

a = "    I Love Python    "
print(a.strip())    # Return a copy of a string with leading and trailing characters removed.
print(a.rstrip())   # Return a copy of a string with trailing characters removed.
print(a.lstrip())   # Return a copy of a string with leading characters removed.

a = "#####I Love Python####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#I Love Python@#@#@"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# ?title()
#returns a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase.
b = "i love 2d graphics and 3g technology and python"
print(b.title())
    
#? capitalize() 
# returns a copy of the string with its first character capitalized and the rest lowercased.
b = "i love 2d graphics and 3g technology and python"
print(b.capitalize()) 

#? zfill
# Returns a copy of the string left-padded with zeros to a total width of specified number of characters.
c, d, e, f = "1", "11", "111", "1111"

print(c)
print(d)
print(e)
print(f)

print(c.zfill(4))
print(d.zfill(4))
print(e.zfill(4))
print(f.zfill(4))

#? upper()
# Returns a copy of the string with all the cased characters converted to uppercase.
g = "osama"
print(g.upper())

#? lower()
# Returns a copy of the string with all the cased characters converted to lowercase.
h = "OSama"
print(h.lower())

# ---------------------
# -- Strings Methods --
# ---------------------

#? split() rsplit()
# Splits the string at the specified separator, and returns a #! list of substrings.
a = "I Love Python and PHP and MySQL"
print(a.split())

b = "I-Love-Python-and-PHP-and-MySQL"
print(b.split("-"))

c = "I-Love-Python-and-PHP-and-MySQL"
print(c.split("-", 3)) # Split at the first 3 occurrences

d = "I-Love-Python-and-PHP-and-MySQL"
print(d.rsplit("-", 3)) # Split at the last 3 occurrences

#? center()
# Returns a centered string of a specified width.
e = "Osama"
print(e.center(9))  # Spaces
print(e.center(9, "#"))  # Hashes
print(e.center(15, "@"))  # @


#? count()
# Returns the number of occurrences of a substring in the string.
f = "I Love Python and PHP Because PHP is Easy"
print(f.count("PHP"))  # 2 PHP Words
print(f.count("PHP", 0, 25)) #check in the first 25 characters   #!Only One PHP Word


#? swapcase()
# returns a copy of the string with uppercase characters converted to lowercase and vice versa.
g = "I Love Python"
h = "i lOVE pYTHON"
print(g.swapcase())
print(h.swapcase())

#? startswith()
# returns True if the string starts with the specified prefix, otherwise False.
i = "I Love Python"
print(i.startswith("I"))
print(i.startswith("S"))
print(i.startswith("P", 7, 12))

#? endswith()
# returns True if the string ends with the specified suffix, otherwise False.
j = "I Love Python"
print(j.endswith("n"))
print(j.endswith("S"))
print(j.endswith("e", 2, 6))

# ---------------------
# -- Strings Methods --
# ---------------------

#? index(SubString, Start of search, End)
# Returns the lowest index of the substring if found in the string. || Raises a ValueError if the substring is not found.
a = "I Love Python"
print(a.index("P"))  # Index Number 7
print(a.index("t", 8, ))  # Index Number 7
print(a.index("P", 0, 5))  #! Through Error


#? find(SubString, Start, End)
# Returns the lowest index of the substring if found in the string. || Returns -1 if the substring is not found.
b = "I Love Python"
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

#~ the difference between index and find : index --> error || find --> -1 (if the substring is not found)


#? rjust(Width, Fill Char) ljust(Width, Fill Char)
# Returns a right/left justified string of a specified width.
c = "Osama"
print(c.rjust(10))
print(c.rjust(10, "#"))
d = "Osama"
print(d.ljust(10))
print(d.ljust(10, "#"))

#? splitlines()
# Splits the string at line breaks and # returns a list of lines.
e = """First Line
Second Line
Third Line"""
print(e.splitlines())

f = "First Line\nSecond Line\nThird Line"

print(f.splitlines())

#? expandtabs()
# Sets the tab size of the string.
g = "Hello\tWorld\tI\tLove\tPython"
print(g.expandtabs(2))


#? istitle()
# Returns True if the string follows the rules of a title.(the first letter in each word is uppercase and all other letters are lowercase)
one = "I Love Python And 3G"
two = "I Love Python And 3g"
print(one.istitle())
print(two.istitle())

#? isspace()
# Returns True if the string contains only whitespace characters.
three = " "
four = ""
print(three.isspace())
print(four.isspace())

#? islower()
# Returns True if the string contains only lowercase characters.
five = 'i love python'
six = 'I Love Python'
print(five.islower())
print(six.islower())


#? isidentifier()
# Returns True if the string is a valid identifier.-> A valid identifier must start with a letter or underscore (_) and can be followed by letters, digits (0-9), or underscores.
seven = "osama_elzero"
eight = "OsamaElzero100"
nine = "Osama--Elzero100"
print(seven.isidentifier())
print(eight.isidentifier())
print(nine.isidentifier())

#? isalpha()
# Returns True if the string contains only alphabetic characters.
x = "AaaaaBbbbbb"
y = "AaaaaBbbbbb111"
print(x.isalpha())
print(y.isalpha())

#? isalnum()
# Returns True if the string contains only alphanumeric characters (letters and numbers).
u = "AaaaaBbbbbb01"
z = "AaaBbbb011_1"
print(u.isalnum())
print(z.isalnum())

# ---------------------
# -- Strings Methods --
# ---------------------
# replace(Old Value, New Value, Count) : 
# Return a copy of a string with some or all occurrences of a substring replaced with a new one.

a = "Hello One Two Three One One"
print(a.replace("One", "1")) #defult count is replacing all items of old value 
print(a.replace("One", "1", 1))
print(a.replace("One", "1", 2))

# join(Iterable)

myList = ["Osama", "Mohamed", "Elsayed"]
print("-".join(myList))
print(" ".join(myList))
print(", ".join(myList))
print(type(",".join(myList)))

# ------------------------
# -- Strings Formatting --
# ------------------------

name = "Osama"
age = 36
rank = 10

print("My Name is:" + name)
print("My Name is: " + name + " and My Age is: " + age)  #! Type Error

print("My Name is: %s" % "Osama")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age)) ### % place holder
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank))

# %s => String
# %d => Number
# %f => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: %d" % myNumber)
print("My Number is: %f" % myNumber)
print("My Number is: %.2f" % myNumber) #كم عدد الارقام بعد العلامه العشريه 

# Truncate String اشيل من السترينج حاجات مش عاوزها 

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is %s" % myLongString)
print("Message is %.5s" % myLongString) #print [0:5] from myLongString --> Message is Hello.

# ---------------------------------
# -- Strings Formatting #~New Ways --
# ---------------------------------

name = "Osama"
age = 36
rank = 10

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: {}".format("Osama"))
print("My Name is: {}".format(name))
print("My Name is: {} My Age: {}".format(name, age))
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(name, age, rank))

##{:s} => String 
#~{:d} => Number  
#?{:f} => Float

n = "Osama"
l = "Python"
y = 10

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y))

# Control Floating Point Number

myNumber = 10
print("My Number is: {:d}".format(myNumber))
print("My Number is: {:f}".format(myNumber))
print("My Number is: {:.2f}".format(myNumber))

# Truncate String

myLongString = "Hello Peoples of Elzero Web School I Love You All"
print("Message is {}".format(myLongString))
print("Message is {:.5s}".format(myLongString))
print("Message is {:.13s}".format(myLongString))

# Format Money

myMoney = 500162350198

print("My Money in Bank Is: {:d}".format(myMoney))
print("My Money in Bank Is: {:_d}".format(myMoney))
print("My Money in Bank Is: {:,d}".format(myMoney)) # مش اي علامه تنفع 


# ReArrange Items

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}"  .format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30
print("Hello {} {} {}".format(x, y, z))
print("Hello {1:d} {2:d} {0:d}".format(x, y, z))
print("Hello {2:f} {0:f} {1:f}".format(x, y, z))
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z)) 

#{index:.&type}  || &:control floating || typr: d/f/s

# Format in Version 3.6+

myName = "Osama"
myAge = 36
print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}") # f:format operator 

