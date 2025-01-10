import requests
#EXERCISE 1
#EXERCISE 1
#EXERCISE 1

def dictionaryTest():
  dictionary={'hello':'hola','goodbye':'adios'}
  dictionary['thank you'] = "gracias"
  dictionary['please'] = 'por favor'
  print(dictionary)

  del dictionary['goodbye']
  print(dictionary)

  dictionaryValue = dictionary.get('hello1')
  print("Dictionary value:",dictionaryValue)

  if dictionaryValue:
    print("Value Exists!")
    print("Value:",dictionaryValue)
  else:
    print("Value doesn't exists!")

#EXERCISE 2
#EXERCISE 2
#EXERCISE 2
def movieSchedule():

  movies={
    "The Grinch":"11:00am",
    "Wreck It Ralph":"1:30pm",
    "Shrek 2":"2:00",
    "Coraline":"3:10pm"
  }
  for movie in movies:
    print(movie)
  
  movie = input("What movie do you like the showtime for?\n")
  showtime = movies.get(movie)
  if showtime:
    print("Showtime for",movie,"is",showtime)
  else:
    print("Movie not found")

#EXERCISE 2
#EXERCISE 2
#EXERCISE 2
def dictionaryOfLists():
  menus={"breakfast":["chilaquiles", "molletes", "barbacoa"],
         "lunch":["pizza","tostadas","gorditas"],
         "dinner":["tacos","beagle","cereal"]}
  print(menus)
  for menu in menus:
    for item in menus[menu]:
      print(item)


#EXERCISE 3
#EXERCISE 3
#EXERCISE 3
def contacts():

  contacts = {
    "number":4,
    "students":[
      {"name":"Sarah Holderness", "email":"sarah@example.com"},
      {"name":"Edgar Itzak", "email":"itzak@example.com"},
      {"name":"BobHouda Abubakar", "email":"bobhouda@example.com"},
      {"name":"Anna Chidubem", "email":"anna@example.com"}
    ]
  }

  print("Students Email:")
  for student in contacts["students"]:
    print(student.get("email"))

#EXERCISE 4
#EXERCISE 4
#EXERCISE 4
def requestingJson():
  response = requests.get("http://api.open-notify.org/astros.json")
  json = response.json()
  
  print("People in space:")
  for people in json.get("people"):
    print(people.get("name"))

#EXERCISE 4
#EXERCISE 4
#EXERCISE 4

def consumeWeatherApi():
  key = ""
  url = "http://api.weatherapi.com/v1/current.json?key="+key+"&q=Monterrey&aqi=no"
  response = requests.get(url)
  weatherJson = response.json()

  location= weatherJson.get("location").get("name")+", "+weatherJson.get("location").get("region")+" "+weatherJson.get("location").get("country")
  celcius = weatherJson.get("current").get("temp_c")
  condition = weatherJson.get("current").get("condition").get("text")
  
  print("Today's weather in",location,"is",condition,"and",celcius,"C degrees")

consumeWeatherApi()