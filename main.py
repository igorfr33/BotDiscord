import discord
from discord.ext import commands
import requests

client = commands.Bot(command_prefix = ">", case_insensitive = True)

@client.event
async def on_ready():
  print('Entramos como {0.user}'.format(client))

  @client.command()
  async def ola(ctx):
    await ctx.send(f'Olá,{ctx.author} ')

  @client.command()
  async def PVU(ctx):
    request = requests.get('https://api.coingecko.com/api/v3/coins/plant-vs-undead-token'.format())
    pvu_data = request.json()
    await ctx.send('Preco de Venda em Real: {}'.format(pvu_data['market_data']['current_price']['brl']))

client.run('ODgwNDI4NzEzNTE3MzkxOTMz.YSeJIg.WVSeU9KfkI2CW3XVm3ekVf-wLHU')