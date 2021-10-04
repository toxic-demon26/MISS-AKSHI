from pyrogram import filters
from LunaRobot import pbot as app
from LunaRobot.utils.errors import capture_err
from LunaRobot.utils.http import get


@app.on_message(filters.command("repo") & ~filters.edited)
@capture_err
async def repo(_, message):
    users = await get(
        "https://api.github.com/repos/zeinzo/LunaRobot/contributors"
    )
    list_of_users = ""
    count = 1
    for user in users:
        list_of_users += (
            f"**{count}.** [{user['login']}]({user['html_url']})\n"
        )
        count += 1

    text = f"""[Luna](https://t.me/lunatapibot) | [Channel](https://t.me/aboutraks)
**----------------
| Contributors |
----------------**
{list_of_users}
[❒ Repository ❒](https://github.com/zeinzo/LunaRobot)"""
    await app.send_message(
        message.chat.id, text=text, disable_web_page_preview=True
    )
