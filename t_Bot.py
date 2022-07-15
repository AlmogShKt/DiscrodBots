import os
import discord
import requests
import json
from Send_grade import getLastGrade
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

def get_qoute():
    respone = requests.get("https://zenquotes.io/api/random")
    js_data = json.loads(respone.text)
    quote = js_data[0]['q']
    return quote


client = discord.Client()


@client.event
async  def on_ready():
    print(f'We have logged in as {client.user}')
botFeatures = [
    '$hello - Just say Hi 😀🔥' ,
    '$getLastGrade - get the last grade 📚'
]
@client.event
async def on_message(msg):
    if msg.author == client.user:
        return

    if msg.content.startswith('$ShowAll'):

        for task in botFeatures:
            await msg.channel.send(task)
            print(task)

    if msg.content.startswith('$hello'):
        await msg.channel.send("Hello Almog! Im your Grade bot 🤖🦾, I will send you updates for your grade! Good luck!")
        tstmsg()

    if msg.content.startswith('$getLastGrade'):
        grade = getLastGrade()
        await msg.channel.send(grade)

    if msg.content.startswith('$Quote'):
        await msg.channel.send(get_qoute())

def tstmsg():
    client.get_channel()
    on_message('$Quote')


client.run(TOKEN)
