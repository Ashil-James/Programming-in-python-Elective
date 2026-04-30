def rate(pricelist, item):
    return pricelist.get(item, -1)

priceList = {
    "Pen": 10, 
    "Pencil": 5, 
    "Eraser": 5, 
    "Ruler": 20
    }

itemprice = rate(priceList, "Ruler")
if itemprice == -1:
    print("Item not found")
else:
    print("Price of item is", itemprice)