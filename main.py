import asyncio
import os
import discord
from discord.ext import commands
from discord.ext.commands.core import command

class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

bot = commands.Bot(command_prefix = "!", case_insensitive=True)
bot.add_cog(Main(bot))

class europe:
    "This is a person class"
    id = 948023902293069855
class northAmerica:
    "This is a person class"
    id = 948023712635052092
class asia:
    "This is a person class"
    id = 948024425293447188
class oceania:
    "This is a person class"
    id = 948024377444798554

@bot.event
async def on_ready():
    print("Bot Online")

@bot.event
async def on_raw_reaction_add(payload):
    channel = bot.get_guild(894921163430588467)
    if payload.message_id != 948260382525501471:
        return
    if payload.emoji.name == "0️⃣":
      await payload.member.add_roles(europe)
      await payload.member.edit(nick=payload.member.name+" [EU]")
    if payload.emoji.name == "1️⃣":
      await payload.member.add_roles(northAmerica)
      await payload.member.edit(nick=payload.member.name+" [NA]")
    if payload.emoji.name == "2️⃣":
      await payload.member.add_roles(asia)
      await payload.member.edit(nick=payload.member.name+" [ASIA]")
    if payload.emoji.name == "3️⃣":
      await payload.member.add_roles(oceania)
      await payload.member.edit(nick=payload.member.name+" [OCE]")
@bot.event
async def on_raw_reaction_remove(payload):
    channel = bot.get_guild(894921163430588467)
    if payload.message_id != 948260382525501471:
        return
    if payload.emoji.name == "0️⃣":
      user = await channel.fetch_member(payload.user_id)
      await user.remove_roles(europe)
      await user.edit(nick=user.name)
    if payload.emoji.name == "1️⃣":
      user = await channel.fetch_member(payload.user_id)
      await user.remove_roles(northAmerica)
      await user.edit(nick=user.name)
    if payload.emoji.name == "2️⃣":
      user = await channel.fetch_member(payload.user_id)
      await user.remove_roles(asia)
      await user.edit(nick=user.name)
    if payload.emoji.name == "3️⃣":
      user = await channel.fetch_member(payload.user_id)
      await user.remove_roles(oceania)
      await user.edit(nick=user.name)

bot.run(os.getenv("TOKEN"))