import discord
import os
import random
import logging
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("discord-bot")

# Set up intents
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

# Bot setup
bot = commands.Bot(command_prefix="$", intents=intents)

# Overwrite help command
bot.remove_command('help')

def contains_numbers(args):
    return any(arg.isdigit() for arg in args)

# Help message and playful personality
cm_1 = '`$sort <space> a b c` = Arranges in ascending order 🔢'
cm_2 = '`$flip <space> a b c` = Reverses input characters 🔁'
cm_3 = '`$flipsort <space> a b c` = Arranges in descending order 🔄'
cm_4 = '`$count <space> a b c` = Displays the number of input characters 📊'
cm_5 = '`$shuffle <space> a b c` = Shuffles input characters 🎲'

help_message = discord.Embed(
    title="✨ Command Help ✨",
    description="Here's a list of what I can do for you! Use them wisely, adventurer! 🐱",
    color=discord.Color.blue(),
)
help_message.add_field(name="Commands:", value=f"{cm_1}\n{cm_2}\n{cm_3}\n{cm_4}\n{cm_5}", inline=False)
help_message.set_footer(text="Need assistance? Use $help anytime! 🔧")

hello_messages = [
    "Hi there, {user}! 😊",
    "Greetings, {user}! 👋",
    "Howdy, {user}! 🤠",
    "'Sup, {user}? 😎",
    "Yo, {user}! 🙌"
]
easter_egg_message = "Do you know Cil? Cil made me! 🤖"

# Commands
@bot.command(name="help", description="Shows a list of all available commands.")
async def help_command(ctx):
    """Displays the help message."""
    await ctx.send(embed=help_message)

@bot.command(name="sort")
async def sort_command(ctx, *args):
    """Sorts input arguments in ascending order."""
    async with ctx.typing():
        if args:
            if contains_numbers(args):
                await ctx.send("⚠️ | Sorting numbers is not supported yet. Please provide non-numeric inputs.")
            else:
                sorted_args = sorted(args)
                await ctx.send(f"🔢 | Sorted result: `{' '.join(sorted_args)}`")
        else:
            await ctx.send("🔢 | Oops! Please provide some items to sort.")

@bot.command(name="flipsort")
async def flipsort_command(ctx, *args):
    """Sorts input arguments in descending order."""
    async with ctx.typing():
        if args:
            if contains_numbers(args):
                await ctx.send("⚠️ | Flipsorting numbers is not supported yet. Please provide non-numeric inputs.")
            else:
                sorted_args = sorted(args, reverse=True)
                await ctx.send(f"🔄 | Flipsorted result: `{' '.join(sorted_args)}`")
        else:
            await ctx.send("🔄 | Oops! Please provide some items to flipsort.")

@bot.command(name="flip")
async def flip_command(ctx, *args):
    """Reverses the order of input arguments."""
    async with ctx.typing():
        if args:
            if contains_numbers(args):
                await ctx.send("⚠️ | Flipping numbers is not supported yet. Please provide non-numeric inputs.")
            else:
                flipped_args = list(reversed(args))
                await ctx.send(f"🔁 | Flipped result: `{' '.join(flipped_args)}`")
        else:
            await ctx.send("🔁 | Oops! Please provide some items to flip.")

@bot.command(name="count")
async def count_command(ctx, *args):
    """Counts the number of input arguments."""
    async with ctx.typing():
        if args:
            if contains_numbers(args):
                await ctx.send("⚠️ | Counting numbers is not supported yet. Please provide non-numeric inputs.")
            else:
                count = len(args)
                await ctx.send(f"📊 | Total items: `{count}`")
        else:
            await ctx.send("📊 | Oops! Please provide some items to count.")

@bot.command(name="shuffle")
async def shuffle_command(ctx, *args):
    """Shuffles input arguments randomly."""
    async with ctx.typing():
        if args:
            if contains_numbers(args):
                await ctx.send("⚠️ | Shuffling numbers is not supported yet. Please provide non-numeric inputs.")
            else:
                shuffled_args = list(args)
                random.shuffle(shuffled_args)
                await ctx.send(f"🎲 | Shuffled result: `{' '.join(shuffled_args)}`")
        else:
            await ctx.send("🎲 | Oops! Please provide some items to shuffle.")

@bot.command(name="hello")
async def hello_command(ctx):
    """Sends a random greeting."""
    async with ctx.typing():
        greeting = random.choice(hello_messages).format(user=ctx.author.display_name)
        await ctx.send(greeting)

@bot.command(name="cil")
async def cil_command(ctx):
    """Sends an easter egg message."""
    async with ctx.typing():
        await ctx.send(easter_egg_message)

# Logs successful login and Sets bot discord profile status
@bot.event
async def on_ready():
    logger.info(f"Bot logged in as {bot.user}")
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="$help! 🔧"))

# Error handling for unknown commands or errors
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("❌ | That command doesn't exist. Type `$help` for available commands.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("❌ | Missing arguments, please provide all required inputs.")
    else:
        await ctx.send(f"❌ | An unexpected error occurred: {error}")
        logger.error(f"Unexpected error: {error}")

# Run the bot
if TOKEN:
    bot.run(TOKEN)
else:
    logger.error("DISCORD_BOT_TOKEN not found in environment variables.")
    print("Error: DISCORD_BOT_TOKEN not found in environment variables.")
