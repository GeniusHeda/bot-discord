import discord
from discord.ext import commands, tasks
import random
from datetime import datetime

bot = commands.Bot(command_prefix="!")

secondes = ["00", "01", "02", "03", "04"]

@bot.event
async def on_ready():
    print("Ready !")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("donner des fréquences "))
    changeFreq.start()


@tasks.loop(seconds=5)
async def changeFreq():
    freq = random.randint(100, 800)
    chanel = bot.get_channel(635220688889708574)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    hour = current_time[0] + current_time[1]
    min = current_time[3] + current_time[4]
    sec = current_time[6] + current_time[7]



    if hour == "22" and min == "30" and sec in secondes:
        print("send")
        embed = discord.Embed(
            title="LSPD Fréquence:",
            description=f"{freq}Hz ",
            colour=discord.Colour.blue())
        await chanel.send("𝙉𝙤𝙪𝙫𝙚𝙡𝙡𝙚 𝙛𝙧𝙚́𝙦𝙪𝙚𝙣𝙘𝙚 𝙍𝙖𝙙𝙞𝙤 @here")
        await chanel.send(embed=embed)




bot.run("Nzg2NzA2MTI3ODk4Mjc5OTY3.X9KTLQ.5pMDbAnrT8Qtc2oHiHKlID2cVPU")
