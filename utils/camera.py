from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("capture") & filters.private)
    async def capture(client, message):
        await message.reply("Capturando foto...")
