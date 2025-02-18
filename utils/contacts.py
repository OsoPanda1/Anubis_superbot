from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("contacts") & filters.private)
    async def contacts(client, message):
        await message.reply("Obteniendo contactos...")
