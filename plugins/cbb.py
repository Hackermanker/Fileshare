#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href='https://t.me/rzxbots'>˹ᴀɴᴏɴ℡˼</a>\n○ 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : <a href='https://docs.pyrogram.org/'>ᴩʏʀᴏɢʀᴀᴍ</a>\n○ 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : <a href='https://www.python.org/download/releases/3.0/'>ᴩyᴛʜᴏɴ 3</a>\n○ 𝖣𝖺𝗍𝖺𝖻𝖺𝗌𝖾 : <a href='https://www.mongodb.com/'>ᴍᴏɴɢᴏDB</a>\n○ 𝖲𝖾𝗋𝗏𝖾𝗋 : <a href='https://t.me/source_Codez/3/'>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n\n😎 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖻𝗒 @rzxbots</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
