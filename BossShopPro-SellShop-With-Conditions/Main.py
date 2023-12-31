# Author: Generated by ChatGPT on 11/4/2023
# Status: WORKING.
# Purpose:
# - Creates a BossShopPro Sell Shop format for the following item list. The numbers are the amount to reward the player for selling 1 inventory worth of items. After selling their items it will also give them a temporary permission for 1 hour that activates the BSP Condition for the item to not allow them to sell the same item type for another hour. 
# Usage: If your items are not already in the below format copy/paste them to ChatGPT and ask it to put your items in that format. Then copy/paste your item list and run the script.
#   - Can use: https://www.onlinegdb.com/online_python_compiler
#   - Crops Example Saved: https://onlinegdb.com/4xsBhsQX1
#   - Mob Drops Example Saved: https://onlinegdb.com/iPeNn9o9u
#
# WANT TO MODIFY AND CAN'T GET CHATPGPT TO DO EXACTLY WHAT YOU NEED? JUST EDIT THE PYTHON CODE DIRECTLY. IT PUTS IT IN A PRETTY STRAIGHTFORWARD FORMAT.
#
# Want to remove all the blank lines it generates between item sections?
# a. In notepad++ do CTRL+F to Find and replace.
# b. "Find what: \n\r"
# c. Replace with: [nothing; blank]
# d. Search mode: Extended
# e. Click "Replace All"
#
# Define your item list with item names and item worth
item_list = [
    ('Wheat Seeds', 11.09),
    ('Wheat', 20.05),
    ('Carrot', 28.16),
    ('Potato', 28.16),
    ('Sugar Cane', 19.80),
    ('Pumpkin', 22.30),
    ('Melon', 23.75),
    ('Cactus', 20.74),
    ('Brown Mushroom', 42.23),
    ('Red Mushroom', 16.21),
    ('Beetroot', 28.16),
    ('Cake', 12.00),
    ('Pumpkin Pie', 50.00),
    ('Cookie', 13.07),
    ('Honey Bottle', 4.00),
    ('Cooked Cod', 8.53),
    ('Cooked Salmon', 23.47),
    ('Pufferfish', 42.67),
    ('Tropical Fish', 36.27),
    ('Kelp', 11.00)
]

# Function to round the item worth to the nearest whole number
def round_item_worth(item_worth):
    return round(item_worth)

# Generate the BossShopPro configuration
for item_name, item_worth in item_list:
    formatted_item_name = item_name.replace(' ', '_')
    rounded_item_worth = round_item_worth(item_worth)
    
    boss_shop_config = f"""
  {formatted_item_name}:
    MenuItem:
    - type:{formatted_item_name}
    - amount:1
    - name:&aSell {item_name}
    - 'lore1:&7Amount: &a2304'
    - 'lore2:&7Sell For: &a{rounded_item_worth} Resource Points'
    - 'lore3:&7Cooldown: &a1 Hour'
    PriceType: item
    Price:
    - - type:{formatted_item_name}
      - amount:2304
    RewardType: COMMAND
    Reward:
    - k admin resourcepoints %kingdoms_name% add {rounded_item_worth}
    - lp user %player% permission settemp bsp.sellshop.cooldown.{formatted_item_name} true 1h
    Message: '&aYou just sold 1 inventory of {item_name} for %price% RP.'
    Condition:
    - type:permission
    - dontmatch:bsp.sellshop.cooldown.{formatted_item_name} 
    ExtraPermission: ''
"""
    print(boss_shop_config)
