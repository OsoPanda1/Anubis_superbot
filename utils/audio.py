from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("record") & filters.private)
    async def record(client, message):
        await message.reply("Grabando audio...")
