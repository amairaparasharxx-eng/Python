temperature=int(input("Enter the temperature in celcius: "))
if (temperature<20):
    outfit="jacket"
    print("It is cold today.")
    print("Wear a", outfit)
else:
    outfit="t-shirt"
    print("It is warm today.")
    print("Wear a", outfit)

raining=input("Is it raining (yes/no): ")
if(raining=="yes"):
    print("Bring an umbrella.")
else:
    print("No need for an umbrella.")

windspeed=int(input("Enter the windspeed(km/h): "))
if(windspeed>30):
    windbreaker="Yes"
    print("It is windy today.")
    print("Wear a windbreaker over your", outfit)
else:
    windbreaker="No"
    print("It is calm today.")
    print("No need for a windbreaker")

puddles=input("Are there any puddles?(yes/no): ")
if(puddles=="yes"):
    shoes="boots"
    print("The ground is wet.")
    print("Wear", shoes)
else:
    shoes="sneakers"
    print("The ground is dry.")
    print("Wear", shoes)

print("")
print("weather check complete...\n")
print("-------------------WEATHER OUTFIT PICKER-------------------------")
print("TEMPERATURE: ", temperature)
print("OUTFIT CHOSEN: ", outfit.upper())
print("UMBRELLA:", raining.upper())
print("WIND BREAKER:", windbreaker.upper())
print("SHOES: ", shoes.upper())
print("-----------------------------------------------------------------")