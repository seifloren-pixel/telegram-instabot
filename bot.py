from telegram import Update
from telegram.ext import *
import yt_dlp
import os

TOKEN="8568571436:AAFlmALkdaCYhBMLor3QmPYQ5wLXGpRjksk"

async def handle(update, context):

    url = update.message.text

    try:

        await update.message.reply_text(
            "جارى التحميل..."
        )

        opts = {
            "outtmpl":"video.%(ext)s"
        }

        with yt_dlp.YoutubeDL(opts) as ydl:

            info = ydl.extract_info(
                url,
                download=True
            )

            file = ydl.prepare_filename(
                info
            )

        await update.message.reply_video(
            open(file,"rb")
        )

        os.remove(file)

    except:

        await update.message.reply_text(
            "فشل تحميل الرابط"
        )

app = Application.builder().token(
TOKEN
).build()

app.add_handler(
MessageHandler(
filters.TEXT,
handle
)
)

app.run_polling()
