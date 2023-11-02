Minecraft ShopGUIPlus Item List Generator

This script simplifies the setup and management of in-game shops in Minecraft servers using ShopGUIPlus.

This Python script is designed to simplify the process of setting up item lists for the popular Minecraft server plugin, ShopGUIPlus. It takes a list of Minecraft item names and their corresponding prices, and generates a well-structured YAML format for use in ShopGUIPlus configuration files. The script replaces spaces in item names with underscores, calculates the slot numbers, and formats the prices correctly, making it easier for server administrators to create and manage in-game shops.

Key Features:

	- Note: By default this is designed to work for adding the Sell prices of items that sell by 64 items at a time. If you'd like to add the buy prices modify the Python output or request ChatGPT to generate your own desired outcome. 
    - Converts a list of item names and prices into a YAML format compatible with ShopGUIPlus.
    - Automatically handles item name formatting (replacing spaces with underscores).
    - Calculates slot numbers following a specific pattern.
    - Ensures proper formatting of prices (without dollar symbols).

Author:

    Created by ChatGPT, an AI language model developed by OpenAI.

Usage:
1. Generate a list of Minecraft items and their prices by providing the official item name followed by the price (either in another program then copy/paste or directly in the program). Item names may have spaces but must be official item names to be recognized by ShopGUIPlus properly.
	- For an example see Main.py

2. Copy and paste the item list into the script, and run it to generate the formatted output.
		- If you do not have a Python IDE on your computer then use an Online compiler such as: https://www.onlinegdb.com/online_python_compiler

3. Paste the output of the program into ShopTemplate.yml where it states to.

	
Contribution:

    Contributions and improvements to the code are welcome and encouraged. Feel free to use, modify, and share it with the Minecraft server community.