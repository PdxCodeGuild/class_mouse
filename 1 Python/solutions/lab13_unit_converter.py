
'''
1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
1 yard is 0.9144 m
1 inch is 0.0254 m
'''

conversion = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254
}


def validate_unit(message):
    while True:
        unit = input(message)
        if unit not in conversion:
            print(f"Invalid unit. Choose one of the following: {', '.join(list(conversion.keys()))}")
            continue
        else:
            return unit


def main():
    distance = input("Please enter the distance to be converted: ")
    distance = float(distance)

    in_unit = validate_unit("Please enter the unit to convert from: ")
    out_unit = validate_unit("Please enter the unit to convert to: ")


    num_meters = distance * conversion[in_unit]

    result = num_meters / conversion[out_unit]

    print(f"{distance} {in_unit} is {result} {out_unit}")

main()