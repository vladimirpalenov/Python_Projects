# Name: Vladimir Palenov
# SSID: 1576921
# Assignment  #: 3
# Submission  Date: 07/13/2021
#
# Description  of  program:
# This program requests a user to input any string,
# and replaces all letters in the string with the
# opposite case letters without changing other characters

# Function print_opposite_case(sentence:str)
# replaces letter characters in the string with opposite case
# letters without changing other characters
def  print_opposite_case(sentence:str)->None:
    result = ""
    for element in sentence:
        result += get_changed_case(element)
    print (result)

# Function get_changed_case(ch:str)->str:
# takes in a string consisting of one character
# if the character is a letter it returns the same
# letter in opposite case. Other characters are
# returned unchanged
def  get_changed_case(ch:str)->str:
    unicode = ord(ch)
    if (unicode >= 65 and unicode <= 90):
        return chr(unicode + 32)
    elif (unicode >= 97 and unicode <=122):
        return chr(unicode - 32)
    else:
        return ch


# continuous  loop to  prompt  user  for  input
# exits when user inputs 'q'
while  True:
    s = input("Enter a string  to  convert  case to upper  or  lower \
    (press  'q' to exit ):\n")
    if(s == 'q'):
        break
    print_opposite_case(s)
    print("\n")
print("Goodbye")