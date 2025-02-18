from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("auto_start") & filters.private)
    async def auto_start(client, message):
        await message.reply("Configurando inicio automático...")
