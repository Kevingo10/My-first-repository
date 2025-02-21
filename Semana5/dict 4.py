# Dada una lista de ventas con la siguiente información:date / customer_email / items
# Y cada item teniendo la siguiente información: name / upc / unit_price
# Cree un diccionario que guarde el total de ventas de cada UPC.

sales = [
    {"date" : "25/11/2024",
     "customer_email" : "kevin@hotmail.com",
     "items": [
        {
         "name" : "PC",
         "upc" : "ITEM 450",
         "unit_price" : 35.85,
        },
        {
        "name" : "keyboard",
         "upc" : "ITEM 430",
         "unit_price" : 98.56,
         },
         {"name" : "mouse",
          "upc" : "ITEM 420",
          "unit_price" : 15.32,
          }, 
    ],
},
]
{
    "date" : "26/11/2024",
    "customer_email" : "kevin10@hotmail.com",
    "items" : [
        {
            "name" : "case",
            "upc" : "ITEM 420",
            "unit_price" : 98,
        },
    ],
},
totales_upc = {}
for sale in sales:
    for item in sale["items"]:
        upc = item["upc"]
        unit_price = item["unit_price"]
        if upc in totales_upc:
            totales_upc[upc] += unit_price
        else:
            totales_upc[upc] = unit_price
for upc, total in totales_upc.items():
    print(f"UPC: {upc}, total de ventas: {total}")


