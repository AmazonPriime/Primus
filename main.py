import discord, config
from functions import *

class MyClient(discord.Client):
    # sets sets bot's presence when bot is online
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(activity = discord.Game(name = config.status))

    # executes when message is received
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))
        # checks if the message is a possible command
        if message.content.startswith(config.prefix) and message.author != self.user:
            # splits message into arguments and checks if the message is a command
            args = message.content.split(" ")
            if args[0][1:] in config.commands:
                # executes the command and passes the rest of the arguments to the function
                await config.commands[args[0][1:]]['fn'](message, args[1:])

client = MyClient()
client.run(config.key)
