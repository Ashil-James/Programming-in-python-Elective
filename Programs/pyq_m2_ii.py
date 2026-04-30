def update(price_list, product_name, new_rate):
    
    # Case 1: Rate is <= 0 AND product exists
    if new_rate <= 0 and product_name in price_list:
        price_list.pop(product_name)

    elif new_rate > 0 and product_name in price_list:
        price_list[product_name] = new_rate
        
    # Case 3: Rate is positive AND product does NOT exist
    elif new_rate > 0 and product_name not in price_list:
        price_list[product_name] = new_rate
        
    return price_list

# --- Example Usage ---
priceList = {"Pen": 10, "Pencil": 5, "Eraser": 5, "Ruler": 20}

# Testing Case 1 (Removes Eraser)
update(priceList, "Eraser", 0) 

# Testing Case 2 (Updates Pen)
update(priceList, "Pen", 15)   

# Testing Case 3 (Adds Marker)
update(priceList, "Marker", 25) 

print(priceList) 
# Output: {'Pen': 15, 'Pencil': 5, 'Ruler': 20, 'Marker': 25}