# Production System in Artificial Intelligence

def production_system(temperature, weather):

    if temperature > 35:
        print("It is very hot. Stay indoors.")

    elif temperature > 25:
        print("Weather is warm. Wear light clothes.")

    elif weather == "rainy":
        print("It is raining. Carry an umbrella.")

    elif temperature < 15:
        print("It is cold. Wear warm clothes.")

    else:
        print("Weather is normal. Enjoy your day.")


temperature = int(input("Enter temperature: "))
weather = input("Enter weather (sunny/rainy/cloudy): ").lower()

production_system(temperature, weather)