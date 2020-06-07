import discord, config

# command to provide information about the commands
async def help(message, *argv):
    help_message = discord.Embed(title = "Commands Help", colour = 0x00fdff)
    for cmd in config.commands:
        value = "{}\n`{}{} {}`".format(config.commands[cmd]['text'], config.prefix, config.commands[cmd]['name'], config.commands[cmd]['usage'])
        help_message.add_field(name = config.commands[cmd]['name'], value = value, inline = False)
    await message.channel.send(embed = help_message)

# command clears the messages from the channel
async def clear(message, *argv):
    if message.author.guild_permissions.administrator:
        await message.channel.purge()
        await message.channel.send("All messages have been removed.")
    else:
        await message.channel.send("You don't seem to be an administrator.")

# command to calculate the result of two numbers
async def calc(message, *argv):
    try:
        operands, operator = [float(argv[0][0]), float(argv[0][2])], argv[0][1]
        msg = "{:.2f} {} {:.2f}".format(operands[0], operator, operands[1])
        if operator in config.calc_functions:
            await message.channel.send(msg + " = {:.2f}".format(config.calc_functions[operator](operands)))
        else:
            await message.channel.send("The operator {} is not supported.".format(operator))
    except:
        await message.channel.send("Make sure your arguments are correct.\nCommand usage: **{}calc <num> {} <num>**".format(config.prefix, list(config.calc_functions.keys())))

# command to convert text to discord emoji symbols
async def textemoji(message, *argv):
    try:
        msg = ""
        for char in " ".join(argv[0]):
            if char.upper() in config.symbols:
                msg += config.symbols[char.upper()]
            elif char == " ":
                msg += "  "
        if len(msg) > 0:
            await message.channel.send(msg)
            await message.delete()
        else:
            await message.channel.send("Cannot convert an empty message. Make sure to use valid symbols. [A-Z] [0-9]")
    except:
        print("Something went wrong.")

# command to get the history of the channel and store in file <guild>.<channel id>.txt
async def history(message, *argv):
    if message.author.guild_permissions.administrator:
        try:
            num, msg = int(argv[0][0]), ""
            length = await message.channel.history(limit = num).flatten()
            num = len(length) - 1 if num > len(length) else num
            async for message in message.channel.history(limit = num):
                msg += "**{0.author}**: '{0.clean_content}'\n".format(message)
            await message.author.send("{}".format(msg))
            await message.channel.send("Sent a DM to {} with the messages.".format(message.author))
        except:
            await message.channel.send("Make sure your arguments are correct.\nCommand usage: **{}history <num>**".format(config.prefix))
    else:
        await message.channel.send("You don't seem to be an administrator.")
