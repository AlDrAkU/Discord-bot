from discord.ext.commands import Bot
import discord.object
import random
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))




BOT_PREFIX = "!"
TOKEN = "NDIyNjk4NDUzNDE2NjczMjgw.DaKg_Q.mcOcI7cSPnXOIGiMOC0UM9Rmh0I"
"""client = discord.Client() """
client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='cn', description="Generates a random Chuck Norris fact",
                aliases=['chucknorris'],
                pass_context=True)
async def cn(context):
    txt_file = open(os.path.join(__location__,"responses.txt"),"r",encoding='utf8')
    possible_responses = txt_file.read().split(';')
    
    await context.send(random.choice(possible_responses).replace('"',""))

@client.command(name='8ball',
                description="Answers a yes/no question.",
                brief="Answers from the beyond.",
                aliases=['eight_ball', 'eightball', '8-ball'],
                pass_context=True)
async def eight_ball(context):
    possible_responses = [
        'That is a resounding no',
        'It is not looking likely',
        'Too hard to tell',
        'It is quite possible',
        'Definitely',
    ]
    await context.send(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith('https://imgur.com'):
        msg = '{0.author.mention}'.format(message) + ' ' + message.content
        channel = discord.utils.get(client.get_all_channels(), name='fun-stuff')
        await  channel.send(msg)
        await  message.delete()

    elif message.content.startswith('https://i.imgur.com'):
        msg = '{0.author.mention}'.format(message) + ' ' + message.content
        channel = discord.utils.get(client.get_all_channels(), name='fun-stuff')
        await  channel.send(msg)
        await message.delete()

    elif message.content.startswith('https://www.youtube.com'):
        msg =  '{0.author.mention}'.format(message) +' ' + message.content
        channel = discord.utils.get(client.get_all_channels(), name='fun-stuff')
        await  channel.send(msg)
        await message.delete()

    elif message.content.startswith('https://en.wikipedia.org'):
        msg =  '{0.author.mention}'.format(message) +' ' + message.content
        channel = discord.utils.get(client.get_all_channels(), name='fun-stuff')
        await  channel.send(msg)
        await message.delete()

    elif message.content.startswith('https://www.wowhead.com'):
        msg =  '{0.author.mention}'.format(message) +' ' + message.content
        channel = discord.utils.get(client.get_all_channels(), name='wow-stuff')
        await  channel.send(msg)
        await message.delete()


    await client.process_commands(message)


@client.event
async def on_ready():
    print('Logged in as ' + client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)


