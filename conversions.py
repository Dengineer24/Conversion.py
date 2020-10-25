import sys

start = input('''Press [ENTER] to continue or type "quit" to exit
> ''')
if start == "quit":
    sys.exit()
else:
    None
error_message = "You typed an invalid option"
value_message = "A numerical value wasn't found"
system = input('''Do you want to convert in:
metric system "m" 
US system "us"
>''')
if system.lower() == "m":
    conversions_metric = {
        "mm": {"mm": 1, "cm": 1 / 10, "m": 1 / 1000, "km": 1 / 1000000},
        "cm": {"mm": 10, "cm": 1, "m": 1 / 100, "km": 1 / 100000},
        "m": {"mm": 1000, "cm": 100, "m": 1, "km": 1 / 1000},
        "km": {"mm": 100000, "cm": 10000, "m": 1000, "km": 1},
    }
    while True:
        try:
            unit_1m = input(''' What metric units would you like to convert from ?
"mm" 
"cm"
"m"
"km" 
>"''')
            unit_1m.lower()
            value_1m = input('What value of your first unit do you have?: ')

            unit_2m = input('''What metric units would you like to convert to? 
"mm" 
"cm"
"m"
"km" 
>''')
            unit_2m.lower()


            m_math = conversions_metric[unit_1m][unit_2m]

            conv_value_m = int(value_1m) * m_math
            print(f"{conv_value_m} {unit_2m}")
        except KeyError:
            print(error_message)
            sys.exit()
        except ValueError:
            print(value_message)
            sys.exit()
        break
    sys.exit()
if system.lower() == "us":
    conversions_us = {
        "in": {"in": 1, "ft": 1 / 12, "yrd": 1 / 36, "m": 1 / 63360},
        "ft": {"in": 12, "ft": 1, "yrd": 1 / 3, "m": 1 / 5280},
        "yrd": {"in": 36, "ft": 3, "yrd": 1, "m": 1 / 1760},
        "m": {"in": 63360, "ft": 5280, "yrd": 1760, "m": 1},
    }
while True:
    try:
        unit_1us = input(''' What us units would you like to convert from ?
    "in" 
    "ft"
    "yrd"
    "m" 
    >''')
        unit_1us.lower()

        value_1us = input('What value of your first unit do you have?: ')

        unit_2us = input('''What us units would you like to convert to? 
    "in" 
    "ft"
    "yrd"
    "m" 
    >''')
        unit_2us.lower()

        math_us = conversions_us[unit_1us][unit_2us]

        conv_value_us = int(value_1us) * math_us
        print(f"{conv_value_us} {unit_2us}")
    except KeyError:
        print(error_message)
        sys.exit()
    except ValueError:
        print(value_message)
        sys.exit()
    break

else:
    print(error_message)