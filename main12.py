import telebot
from telebot import types

# Replace 'YOUR_BOT_API_TOKEN' with your bot token from BotFather
bot = telebot.TeleBot('7654999319:AAFNx6gMeep483z3xA91dr9WFoekpwtZWvk')

# Menu information for all days of the week
menu = {
    '📅𝗠𝗢𝗡𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Pav Bhaji, Tea',
        '🍲LUNCH': 'Mix Veg, Dal Fry, Green Peas Pulao, Raita, Chapati and Fruits',
        '🍩SNACKS': 'Masala Pav, Tea',
        '🍽DINNER': 'Matar Paneer/Palak Paneer, Dal Fry, Plain Rice, Shahi Tukda, Chapati'
    },
    '📅𝗧𝗨𝗘𝗦𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Poha, Black Chana/Dalia, Coconut Chutney, Tea',
        '🍲LUNCH': 'Rajma Masala, Aloo Bhindi Dry, Plain Rice, Curd, Salad, Chapati and Fruits',
        '🍩SNACKS': 'Samosa, Chutney, Tea',
        '🍽DINNER': 'Chhole Masala, Dal Fry, Masala Rice, Methi Roti, Sheera'
    },
    '📅𝗪𝗘𝗗𝗡𝗘𝗦𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Idli, Sambhar/Coconut Chutney, Tea',
        '🍲LUNCH': 'Dal Makhni, Chana Cabbage Dry, Zeera Rice, Curd, Chapati and Fruits',
        '🍩SNACKS': 'Vada Pav, Tea',
        '🍽DINNER': 'Paneer Kofta/Chicken Curry, Dal Fry, Rice, Chapati, Fruit Custard'
    },
    '📅𝗧𝗛𝗨𝗥𝗦𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Puri Bhaji, Tea',
        '🍲LUNCH': 'Veg Biryani, Curry, Papad, Raita and Fruits',
        '🍩SNACKS': 'Poha, Chutney, Coffee',
        '🍽DINNER': 'Aloo Gobhi/Veg Tawa (Alternative Week), Chana Dal Palak, Zeera Rice, Ajwain Chapati, Gulab Jamun'
    },
    '📅𝗙𝗥𝗜𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Bread Butter Jam, Veg Cutlet/Boiled Eggs (2 Pcs), Tea',
        '🍲LUNCH': 'Aloo Matar, Dahi Kadi and Onion Pakoda (2 Pcs), Plain Rice, Salad, Roti and Fruits',
        '🍩SNACKS': 'Bread Pakoda, Chutney, Tea',
        '🍽DINNER': 'Paneer Kadai/Egg Curry, Plain Rice, Dal Fry, Chapati, Shevai Kheer'
    },
    '📅𝗦𝗔𝗧𝗨𝗥𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Aloo Paratha, Curd, Tea',
        '🍲LUNCH': 'Methi Roti/Chhole Bhature (Alternative Week), Chhole Masala, Rice, Dal Fry, Boondi Raita, Salad and Fruits',
        '🍩SNACKS': 'Bhel (Onion + Chilies Incl), Coffee',
        '🍽DINNER': 'Soyabean Sabzi, Masoor Dal Fry, Masala Rice, Chapati, Rice Kheer/Chinese Food (Chow Mein, Fried Rice, Soup)'
    },
    '📅𝗦𝗨𝗡𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Onion-Tomato Uttapam/Veg Upma, Sambhar, Tea',
        '🍲LUNCH': 'Black Chana Masala, Dal Fry, Rice, Raita, Chapati and Fruits',
        '🍩SNACKS': 'Cream Bun, Tea',
        '🍽DINNER': 'Aloo Palak/Aloo Mattar (As per season), Panchratan Dal, Green Peas Pulav, Puri/Methi Roti, Sabudana Kheer'
    }
}

# Menu photos paths (replace with actual file paths on your computer)
menu_photos = {
    '📅𝗠𝗢𝗡𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Pav bhaji.jpg',
        '🍲LUNCH': 'monday lunch..jpg',
        '🍩SNACKS': 'masala pav.JPG',
        '🍽DINNER': 'monday dinner.jpg'
    },
    '📅𝗧𝗨𝗘𝗦𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Untitled Project (2).jpg',
        '🍲LUNCH': 'tuesday lunmch.jpg',
        '🍩SNACKS': 'samosa.jpg',
        '🍽DINNER': 'tuesday dinner.jpg'
    },
    '📅𝗪𝗘𝗗𝗡𝗘𝗦𝗗𝗔𝗬': {
        '☕BREAKFAST': 'idli.jpg',
        '🍲LUNCH': 'wednesday lunch.jpg',
        '🍩SNACKS': 'vada pav.jpg',
        '🍽DINNER': 'wednesday night.jpg'
    },
    '📅𝗧𝗛𝗨𝗥𝗦𝗗𝗔𝗬': {
        '☕BREAKFAST': 'Pav bhaji.jpg',
        '🍲LUNCH': 'thursday lunch.jpg',
        '🍩SNACKS': 'poha.jpg',
        '🍽DINNER': 'thursday night.jpg'
    },
    '📅𝗙𝗥𝗜𝗗𝗔𝗬': {
        '☕BREAKFAST': 'bread butter jam.jpg',
        '🍲LUNCH': 'friday lunch.jpg',
        '🍩SNACKS': 'bread pakoda.jpg',
        '🍽DINNER': 'friday dinner.jpg'
    },
    '📅𝗦𝗔𝗧𝗨𝗥𝗗𝗔𝗬': {
        '☕BREAKFAST': 'aloo paratha.jpg',
        '🍲LUNCH': 'saturday lunch.jpg',
        '🍩SNACKS': 'murmura.jpg',
        '🍽DINNER': 'saturday night.jpg'
    },
    '📅𝗦𝗨𝗡𝗗𝗔𝗬': {
        '☕BREAKFAST': 'upma.jpg',
        '🍲LUNCH': 'sunday lunch.jpg',
        '🍩SNACKS': 'cream roll.jpg',
        '🍽DINNER': 'sunday night.jpg'
    }
}

# Start command handler
@bot.message_handler(commands=['Hii'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    days = ['📅𝗠𝗢𝗡𝗗𝗔𝗬', '📅𝗧𝗨𝗘𝗦𝗗𝗔𝗬', '📅𝗪𝗘𝗗𝗡𝗘𝗦𝗗𝗔𝗬', '📅𝗧𝗛𝗨𝗥𝗦𝗗𝗔𝗬', '📅𝗙𝗥𝗜𝗗𝗔𝗬', '📅𝗦𝗔𝗧𝗨𝗥𝗗𝗔𝗬', '📅𝗦𝗨𝗡𝗗𝗔𝗬']
    for day in days:
        markup.add(types.KeyboardButton(day))

    bot.send_message(message.chat.id, "Aa gya bhulakad 😝\n Ab bata kis din ka khana bhul gaya🤔", reply_markup=markup)

# Day selection handler
@bot.message_handler(func=lambda message: message.text in menu.keys())
def day_selection(message):
    selected_day = message.text
    markup = types.ReplyKeyboardMarkup(row_width=2)
    meals = ['☕BREAKFAST', '🍲LUNCH', '🍩SNACKS', '🍽DINNER']
    for meal in meals:
        markup.add(types.KeyboardButton(meal))

    bot.send_message(message.chat.id, f"Acha tu {selected_day} ka bhula hai😃, Ab bata konsa time ka khana bhul gaya🤔 ", reply_markup=markup)

    # Save selected day for further reference
    bot.register_next_step_handler(message, lambda msg: meal_selection(msg, selected_day))

# Meal selection handler
def meal_selection(message, selected_day):
    selected_meal = message.text
    if selected_meal in menu[selected_day]:
        # Send the meal description
        bot.send_message(message.chat.id, f"toh dekh {selected_meal} iss {selected_day} ka ya hai😃😃: {menu[selected_day][selected_meal]}")

        # Send the corresponding photo
        if selected_meal in menu_photos[selected_day]:
            photo_path = menu_photos[selected_day][selected_meal]
            with open(photo_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)

    else:
        bot.send_message(message.chat.id, "Abae Jyada tej na bann jo puchna hai puch")

    # End or continue offering assistance
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Aur jana ka liya /Hii click kar😀😊", reply_markup=markup)

# Polling
bot.polling()