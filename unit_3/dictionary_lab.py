""" 
Ask the user for the number of feet, and print out the equivalent distance in meters.

Hint: 1 ft is 0.3048 m.

So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
Version 2

Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

Hint: Try using the unit as the key and the conversion as the value.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
Version 3

Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m
"""
# .........................................................................................#

metric_feet_conversion = {
    "feet": 0.3048
}

user_input = input('Enter number of feet: ')
user_input = int(user_input)
calculated_val = user_input * metric_feet_conversion["feet"]
print(f'{user_input} ft is equals {round(calculated_val, 2)} meters')

# .........................................................................................#
metrics = {
    "feet": 0.3048, 
    "miles": 1609.34, 
    "meters": 1, 
    "kilometers": 1000
}
distance = input('What is the distance? ')
distance = int(distance)
units = input('What is the unit? ')
total_val = distance * metrics[units]
print(f'{distance} {units} is {total_val}  meters')

# .........................................................................................#

# adding yard to dictionary
metrics.update({"yard": 0.9144, "inch": 0.0254})
print(metrics)
