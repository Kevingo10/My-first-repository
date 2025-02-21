import json

with open("C:/Users/USUARIO/OneDrive/Desktop/Python/Semana 8/pokemon.json.txt", "r") as file:
    data = json.load(file)
  

new_pokemon = {
    "name" : {
        "english" : "Bulbasaur"
    },
    "type" : [
        "plant"
    ],
    "base":{
        "HP" : 45,
        "Attack" : 49,
        "Defense" : 49,
        "Sp. Attack" : 65,
        "Sp. Defense" : 65,
        "speed" : 45
    }
}

data.append(new_pokemon)

with open("C:/Users/USUARIO/OneDrive/Desktop/Python/Semana 8/pokemon.json.txt", "w") as file:
    json.dump(data, file, indent=4)

print("Pokemon agregado correctamente")
    
