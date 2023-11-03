item_list = [
    "String $15.57",
    "Spider Eye $15.69",
    "Egg $16.61",
    "Raw Chicken $16.74",
    "Cooked Chicken $20.75"
]

output = ""

for i, item in enumerate(item_list, start=1):
    item_name, price_str = item.split('$')
    item_name = item_name.strip().replace(" ", "_")
    price = price_str.strip()

    # Calculate the slot number based on your new format
    slot = i - 1

    item_output = f"      {i}:\n"
    item_output += "        type: item\n"
    item_output += "        item:\n"
    item_output += f"          material: {item_name}\n"
    item_output += "          quantity: 64\n"
    item_output += "        buyPrice: -1\n"
    item_output += f"        sellPrice: {price}\n"
    item_output += f"        slot: {slot}\n"

    output += item_output

print(output)
