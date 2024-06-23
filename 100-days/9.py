#Dist

country_visited = []

country_name = input("Enter country name ")
cities_visited = input("Enter cities visted by comma separated ")
total_visit = int(input("enter total visit inside the country "))

country_visited.append({
  "country_name": country_name,
  "cities_visited": cities_visited.split(","),
  "total_visit": total_visit
})

print(country_visited)