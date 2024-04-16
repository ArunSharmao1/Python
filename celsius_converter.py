def to_other_unit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def to_original_unit(converted_temp):
    celsius = (converted_temp - 32) * 5/9
    return celsius
