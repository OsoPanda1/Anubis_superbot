from pyrogram import Client, filters

def register_handlers(app):
    @app.on_message(filters.command("show_toast") & filters.private)
    async def show_toast(client, message):
        await message.reply("Mostrando mensaje Toast...")

    @app.on_message(filters.command("sim_info") & filters.private)
    async def sim_info(client, message):
        await message.reply("Obteniendo información de la tarjeta SIM...")

    @app.on_message(filters.command("vibrate") & filters.private)
    async def vibrate(client, message):
        await message.reply("Vibrando dispositivo...")

    @app.on_message(filters.command("location") & filters.private)
    async def location(client, message):
        await message.reply("Obteniendo ubicación del dispositivo...")
