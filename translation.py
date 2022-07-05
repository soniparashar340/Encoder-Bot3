from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):



    START_TEXT = """
Hey! Master {} 
🔸I am alive! 🍀
"""
    HELP_TEXT = """
Recommended
➠ Just Send Me Media To Get Started

Delete Thumbnail
➠ Send /dthumb To Delete Thumbnail

Set Thumbnail
➠ Reply To Photo With /sthumb To Save Thumbnail

Settings
➠ Use /settings Command To Check Settings

Made by Cooldude (my master)...
"""
    ABOUT_TEXT = """
🤖 My Name : Media-Encoder-Bot\n
🚦 Version : <a href='htpps://t.me/doraemon_hindi_movies'>2.0</a>\n
💫 Source Code : <a href='https://te.legra.ph/file/2204524f055aba9a01bb5.jpg'>Click Here</a>\n
🗃️ Library : <a href='https://pyrogram.org'>Click Here</a>\n
👲 Developer : <a href='https://telegram.me/C_O_O_L_DUDE'>TellyBots_4u</a>\n
📦 Last Updated : <a href='https://telegram.me/anicoder_bot'>[ 05-Jul-22 ] 10:32 AM</a>"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Owner', url='https://telegram.me/C_O_O_L_DUDE'),
        InlineKeyboardButton('💬 Off topic', url='https://telegram.me/Otakutalk')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
