from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("read_notifications") & filters.private)
    async def read_notifications(client, message):
        await message.reply("Leyendo notificaciones...")

    @app.on_message(filters.command("send_notification") & filters.private)
    async def send_notification(client, message):
        await message.reply("Enviando notificación...")
