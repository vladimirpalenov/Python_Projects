# Name: Vladimir Palenov
# SSID: 1576921
# Assignment  #: 1
# Submission  Date: 3/1/2021
#
# Description  of  program:
# This  program  computes  the  area of a circle  and
# volume  of a cylinder  from a radius

# importing math library
import math
# displaying welcome message
print ('Welcome! This program will help you to calculate area and volume based on radius.\n')
# displaying prompt message, getting user's input and assigning it to the variable
radius = float(input('Enter a radius to compute the area of a circle and the volume of a sphere:\n'))
# calculating the area and assigning it to another variable
area = math.pi * radius ** 2
# formatting the area variable to have 2 decimals
area = format(area, '.2f')
# displaying the result for the area
print ('The area of a circle, with radius ', radius, ' is ', area)
# calculating the volume and assigning it to a variable
volume = 4 / 3 * math.pi * radius ** 3
# formatting the volume variable to have 2 decimals
volume = format(volume, '.2f')
# displaying the result for the volume
print ('The volume of a sphere with radius ', radius, ' is ', volume)
