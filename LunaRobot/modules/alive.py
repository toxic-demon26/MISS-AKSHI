import re
import os

from telethon import events, Button
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from LunaRobot.events import register as LIVVYCMD
from LunaRobot import telethn as tbot

@LIVVYCMD(pattern=("/reload"))
async def reload(event):
  tai = event.sender.first_name
  text = "✅ **Bot Successfully Updated**"
  await tbot.send_message(event.chat_id, text)
