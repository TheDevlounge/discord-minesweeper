import json
import sys
from random import randint

import discord
from discord.ext.commands import Bot, bot

from generator import generate, to_dc_spoilers

bot = Bot(description="Minesweeper", command_prefix="mine ", pm_help=False)


@bot.event
async def on_ready():
    # print('Logged in as ' + bot.user.name + ' (ID:' + bot.user.id + ') | Connected to ' + str(
    #     len(bot.servers)) + ' servers | Connected to ' + str(len(set(bot.get_all_members()))) + ' users')
    # print('--------')
    print('Use this link to invite {}:'.format(bot.user.name))
    print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=0'.format(bot.user.id))
    print('--------')

    #return await bot.change_presence(game=discord.Game(name='With human lives'))

def getErr(e):
    str0 = "{} at line {} [{}]".format(str(e), sys.exc_info()[-1].tb_lineno, type(e).__name__)

    return str0


bot.remove_command('help')
@bot.command(pass_context=True)
async def help(ctx, *args):
    _help = """
    Discord minesweeper

    **Player commands**
    `mine play [x] [y] [M]` - creates a new field of X rows and Y columns and M mines. Default field is 9 x 9 with 10 mines
    """
    return await bot.say(_help)


@bot.command(pass_context=True)
async def play(ctx, x:int=9,y:int=9,m:int=10, *args):
    try:
        grid = generate(int(x),int(y),int(m))

        str0 = to_dc_spoilers(grid)
        str0 = ctx.message.author.mention + " here is your mine field :triangular_flag_on_post: \n" + str0

        await bot.say(str0)


    except Exception as e:
        getErr(e)


if __name__ == "__main__":
    with open('pw.json') as fh:
        conf = json.load(fh)
    bot.run(conf['secret'])
