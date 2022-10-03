import disnake
import datetime
from disnake.ext import commands
from disnake.enums import ButtonStyle, TextInputStyle

class cog_events_event(commands.Cog):
    def __init__(self, bot: commands.Bot(intents = disnake.Intents.all(), command_prefix = 'test!')):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):

        if member.guild.id == 943924240795709460:

            embed = disnake.Embed(title = 'Зашел', description=f'{member.mention} | **{member.name}**({member.id}) зашел на сервер!', color = disnake.Color.green())
            embed.add_field(name=f'<:zashel:979821014097739886> Создал аккаунт', value=f'```yaml\n{member.created_at.strftime("%d.%m.%Y")}```')
            embed.set_thumbnail(url=member.display_avatar.url)
            await self.bot.get_channel(1006910856061259866).send(embed = embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):

        if member.guild.id == 943924240795709460:

            embed = disnake.Embed(title = 'Вышел', description=f'{member.mention} | **{member.name}**({member.id}) вышел из сервера!', color = disnake.Color.red())
            embed.add_field(name=f'<:zashel:979821014097739886> Создал аккаунт', value=f'```yaml\n{member.created_at.strftime("%d.%m.%Y")}```')
            embed.set_thumbnail(url=member.display_avatar.url)
            await self.bot.get_channel(1006910856061259866).send(embed = embed)

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.guild.id == 943924240795709460:
            try:
                if before.roles != after.roles:
                    async for event in before.guild.audit_logs(limit=1, action=disnake.AuditLogAction.member_role_update):
                        for role in before.roles:
                            embed = disnake.Embed(description = f'**Обновление ролей пользователя - {before.mention}**', color = 3092790)
                            embed.add_field(name = 'Модератор', value = f'{event.user}\n**ID**: {event.user.id}')
                            embed.add_field(name = 'Роли до', value=" ".join([r.name for r in before.roles][1:]), inline=False)
                            embed.add_field(name = 'Роли после', value=" ".join([r.name for r in after.roles][1:]), inline=False)
                            embed.add_field(name = 'Измененные роли', value = role)
                            embed.set_thumbnail(url = event.user.display_avatar.url)
                            return await self.bot.get_channel(1006914904156029080).send(embed=embed)
                        for role in after.roles:
                            embed = disnake.Embed(description = f'**Обновление ролей пользователя - {after.mention}**', color = 3092790)
                            embed.add_field(name = 'Модератор', value = f'{event.user}\n**ID**: {event.user.id}')
                            embed.add_field(name = 'Роли до', value=" ".join([r.name for r in after.roles][1:]), inline=False)
                            embed.add_field(name = 'Роли после', value=" ".join([r.name for r in after.roles][1:]), inline=False)
                            embed.add_field(name = 'Измененные роли', value = role)
                            embed.set_thumbnail(url = event.user.display_avatar.url)
                            return await self.bot.get_channel(1006914904156029080).send(embed=embed)
            except: 
                pass

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if member.guild.id == 943924240795709460:
            if after.channel and after.channel != before.channel:
                embed = disnake.Embed(description = f"**Зашёл в голосовой канал - {member.mention}**", color = disnake.Color.green())
                embed.add_field(name = 'Пользователь', value = f'{member}\n**ID**: {member.id}')
                embed.add_field(name = 'Канал', value = f"<#{after.channel.id}>\n{after.channel}\n**ID:** {after.channel.id}")
                embed.set_thumbnail(url = member.display_avatar.url)
                await self.bot.get_channel(1005360297432842240).send(embed = embed)
            if before.channel and after.channel != before.channel:
                embed = disnake.Embed(description = f"**Вышел из голосового канала - {member.mention}**", color = disnake.Color.red())
                embed.add_field(name = 'Пользователь', value = f'{member}\n**ID**: {member.id}')
                embed.add_field(name = 'Канал', value = f"<#{before.channel.id}>\n{before.channel}\n**ID:** {before.channel.id}")
                embed.set_thumbnail(url = member.display_avatar.url)
                await self.bot.get_channel(1005360297432842240).send(embed = embed)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        try:
            if message.guild.id == 943924240795709460:
                if message.author.id == 464148182410985483: return
                embed = disnake.Embed(description = f'Сообщение **было удалено** от пользователя {message.author.mention} удалено в канале <#{message.channel.id}>', color = disnake.Color.red())
                embed.add_field(name = 'Содержимое сообщения', value = message.content).set_footer(text = f'Author: {message.author.id} | Message ID: {message.id}')
                embed.set_author(name = 'Удаление сообщения')
                try: 
                    await self.bot.get_channel(1005360335902998618).send(embed = embed)
                except: 
                    pass
        except:
            pass

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        try:
            if before.guild.id == 943924240795709460:
                if before.author.bot:
                    return
                embed = disnake.Embed(title=f"{after.guild.name}", description=f":pencil2: **Сообщение от {before.author.mention} изменено в - {before.channel.mention}**\n**Старое сообщение -**\n ```\n {before.content}\n```\n**Новое сообщение -**\n```\n{after.content}\n```", color = 0x40cc88)
                embed.set_footer(text = after.guild.name).set_thumbnail(url = after.guild.icon_url)
                await self.bot.get_channel(1005360335902998618).send(embed = embed)
        except:
            pass

    @commands.Cog.listener()
    async def on_member_ban(self, guild, member):
        if guild.id == 943924240795709460:
            logs = await guild.audit_logs(limit = 1, action = disnake.AuditLogAction.ban).flatten()
            logs = logs[0]
            embed = disnake.Embed(title = 'Бан', description = f"{logs.target} был забанен {logs.user} (время {logs.created_at}), по причине {logs.reason}", color = disnake.Color.red())
            embed.set_thumbnail(url = logs.user.display_avatar.url)
            if logs.target == member: 
                await self.bot.get_channel(1006923620393685063).send(embed = embed)

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member):
        if guild.id == 943924240795709460:
            logs = await guild.audit_logs(limit = 1, action = disnake.AuditLogAction.unban).flatten()
            logs = logs[0]
            if logs.target == member: 
                embed = disnake.Embed(title = 'Бан', description = f"{logs.target} был разбанен {logs.user} (время {logs.created_at}), по причине {logs.reason}", color = disnake.Color.green())
                embed.set_thumbnail(url = logs.user.display_avatar.url)
                await self.bot.get_channel(1006923620393685063).send(embed = embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        if channel.guild.id == 943924240795709460:
            async for entry in channel.guild.audit_logs(limit = 1, action = disnake.AuditLogAction.channel_delete):
                embed = disnake.Embed(title = "Удаление Канала", description = f"{entry.user.mention} | {entry.user} | **ID: {entry.user.id}** Удалил **канал** {channel}", color = disnake.Color.red())
                embed.set_thumbnail(url = entry.user.display_avatar.url)
                await self.bot.get_channel(1006915082829176964).send(embed = embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        if channel.guild.id == 943924240795709460:
            async for entry in channel.guild.audit_logs(limit = 1, action = disnake.AuditLogAction.channel_create):
                embed = disnake.Embed(title = "Создание Канала", description = f"{entry.user.mention} | {entry.user} | **ID: {entry.user.id}** Создал **канал** {channel}", color = disnake.Color.green())
                embed.set_thumbnail(url = entry.user.display_avatar.url)
                await self.bot.get_channel(1006915082829176964).send(embed = embed)

    @commands.Cog.listener()
    async def on_guild_role_delete(self, role):
        if role.guild.id == 943924240795709460:
            async for entry in role.guild.audit_logs(limit = 1, action = disnake.AuditLogAction.role_delete):
                embed = disnake.Embed(title = "Удаление Роли", description = f"{entry.user.mention} | {entry.user} | **ID: {entry.user.id}** Удалил **роль** {role}", color = disnake.Color.red())
                embed.set_thumbnail(url = entry.user.display_avatar.url)
                await self.bot.get_channel(1006914904156029080).send(embed = embed)

    @commands.Cog.listener()
    async def on_guild_role_create(self, role):
        if role.guild.id == 943924240795709460:
            async for entry in role.guild.audit_logs(limit = 1, action = disnake.AuditLogAction.role_create):
                embed = disnake.Embed(title = "Создание Роли", description = f"{entry.user.mention} | {entry.user} | **ID: {entry.user.id}** Создал **роль** {role}", color = disnake.Color.green())
                embed.set_thumbnail(url = entry.user.display_avatar.url)
                await self.bot.get_channel(1006914904156029080).send(embed = embed)

def setup(bot): 
    bot.add_cog(cog_events_event(bot))
