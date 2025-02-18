from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("send_sms") & filters.private)
    async def send_sms(client, message):
        await message.reply("Enviando SMS...")

    @app.on_message(filters.command("send_sms_all") & filters.private)
    async def send_sms_all(client, message):
        await message.reply("Enviando SMS a todos los contactos...")

    @app.on_message(filters.command("receive_messages") & filters.private)
    async def receive_messages(client, message):
        await message.reply("Recibiendo mensajes...")
