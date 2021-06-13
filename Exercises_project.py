from datetime import datetime

user_input = input("Entre ton but et sa date de fin separes par une colonne \n")
# on decoupe ce que l'utilisateur rentre dans un tableau en champs
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

# print(datetime.datetime.strptime(deadline, "%d.%m.%Y"))
# print(type(deadline_date = datetime.datetime.strptime(deadline,"%d.%m.%Y"))

deadline_date = datetime.strptime(deadline,"%d.%m.%Y")
today_date = datetime.today()

# calculate how many days till deadline
time_till = deadline_date - today_date
hour_tille = int(time_till.total_seconds() /60 /60)
print(f"Dear user, your time remaining for your goal: {goal} and also {hour_tille} hours ")