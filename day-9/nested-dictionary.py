# Nesting Dictionary in a Dictionary
travel_logs = {
    "France":   {
                    "cities_visited": ["Paris", "Lille", "Dijon"], 
                    "total_visits": 12
                },
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

print(travel_logs["France"]["cities_visited"][0])

# Nesting Dictionary in a List
travel_logz = [
    {   
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
    },
    {   
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 7
    }
]

print(travel_logz[0]["country"])