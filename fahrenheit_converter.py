def to_other_unit(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def to_original_unit(converted_temp):
    fahrenheit = (converted_temp * 9/5) + 32
    return fahrenheit
