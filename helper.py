# calculation_to_units = 24
# name_of_unit = "hours"


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f'{num_of_days} days are {num_of_days * 24} hours'
    elif conversion_unit == "minutes":
        return f'{num_of_days} days are {num_of_days * 24 * 60} minutes'
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    # isdigit() verfifie que le nombre entrer est bien un chiffre entier sup a zero
    try:
        # on convertit l'enter en un nombre par int(...)
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("tu as taper 0, svp taper un chiffre superieur a zero")
        else:
            print("Vous aviez entrer un nombre negatif !!")
    except:
        print("Ce que vous aviez  entrer est pas un nombre !!")


user_input_message = "Hey!!, vas-y mec ecrit un numero de jours et son unite a convertir !!\n"
