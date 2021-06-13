# importer une fonction dans helper vers main
from helper import validate_and_execute, user_input_message

import logging

logger = logging.getLogger("main")
logger.error("Error happened in the app")

# utilisation de la Loop While
# user_input = ""
# while user_input != "exit":
#     user_input = input(user_input_message)
#     # connaitre le type de donnees entrer
#     # print(type(user_input.split(":"))
#     days_and_unit = user_input.split(":")
#     print(days_and_unit)
#     # creation du dictionnaire
#     days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
#     print(days_and_unit_dictionary)
#     # verification du type
#     print(type(days_and_unit_dictionary))
#     validate_and_execute()
