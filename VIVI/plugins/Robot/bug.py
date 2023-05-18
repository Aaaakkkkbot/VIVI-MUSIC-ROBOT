from datetime import datetime

from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
    Message,
)

from VelionaMusicBot import app as Client
from config import (
    OWNER_ID as owner_id,
)

SUPPORT = "BotsXSupport"

def content(msg: Message) -> [None, str]:
    text_to_return = msg.text

    if msg.text is None:
        return None
    if " " in text_to_return:
        try:
            return msg.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None


@Client.on_message(filters.command("bug"))
async def bug(_, msg: Message):
    if msg.chat.username:
        chat_username = (f"@{msg.chat.username}/`{msg.chat.id}`")
    else:
        chat_username = (f"ᴩʀɪᴠᴀᴛᴇ ɢʀᴏᴜᴩ/`{msg.chat.id}`")

    bugs = content(msg)
    user_id = msg.from_user.id
    mention = "["+msg.from_user.first_name+"](tg://user?id="+str(msg.from_user.id)+")"
    datetimes_fmt = "%d-%m-%Y"
    datetimes = datetime.utcnow().strftime(datetimes_fmt)

    thumb = "https://telegra.ph/file/ccce2f6bff9a1b0dc3818.jpg"
    
    bug_report = f"""
**#ʙᴜɢ :** **@Haruki_Shiga_16**

**ʀᴇᴩᴏʀᴛᴇᴅ ʙʏ :** **{mention}**
**ᴜsᴇʀ ɪᴅ :** **{user_id}**
**ᴄʜᴀᴛ :** **{chat_username}**

**ʙᴜɢ :** **{bugs}**

**ᴇᴠᴇɴᴛ sᴛᴀᴍᴩ :** **{datetimes}**"""

    
    if msg.chat.type == "private":
        await msg.reply_text("<b>» ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ɪs ᴏɴʟʏ ғᴏʀ ɢʀᴏᴜᴩs.</b>")
        return

    if user_id == owner_id:
        if bugs:
            await msg.reply_text(
                "<b>»ʙʀᴜʜ, ʏᴏᴜ'ʀᴇ ᴛʜᴇ ᴏᴡɴᴇʀ ᴏғ ᴛʜᴇ ʙᴏᴛ.</b>",
            )
            return
        else:
            await msg.reply_text(
                "ᴏᴡɴᴇʀ!"
            )
    elif user_id != owner_id:
        if bugs:
            await msg.reply_text(
                f"<b>ʙᴜɢ ʀᴇᴩᴏʀᴛ : {bugs}</b>\n\n"
                "<b>» ʙᴜɢ sᴜᴄᴄᴇssғᴜʟʟʏ ʀᴇᴩᴏʀᴛᴇᴅ ᴀᴛ sᴜᴩᴩᴏʀᴛ ᴄʜᴀᴛ !</b>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• ᴄʟᴏsᴇ •", callback_data=f"close_reply")
                        ]
                    ]
                )
            )
            await Client.send_photo(
                SUPPORT,
                photo=thumb,
                caption=f"{bug_report}",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                "• ᴠɪᴇᴡ ʙᴜɢ •", url=f"{msg.link}"),
                            InlineKeyboardButton(
                                "• ᴄʟᴏsᴇ •", callback_data="close_send_photo")
                        ]
                    ]
                )
            )
        else:
            await msg.reply_text(
                f"<b>» ɴᴏ ʙᴜɢ ᴛᴏ ʀᴇᴩᴏʀᴛ !</b>",
            )
        

@Client.on_callback_query(filters.regex("close_reply"))
async def close_reply(msg, CallbackQuery):
    await CallbackQuery.message.delete()

@Client.on_callback_query(filters.regex("close_send_photo"))
async def close_send_photo(_, CallbackQuery):
    is_Admin = await Client.get_chat_member(
        CallbackQuery.message.chat.id, CallbackQuery.from_user.id
    )
    if not is_Admin.can_delete_messages:
        return await CallbackQuery.answer(
            "ʏᴏᴜ ᴅᴏɴ'ᴛ ʜᴀᴠᴇ ʀɪɢʜᴛs ᴛᴏ ᴄʟᴏsᴇ ᴛʜɪs.", show_alert=True
        )
    else:
        await CallbackQuery.message.delete()
