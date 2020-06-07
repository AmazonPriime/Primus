import functions as fn

key = "INSERT KEY HERE"

prefix = "INSERT COMMAND PREFIX HERE"

status = "INSERT BOT STATUS HERE"

calc_functions = {
    '+' : lambda l: l[0] + l[1],
    '-' : lambda l: l[0] - l[1],
    '*' : lambda l: l[0] * l[1],
    '/' : lambda l: l[0] / l[1],
}

calc_list = list(calc_functions.keys())

# 'fn' - function associated with command
# 'name' - name of the command
# 'text' - the text that appears on the help page
# 'usage' - describes the arguments taken (empty string if no arguments required)
commands = {
    'help' : {'fn' : fn.help, 'name' : 'help', 'text' : 'Help command to explain the commands of the bot.', 'usage' : ''},
    'clear' : {'fn' : fn.clear, 'name' : 'clear', 'text' : '[Admin] Used to clear the chat of the channel command is executed in.', 'usage' : ''},
    'calc' : {'fn' : fn.calc, 'name' : 'calc', 'text' : 'Used to calculate the result of two numbers.', 'usage' : '<num> {} <num>'.format(calc_list)},
    'textemoji' : {'fn' : fn.textemoji, 'name' : 'textemoji', 'text' : 'Used to convert text to emojis. Supports [A-Z] [0-9]', 'usage' : '<text>'},
    'history' : {'fn' : fn.history, 'name' : 'history', 'text' : '[Admin] Used to get the message history of the channel.', 'usage' : '<num>'},
}

symbols = {
    '0' : ':zero:', '1': ':one:', '2': ':two:', '3': ':three:', '4': ':four:',
    '5': ':five:', '6': ':six:', '7': ':seven:', '8': ':eight:', '9': ':nine:',

    'A': ':regional_indicator_a:', 'B': ':regional_indicator_b:', 'C': ':regional_indicator_c:', 'D': ':regional_indicator_d:',
    'E': ':regional_indicator_e:', 'F': ':regional_indicator_f:', 'G': ':regional_indicator_g:', 'H': ':regional_indicator_h:',
    'I': ':regional_indicator_i:', 'J': ':regional_indicator_j:', 'K': ':regional_indicator_k:', 'L': ':regional_indicator_l:',
    'M': ':regional_indicator_m:', 'N': ':regional_indicator_n:', 'O': ':regional_indicator_o:', 'P': ':regional_indicator_p:',
    'Q': ':regional_indicator_q:', 'R': ':regional_indicator_r:', 'S': ':regional_indicator_s:', 'T': ':regional_indicator_t:',
    'U': ':regional_indicator_u:', 'V': ':regional_indicator_v:', 'W': ':regional_indicator_w:', 'X': ':regional_indicator_x:',
    'Y': ':regional_indicator_y:', 'Z': ':regional_indicator_z:',

    '!' : ':exclamation:', '?' : ':question:',
}
