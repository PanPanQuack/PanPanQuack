import discord
import asyncio
from discord.ext import commands
import safygiphy
import os

g = safygiphy.Giphy()
COR = 0x101010
client = commands.Bot(command_prefix='pq!', case_insensitive=True)
client.remove_command('help')

@client.event
async def on_ready():
    print('___' * 20)
    print(f'Online --> {client.user.name}')
    print(f'ID: {client.user.id}')
    print(f'Estou em {str(len(client.guilds))} Servidores')
    print(f'Total de Membros: {str(len(set(client.get_all_members())))}')
    print("https://discordapp.com/api/oauth2/authorize?client_id=" + str(client.user.id) + "&permissions=8&scope=bot")
    print('___' * 20)
    while True:
        await client.change_presence(activity=discord.Streaming(name="• Criadora: Brenda Leah 🐼", type=1, url='https://www.twitch.tv/sushuska'))
        await asyncio.sleep(20)

        await client.change_presence(activity=discord.Streaming(name="• Venha para o The Universe ! 🔮 \n https://discord.gg/wuXB5C9", type=1, url='https://www.twitch.tv/sushuska'))
        await asyncio.sleep(30)

        await client.change_presence(activity=discord.Streaming(name="• A Bre é a melhor, Muuuuh ! 💖", type=1, url='https://www.twitch.tv/sushuska'))
        await asyncio.sleep(40)

        await client.change_presence(activity=discord.Streaming(name="• Muuuuuuh ! 🐮", type=1, url='https://www.twitch.tv/sushuska'))
        await asyncio.sleep(50)

@client.command()
async def setar(ctx, *, img=None):
    await ctx.message.delete()
    if ctx.author.guild_permissions.administrator:
        if img is None:
            await ctx.send('**Você não pode deixar a imagem em branco !**')
        else:
            global set_1
            set_1 = img
            embedsetar = discord.Embed(title='<:frame_photo:462594078899568651> `IMAGEM SETADA !`', description='`Agora prossiga com o comando: "pq!msg".`', color=0x22eb7b)
            embedsetar.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await ctx.send(embed=embedsetar)
    else:
        await ctx.send('**Você não tem permissão para usar este comando !**')

@client.command()
async def msg(ctx, *, msg=None):
    await ctx.message.delete()
    if msg is None:
        await ctx.send('**Você não pode deixar o texto em branco !**')
    else:
        if ctx.author.guild_permissions.administrator:
            embed2 = discord.Embed(title='⏱ *ENVIANDO MENSAGEM...*', description='🔹 `MENSAGEM ESCOLHIDA:`\n' + (msg), color=0x7459ff)
            embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await ctx.send(embed=embed2)
            x = ctx.guild.members
            s = 0
            for member in x:
                embed1 = discord.Embed(title="", url="", color=0x5c02db, description='``Ei`` <@!{}>, ``tenho uma mensagem pra você !`` \n {}'.format(member.id, msg))
                embed1.set_image(url=set_1)
                embed1.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
                try:
                    await member.send(embed=embed1)
                    print(f'{member.name} | {s}')
                    s += 1
                except:
                    pass
            print('\nAviso enviado para {} membros de {}'.format(s, len(x)))
            embed2 = discord.Embed(title='<:yeeeah:527144209011048458> MENSAGEM ENVIADA !', description="<:pandaadmirado:532592405300510720> `SUCESSO !` \n\n *Mensagem Enviada com Sucesso para Todos os Membros do Servidor !*", color=COR)
            embed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await ctx.send(embed=embed2)
        else:
            embed3 = discord.Embed(name='🚫 N E G A D O ❗', description='**Você não tem permissão para usar este comando !**', color=COR)
            await ctx.send(embed=embed3)


client.run(str(os.environ.get('TOKEN')))
