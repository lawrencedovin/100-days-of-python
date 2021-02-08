travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_travel_log(country, visits, cities):
    travel_log.append({"counter": country, "visits": visits, "cities": cities})

#🚨 Do not change the code below
add_travel_log("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)