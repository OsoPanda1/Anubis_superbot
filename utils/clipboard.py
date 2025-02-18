from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("clipboard") & filters.private)
    async def clipboard(client, message):
        await message.reply("Obteniendo texto del portapapeles...")
