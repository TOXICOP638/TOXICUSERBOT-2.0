import time
from datetime import datetime

import speedtest
from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message

from Zaid import StartTime, app, SUDO_USER
from Zaid.helper.PyroHelpers import SpeedConvert
from Zaid.modules.bot.inline import get_readable_time

from Zaid.modules.help import add_command_help

class WWW:
    SpeedTest = (
        "Speedtest started at `{start}`\n\n"
        "Ping:\n{ping} ms\n\n"
        "Download:\n{download}\n\n"
        "Upload:\n{upload}\n\n"
        "ISP:\n__{isp}__"
    )

    NearestDC = "Country: `{}`\n" "Nearest Datacenter: `{}`\n" "This Datacenter: `{}`"

@Client.on_message(
    filters.command(["speedtest"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def speed_test(client: Client, message: Message):
    new_msg = await message.reply_text("`Running speed test . . .`")
    try:
       await message.delete()
    except:
       pass
    spd = speedtest.Speedtest()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting Devil power . . .`"
    )
    spd.get_best_server()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Getting devil speed . . .`")
    spd.download()

    new_msg = await new_msg.edit(f"`{new_msg.text}`\n" "`Getting devil powers . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`𝙏𝙀𝘼𝙈 𝘾𝙍𝙄𝙈𝙄𝙉𝘼𝙇𝙎 𝙋𝙊𝙒𝙀𝙍 . . .😈`"
    )
    results = spd.results.dict()

    await new_msg.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )



@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% ▒▒▒▒▒▒▒▒▒▒**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**#𝙏𝙀𝘼𝙈 𝘾𝙍𝙄𝙈𝙄𝙉𝘼𝙇𝙎**")
    await xx.edit("**𝘿𝘼𝙉𝙂𝙀𝙍𝙊𝙐𝙎**")
    await xx.edit("**𝙁𝙐𝘾𝙆𝙄𝙉𝙂**")
    await xx.edit("**𝙈𝙊𝘿𝙀**")
    await xx.edit("**𝘼𝘾𝙏𝙄𝙑𝘼𝙏𝙀𝘿😈**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await xx.edit(
        f"❏ **╰☞TEAM CRIMINALS OP ™╮**\n"
        f"├• **╰☞FUCKTIME** - `%sms`\n"
        f"├• **╰☞ -** `{uptime}` \n"
        f"└• **╰☞:** {client.me.mention}" % (duration)
    )


add_command_help(
    "ping",
    [
        ["ping", "Check bot alive or not."],
    ],
)
