
import os
import discord
from discord.ext import commands, tasks
from discord import Interaction
from SteamR import steamfunction
from ComicF import comic_getter
import asyncio
import string
import random
import re
from Anagrams.anagramfun import find_anagrams
from Teeth.teeth import brush_teeth

#tf does this do
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

#@testServerId = 1078893479624712242
#guild_ids=[testServerId]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def sinc(ctx):
    await bot.tree.sync()
    await ctx.send("Ready")
    
    
@bot.event
async def on_message(message):
    '''Testing listener'''
    if message.author == bot.user:
        return
    print(f"hello: {message.content}")

    await bot.process_commands(message)
    
    #wessage = message.content.replace("r", "w").replace("l", "w")
    #await message.delete()
    #await message.channel.send(f"{wessage}")
    
#Unfinished, function does work, needs to be scheduled
@bot.tree.command()
async def teeth(interaction: discord.Interaction):
    '''Will remind you to brush your teeth 4 times a day'''
    await interaction.response.defer()
    try:
        brush_teeth()
        embed = discord.Embed(title="Reminder", description=f"Remember to brush your teeth at least 3 times a day",
                               color=discord.Color.purple())
        file = discord.File("/path/pokemon_image.png", filename="pokemon_image.png",)
        embed.set_image(url="attachment://pokemon_image.png")                          
        await interaction.followup.send(embed=embed, file=file)
    except discord.DiscordException as e:
        embed = discord.Embed(title="Error", description="Please try again or review your argument/permissions",
                               color=discord.Color.red())
        await interaction.followup.send(embed = embed)


@bot.tree.command(name='review')
async def steam(interaction: discord.Interaction):
    """Retrieves a random steam review"""
    await interaction.response.defer()
    await asyncio.sleep(3)
    
    try:
        app_name = steamfunction.ss_steam_review()   
        embed = discord.Embed(title=app_name, color=discord.Color.gold())
        embed.set_image(url="attachment://steam_screenshot.png") 
        await interaction.followup.send(file=discord.File('SteamR/steam_screenshot.png'),
                                                embed=embed)
        
    except discord.DiscordException as e:
        embed = discord.Embed(title="Error", description="Please try again or review your argument/permissions",
                               color=discord.Color.red())
        await interaction.followup.send(embed=embed)
    #print(f"error {e}")


@bot.tree.command(name='anagram')
async def anagram(interaction: discord.Interaction, word: str):
    '''Attempts to find an anagram for your word'''
    if not re.match("^[a-zA-Z]+$", word):
        embed = discord.Embed(title="Error", description="Whatever you just pasted as argument is not a word.",	color=discord.Color.red())
        await interaction.response.send_message(embed=embed)
        return

    anagrams_list = find_anagrams(word)

    if anagrams_list:
        embed = discord.Embed(title=f"Anagrams of {word.capitalize()}", description=f"{', '.join(anagrams_list)}", color=discord.Color.green())
        await interaction.response.send_message(embed=embed)
    else:
        embed = discord.Embed(title="No anagrams found", description=f"No anagrams found for {word}.", color=discord.Colour.orange())
        await interaction.response.send_message(embed=embed)
        
        
@bot.tree.command(name='comic')
async def comic(interaction: discord.Interaction):
    '''Generates a random 3-panel comic'''
    await interaction.response.defer()
    await asyncio.sleep(3)
    try:
        attachment = comic_getter.comic()
        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url='attachment://comic_panel.png')
        await interaction.followup.send(embed=embed, file=discord.File('ComicF/comic_panel.png'))
    except discord.DiscordException as e:
        embed = discord.Embed(title="Error", description="Please try again or review your argument/permissions",
                               color=discord.Color.random())
        await interaction.followup.send(embed=embed)
        
        
        
@bot.tree.command(name='clearbot')
async def clearbot(interaction: discord.Interaction, amount: int):
    """Deletes the last (number) bot's messages.
    
     Parameters
    ----------
    amount: int
        Amount of messages to be deleted.
    """
    await interaction.response.defer()
    channel = interaction.channel
    deleted_count = 0

    async for message in channel.history(limit=None, oldest_first=False):
        if message.author == interaction.guild.me:
            await message.delete()
            deleted_count += 1
        if deleted_count >= amount:
            break
    embed = discord.Embed(title="Deleted messages", description=f"{deleted_count} messages deleted",	color=discord.Colour.blue())
    await interaction.followup.send(embed=embed)


@bot.tree.command(name='clear')
async def clear(interaction: discord.Interaction, amount: int, target_user: discord.User):
    """Deletes anyone's messages, if permission
    
    Parameters
    ----------
    target_user: discord.User 
        Select a user whose messages are to be deleted.
    amount: int
        Amount of messages to be deleted.
 
    """
    await interaction.response.defer()
    channel = interaction.channel
    deleted_count = 0

    if interaction.user.guild_permissions.manage_messages:
        async for message in channel.history(limit=None, oldest_first=False):
            if message.author.id == target_user.id:
                await message.delete()
                deleted_count += 1
            if deleted_count >= amount:
                break
        embed = discord.Embed(title="Deleted messages", description=f"{deleted_count} messages deleted", color=discord.Colour.blue())
        await interaction.followup.send(embed=embed)
    
    else:
        embed = discord.Embed(title="Not enough permissions", 
                               description=f"You don't have permissions to manage messages.",
                               color=discord.Color.orange())
        await interaction.followup.send(embed=embed)



@bot.tree.command(name='clearme')
async def clearme(interaction: discord.Interaction, amount: int):
    """Deletes your last (number) messages.
    amount: int
        Amount of messages to be deleted.   
    """
    await interaction.response.defer()
    channel = interaction.channel
    deleted_count = 0

    async for message in channel.history(limit=None, oldest_first=False):
        if message.author == interaction.user:
            await message.delete()
            deleted_count += 1
        if deleted_count >= amount:
            break
    embed = discord.Embed(title="Deleted messages", description=f"{deleted_count} messages deleted", color=discord.Colour.blue())
    await interaction.followup.send(embed=embed)
    
#capital letters and special characters on commands names raise errors


bot.run('TOKEN')

