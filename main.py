from typing import Final
import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
from discord import app_commands
from responses import get_openrouter_response

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")
GUILD_ID: Final[int] = os.getenv("GUILD_ID")
    
class Client(commands.Bot):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

        try:
            id_server1 = discord.Object(id=GUILD_ID)
            synced = await self.tree.sync(guild=id_server1)
            print(f"{len(synced)} commands")
        except Exception as e:
            print(f"Error: {e}")
    
    async def on_message(self, message: discord.Message) -> str:
        if message.author == self.user:
            return
        
        if message.content.startswith('halo'):
            await message.channel.send(f"Assalamualaikum, hai mang {message.author}")

intents: discord.Intents = discord.Intents.default()
intents.message_content = True
client: Client = Client(command_prefix="!", intents=intents)

id_server = discord.Object(id=GUILD_ID)
@client.tree.command(name="ask", description="Ask to AI bot", guild=id_server)
async def aiBot(interaction: discord.Interaction, prompt: str):
    await interaction.response.defer()
    print(f"Prompt: {prompt}")
    response: str = get_openrouter_response(prompt)
    await interaction.followup.send(content=response)
    
client.run(token=TOKEN)