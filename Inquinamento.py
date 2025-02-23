import discord
from discord.ext import commands
import os, random

intents = discord.Intents.default() #permette di attivare le funzioni di base
intents.message_content = True #permette al bot di leggere i contenuto dei messaggi
bot = commands.Bot(command_prefix='$', intents=intents) #il bot risponde ai comandi che iniziano con $

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def mem(ctx):
    img_name= random.choice(os.listdir('immagini_inquinamento'))
    with open(f'immagini/{img_name}', 'rb') as f:
        picture = discord.File(f)# converte l'immagine in un formato che discord riesce a inviare
    await ctx.send(file=picture)

bot.run('718d2919c7cdc3f18e8daf4f0427445eba8d22f5bdd5144864dde16cf461de84')
