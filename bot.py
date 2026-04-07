import discord
from discord.ext import commands
import json
import asyncio
import aiohttp

CONFIG_FILE = "config.json"

# Load config
def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

config = load_config()

# Bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="cdv", intents=intents, help_command=None)
user_memory = {}
active_channel_id = config.get("channel_id")  # Load saved channel

@bot.event
async def on_ready():
    print(f"Cng ng Vit ")
    print(f"Logged in as {bot.user}!!")

    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name="Cng ng Vit "),
        status=discord.Status.idle
    )

@bot.command()
@commands.has_permissions(administrator=True)
async def setup(ctx):
    global active_channel_id
    active_channel_id = ctx.channel.id
    config["channel_id"] = active_channel_id
    save_config(config)
    await ctx.send(f" | y hin l knh ang hot ng  tr chuyn vi bot.: <#{active_channel_id}>")

@bot.command(name="unsetup")
@commands.has_permissions(administrator=True)
async def unsetup(ctx):
    global active_channel_id
    if "channel_id" in config:
        removed_channel = config.pop("channel_id", None)
        save_config(config)
        active_channel_id = None
        await ctx.send(f"Thit lp knh  b xa: <#{removed_channel}>")
    else:
        await ctx.send(" | Khng tm thy knh thit lp no  xa.")

@bot.command(name="help")
async def custom_help(ctx):
    help_text = "__**AI BOT CMDS :**__\n" \
                "> **`cdvsetup`** - chnh bot chat  knh \n" \
                "> **`cdvunsetup`** - xa bot khi knh \n" \
                "> **`cdvclearmemory`** - xa b nh bot\n" \
                "> **`cdvhelp`** - hin th lnh h tr"
    await ctx.send(help_text)

@bot.command(name="clearmemory")
async def clear_memory(ctx):
    user_id = str(ctx.author.id)
    if user_id in user_memory:
        del user_memory[user_id]
    await ctx.send(" | B nh ca bn  c xa!")

@bot.event
async def on_message(message):
    global active_channel_id

    if message.author.bot:
        return

    await bot.process_commands(message)

    # Only respond in the designated channel
    if active_channel_id is None or message.channel.id != active_channel_id:
        return

    if message.content.startswith("-ai"):
        return

    await message.channel.typing()

    user_id = str(message.author.id)
    user_memory.setdefault(user_id, [])
    user_memory[user_id].append({"role": "user", "content": message.content})

    messages = [{"role": "system", "content": config["system_context"]}] + user_memory[user_id]

    try:
        async with aiohttp.ClientSession() as session:
            headers = {
                "Authorization": f"Bearer {config['api_key']}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": config["model"],
                "messages": messages
            }
            async with session.post(f"{config['api_base']}/chat/completions", headers=headers, json=payload) as resp:
                if resp.status != 200:
                    error_detail = await resp.text()
                    print(f"[API ERROR] {resp.status}: {error_detail}")
                    await message.reply(config.get("error_message", "❌ | API Error, try again later."))
                    return
                response = await resp.json()
                reply = response["choices"][0]["message"]["content"]
                user_memory[user_id].append({"role": "assistant", "content": reply})
                await message.reply(reply)
    except Exception as e:
        await message.reply(config.get("error_message", " | Li ni b  xy ra."))
        print(f"[ERROR] {e}")

bot.run("<YOUR_DISCORD_BOT_TOKEN>")