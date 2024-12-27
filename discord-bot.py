import os 
import discord
from maid_service_LLM import maid_service

# client是跟discord連接，intents是要求機器人的權限
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

client = discord.Client(intents=intents)

maid = maid_service()


@client.event
# 當機器人完成啟動
async def on_ready():
    print(f"目前登入身份 --> {client.user},{client.user.mention}")


@client.event
async def on_guild_join(guild: discord.Guild):
    response = maid.request(
        author="everyone", message="向 Discord 伺服器中的大家自我介紹，並邀請他們使用 <@1321447514628689980> 標記你與你聊天，不用介紹你的外貌")
    await guild.text_channels[0].send(response)


@client.event
# 當頻道有新訊息
async def on_message(message):
    # 排除機器人本身的訊息，避免無限循環
    if message.author == client.user:
        return

    # 自動回寄
    if message.content in {"幾", "今幾"}:
        await message.channel.send("寄")

    # 如果機器人被 tag 則調用 LLM 進行回答
    if client.user.mentioned_in(message):
        response = maid.request(
            author=message.author, message=message.content.replace("<@1321447514628689980>", ""))
        await message.channel.send(response)


client.run(
    os.getenv("DISCORD_BOT_TOKEN"))
