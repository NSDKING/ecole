# Dictionary of days with corresponding weather
weather = {
    "Lundi": [],        
    "Mardi": [],
    "Mercredi": [],
    "Jeudi": [],
    "Vendredi": [],
    "Samedi": [],
    "Dimanche": []
}

def add_weather(day, temperature):
    try:
        if not isinstance(temperature, int):
            raise TypeError("Weather must be an integer")
        weather[day].append(temperature)
        print(f'Temperature {temperature} added for {day}')
    except TypeError as e:
        print(f'Error: {str(e)}')

def show_weather(day):
    try:
        if not isinstance(day, str):
            raise TypeError("Day must be a string")
        print(f'Weather for {day}: {weather[day]}')
    except TypeError as e:
        print(f'Error: {str(e)}')

def show_all_weather():
    for day in weather:
        show_weather(day)

print("choose what you want to do")
print("1: add temperature")
print("2: show_weather")
print("3: show_all_weather")

def is_a_days_of_the_week(day):
    weeksday=["Lundi", "Mardi", "Mercredi", "Jeudi", 'Vendredi', "Samedi","Dimanche"]
    if day in weeksday:
        return True
    else:
        return False

command =  int(input())
while type(command) != int:
    print("command must be an int")
    command = int(input())


if command == 1:
    try:
        day = input("enter the day: ")
        if not isinstance(day, str):
            raise TypeError("day must be a str")
        is_day_valid = is_a_days_of_the_week(day)
        
        while is_day_valid == False:
            day = input("enter the day: ")
            if not isinstance(day, str):
                raise TypeError("day must be a str")
            is_day_valid = is_a_days_of_the_week(day)

        temperature = int(input("enter the temperature : "))
        if not isinstance(temperature, int):
            raise TypeError("temperature must be a int")
        print(f'Weather for {day}: {weather[day]}')
        add_weather(day, temperature)
    except TypeError as e:
        print(f'Error: {str(e)}')
elif command == 2:
    try:
        day = input("enter the day : ")
        if not isinstance(day, str):
            raise TypeError("day must be a str")
        is_day_valid = is_a_days_of_the_week(day)
        
        while is_day_valid == False:
            day = input("enter the day: ")
            if not isinstance(day, str):
                raise TypeError("day must be a str")
            is_day_valid = is_a_days_of_the_week(day)
        show_weather(day)
    except TypeError as e:
        print(f'Error: {str(e)}')
elif command == 3:
    show_all_weather()

