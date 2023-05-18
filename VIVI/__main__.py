

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from VelionaMusicBot import LOGGER, app, userbot
from VelionaMusicBot.core.call import VIV
from VelionaMusicBot.plugins import ALL_MODULES
from VelionaMusicBot.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("VelionaMusicBot").error(
            "Blehh! Atleast add a pyrogram string..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("VelionaMusicBot").warning(
            "Spotify Client Id & Secret not added."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VelionaMusicBot.plugins" + all_module)
    LOGGER("VelionaMusicBot.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await VelionaMusicBot.start()
    try:
        await VelionaMusicBot.stream_call(
            "https://te.legra.ph/file/0c718de5c84a1940f0b48.jpg"
        )
    except NoActiveGroupCall:
        LOGGER("VelionaMusicBot").error(
            "[ERROR] - #."
        )
        sys.exit()
    except:
        pass
    await VIV.decorators()
    LOGGER("VelionaMusicBot").info("Music Bot Started Successfully, ENJOY PEEPS")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("VIVI").info("Stopping Music Bot")
