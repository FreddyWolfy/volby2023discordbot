# Made by FreddyWolfy - https://github.com/FreddyWolfy
# Licensed under GNU General Public License v3.0
# Uses StringProgressBar by Sparker-99 - https://github.com/Sparker-99/string-progressbar



from urllib.request import urlopen
import xml.etree.ElementTree as ET
import os
import discord
from discord.ext import tasks
from StringProgressBar import progressBar
import datetime



intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
from discord.ext import commands

discordtoken = "MTA2MzkyODU5NTc2NjA2NzIzMA.Gzvv2A.InRgc44e3ZlsWR-hhv_GGzOBtthKCp7HKOa8n8"

embed = ""


def stahnidata():
    global embed
    pocetkandidatu = 0
    kandidat = []
    druhekolo = False

    today = datetime.date.today()
    future = datetime.date(2023,1,27)
    diff = future - today
    
    
    try:
        tree = ET.parse(urlopen("https://www.volby.cz/pls/prez2023/vysledky"))
        root = tree.getroot()
        for i in root.findall("{http://www.volby.cz/prezident/}CR/"):
            if i.tag == "{http://www.volby.cz/prezident/}KANDIDAT":
                if "HLASY_PROC_2KOLO" in i.attrib:
                    druhekolo = True
                else:
                    pass
        
        if druhekolo == True:
            for n in root.findall("{http://www.volby.cz/prezident/}CR/"):
                if n.tag == "{http://www.volby.cz/prezident/}KANDIDAT":
                    if "HLASY_PROC_2KOLO" in n.attrib:
                        pocetkandidatu += 1
                        kandidat.append([n.attrib["JMENO"],n.attrib["PRIJMENI"],n.attrib["HLASY_PROC_2KOLO"]])
                    else:
                        pass
        
        if druhekolo == False:
            for a in root.findall("{http://www.volby.cz/prezident/}CR/"):
                if a.tag == "{http://www.volby.cz/prezident/}KANDIDAT":
                    pocetkandidatu += 1
                    kandidat.append([a.attrib["JMENO"],a.attrib["PRIJMENI"],a.attrib["HLASY_PROC_1KOLO"]])


        for i in range(0,pocetkandidatu):
            bardata = progressBar.splitBar(100, int(float(kandidat[i][2])), size= 10,slider="🟥",line= "⬜" )
            kandidat[i].append(bardata[0])
        
       
        def razeniproc(elem):
            return int(float(elem[2]))        
        
        kandidat.sort(key=razeniproc ,reverse=True)

        embed=discord.Embed(color=0xff0000) 
        embed.add_field(name="Výsledky voleb 2023", value="", inline=False)
        embed.set_footer(text="Zdroj dat: ČSÚ - Programmed by FreddyWolfy")
         
        for i in range(0,pocetkandidatu):
            jmeno = kandidat[i][0] + " " + kandidat[i][1]
            procenta = kandidat[i][3] + " " + kandidat[i][2] + "%"
            embed.add_field(name=jmeno, value=procenta, inline=False)
        
        if diff.days >= 0:
            embed.add_field(name="Druhé kolo voleb!", value="Zbývá " + str(diff.days) + " dní do 27.ledna", inline=False)
        
        if diff.days == -1:
            stahnidata.akt = 300
        else:
            stahnidata.akt = 3600
        
        if diff.days == -2:
            stahnidata.akt = 50000
        
        
   
    except Exception as l:
        print("Stahovani selhalo, zkousim to znovu " + str(l))
        stahnidata()

    return diff.days

rozdildnu = stahnidata()


client.channel_id = 0


#Discord integrace
client = commands.Bot(command_prefix='.', intents=intents)
client.firsmess = 0
client.idecko = 0
client.dnidovoleb = rozdildnu
client.volbyupozorneni = 0


@client.event
async def on_ready():
    print('bot ready')
    

@client.command()
async def hello(ctx):
    client.channel_id = ctx.channel.id
    await ctx.send('Vítejte, aktualizace o volbach se budou nyní posílat v tomto channelu')
    stahnidata()
    print("Aktualizace nastavena na :" + str(stahnidata.akt))
    myLoop.start()

@tasks.loop(seconds = stahnidata.akt) 
async def myLoop():
    channel = client.get_channel(client.channel_id)
    if client.firsmess == 0:
        message = await channel.send(embed=embed)
        client.idecko = message.id
        print(client.idecko)
        client.firsmess = 1
    
    if client.dnidovoleb == 0 and client.volbyupozorneni == 0:
        await channel.send("@everyone Dnes a zítra jsou volby! Nezapomeňte na ně prosím! Dnes od 14:00 do 22:00 a zítra od 8:00 do 14:00")   
        client.volbyupozorneni = 1  

    msg = await channel.fetch_message(client.idecko)
    await msg.edit(embed=embed)
    print("Probehla aktualizace")
    stahnidata()


    



client.run(discordtoken)