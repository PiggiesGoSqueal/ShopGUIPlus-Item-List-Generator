item_list = [
    ("Wheat Seeds", 2.77),
    ("Wheat", 5.01),
    ("Carrot", 7.04),
    # ... (other items)
]

def generate_shop_format(item_name, price):
    item_name_no_space = item_name.replace(" ", "_").upper()
    rounded_price = round(price)
    
    shop_format = f"{item_name_no_space}:\n  MenuItem:\n  - type:{item_name_no_space}\n  - amount:1\n  - name: \"&a{item_name}\"\n  - 'lore1: &7Amount: &a576'\n  - 'lore2: &7Sell For: &a{rounded_price} Resource Points'\n  PriceType: item\n  Price:\n  - - type:{item_name_no_space}\n    - amount:576\n  RewardType: POINTS\n  Reward: {rounded_price}\n  Message: \"&aYou just sold 576 {item_name} for {rounded_price} RP.\"\n  ExtraPermission: ''\n"
    
    return shop_format

for item, price in item_list:
    formatted_item = generate_shop_format(item, price)
    print(formatted_item)
