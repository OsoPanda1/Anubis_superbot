from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("autostart") & filters.private)
    async def auto_start_command(client, message):
        await message.reply("Auto-start command received.")
