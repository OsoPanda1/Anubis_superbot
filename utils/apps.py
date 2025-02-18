from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("apps") & filters.private)
    async def apps(client, message):
        await message.reply("Obteniendo lista de aplicaciones...")
