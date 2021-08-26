from discord import channel
from discord.ext import commands, tasks
import requests

client = commands.Bot(command_prefix = ">", case_insensitive = True)

@client.event
async def on_ready():
  print('Entramos como {0.user}'.format(client))

  @client.command()
  async def ola(ctx):
    await ctx.send(f'Olá,{ctx.author} ')

    @tasks.loop(minutes = 1)
    async def cotacoes():
      
      requestPUV = requests.get('https://api.coingecko.com/api/v3/coins/plant-vs-undead-token'.format())
      request2CYT = requests.get('https://api.coingecko.com/api/v3/coins/coinary-token'.format())
      requestCCAR = requests.get('https://api.coingecko.com/api/v3/coins/cryptocars'.format())

      pvu_data = requestPUV.json()
      cyt_data = request2CYT.json()
      ccar_data = requestCCAR.json()

      canal = await client.get_channel(id)

      await canal.send('PVU - R$: {}'.format(pvu_data['market_data']['current_price']['brl']))
      await canal.send('CYT - R$: {}'.format(cyt_data['market_data']['current_price']['brl']))
      await canal.send('CCAR - R$ {}'.format(ccar_data['market_data']['current_price']['brl']))

      client.run('ODgwNDI4NzEzNTE3MzkxOTMz.YSeJIg.WVSeU9KfkI2CW3XVm3ekVf-wLHU')