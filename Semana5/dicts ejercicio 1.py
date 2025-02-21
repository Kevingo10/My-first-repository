# Cree un diccionario que guarde la siguiente información sobre un hotel: nombre , numero_de_estrellas, habitaciones
# El key de habitaciones debe ser una lista, y cada habitación debe tener la siguiente información
# numero, piso, precio_por_noche

hotel_info =[
{
"name" : "El Cajon",
"num_star" : 5,
"rooms": [
    {"number":1, "Floor": 3, "price per night": 5},
    {"number": 4, "Floor": 7, "price per night": 20}
    ],
},
]
print(hotel_info[0]["rooms"][0])

