# Andrew Tennant
# DSCI-15310-001 -- Computational Thinking and Programming
# Due Date -- 10/13/2017
# Program #1 -- Fahrenheit, Celsius, Kelvin Converter
# Converts Fahrenheit, Celsius, and Kelvin interchangably

# Acquire the standard being used
standard = str(input("What standard will you be converting from? Input F for Fahrenheit, C for Celcius, or K for Kelvin. "))

Tc = int
Tf = int
Tk = int
if standard == 'f':
    # Farhenheit
    Tf = int(input("What is the temperature in Fahrenheit? "))
    convertTo = str(input("Will we be converting to [C]elcius or [K]elvin? "))
    if convertTo == 'c':
        # Convert to Celcius
        Tc = (5/9)*(Tf-32)
        print(Tf, "degrees fahrenheit is ", round(Tc), "degrees celcius.")
    elif convertTo == 'k':
        # Convert to Kelvin
        Tc = (5/9)*(Tf-32)
        Tk = Tc + 273.15
        print(Tf, "degrees fahrenheit is ", Tk, "kelvin.")
elif standard == 'k':
    # Kelvin
    Tk = int(input("What is the temperature in kelvin? "))
    convertTo = str(input("Will we be converting to [C]elcius or [F]ahrenheit? "))
    if convertTo == 'c':
        # Convert to Celcius
        Tc = Tk - 273.15
        print(Tk, "kelvin is", round(Tc), "degrees celcius.")
    elif convertTo == 'f':
        # Convert to Fahrenheit
        Tc = Tk - 273.15
        Tf = (9/5)*Tc+32
        print(Tk, "kelvin is", round(Tf), "degrees fahrenheit.")
else:
    #Celcius
    Tc = int(input("What is the temperature in celcius? "))
    convertTo = str(input("Will we be converting to [F]ahrenheit or [K]elvin? "))
    if convertTo == 'f':
        # Convert to Fahrenheit
        Tf = (9/5)*Tc+32
        print(Tc, "degrees celcius is ", round(Tf), "degrees fahrenheit.")
    elif convertTo == 'k':
        # Convert to Kelvin
        Tk = Tc + 273.15
        print(Tc, "degrees celcius is ", Tk, "kelvin.")
