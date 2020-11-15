def weather_condition(temp):
    if temp > 7:
        return "Warm"
    else:
        return "Cold"


user_name = input("Name: ")
user_surname = input("Surname: ")
print("Hello %s %s" % (user_name, user_surname))
print(f"Hello {user_name} {user_surname}")  # note: only python version >= 3.6

user_input = float(input("Enter temperature: "))
print(weather_condition(user_input))
