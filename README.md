# messKemenu


README for Telegram Menu Bot
Overview
This Telegram bot provides users with a menu for different meals throughout the week, including breakfast, lunch, snacks, and dinner. The bot can respond to user input, presenting the meal options and corresponding photos for each day of the week. It also allows the user to navigate through days and meals in a conversational manner.

Features:
Provides a menu for each day of the week.
Sends corresponding images for meals when available.
Allows users to interactively choose the day and type of meal.
Friendly, conversational prompts and replies.
Prerequisites
Python 3.x: Ensure you have Python installed on your system.
TeleBot: Install the pyTelegramBotAPI library by running the following command:
bash
Copy code
pip install pyTelegramBotAPI
Setup Instructions
Step 1: Create a Bot
Go to Telegram and find the BotFather.
Create a new bot by sending /newbot to BotFather and follow the prompts.
You will receive a bot token, which you need to insert into the code.
Step 2: Configure the Bot
Clone or download this repository to your local machine.

In the Python file, replace the placeholder token (YOUR_BOT_API_TOKEN) with the bot token you received from BotFather.

python
Copy code
bot = telebot.TeleBot('YOUR_BOT_API_TOKEN')
Prepare image files:

Ensure that the meal photos specified in the menu_photos dictionary are available in the correct file paths on your machine.
Update the file paths in the menu_photos dictionary with the correct locations for your images:
python
Copy code
menu_photos = {
    '📅𝗠𝗢𝗡𝗗𝗔𝗬': {
        '☕BREAKFAST': 'path/to/your/image1.jpg',
        ...
    },
    ...
}
Step 3: Run the Bot
Run the bot using the following command:

bash
Copy code
python your_bot_script.py
Step 4: Interact with the Bot
Open Telegram and find your bot by its username.
Start a conversation by typing /Hii and follow the prompts to select a day and meal.
Code Walkthrough
Main Components:
Menu Data Structure: The menu dictionary contains all the meal details for each day of the week. Each day has separate entries for breakfast, lunch, snacks, and dinner.

python
Copy code
menu = {
    '📅𝗠𝗢𝗡𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Pav Bhaji, Tea',
        '🍲LUNCH': 'Mix Veg, Dal Fry, Green Peas Pulao...',
        ...
    },
    ...
}
Menu Photos: A separate menu_photos dictionary maps each meal to an image file path.

python
Copy code
menu_photos = {
    '📅𝗠𝗢𝗡𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Pav bhaji.jpg',
        ...
    },
    ...
}
Command Handlers:

/Hii: Starts the interaction with the bot, prompting the user to choose a day.
day_selection: Allows users to select which meal they want for a particular day.
meal_selection: Displays the meal for the selected day and meal type, and sends a corresponding image if available.
Reply Keyboards: The bot uses ReplyKeyboardMarkup to display buttons for days and meal types. This allows users to select options without typing.

python
Copy code
markup = types.ReplyKeyboardMarkup(row_width=2)
How it Works:
When the bot receives /Hii, it presents a keyboard with days of the week.
After selecting a day, the user is asked to choose which meal they want.
The bot then responds with the description of the selected meal and an image if available.
After providing the information, the bot invites the user to restart the interaction by typing /Hii.
Example Interaction:
User sends /Hii.
Bot responds: "Aa gya bhulakad 😝\n Ab bata kis din ka khana bhul gaya🤔"
User selects a day, e.g., "📅𝗧𝗨𝗘𝗦𝗗𝗔𝗬".
Bot responds: "Acha tu 📅𝗧𝗨𝗘𝗦𝗗𝗔𝗬 ka bhula hai😃, Ab bata konsa time ka khana bhul gaya🤔"
User selects a meal, e.g., "🍲LUNCH".
Bot responds with the lunch menu for that day, followed by the corresponding photo if available.
Additional Notes:
If the bot cannot find a meal or photo, it responds with a message saying "Abae Jyada tej na bann jo puchna hai puch."
You can extend this bot by adding more features, such as customizing the menu or adding more meal times.
