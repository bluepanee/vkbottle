from io import BytesIO

from vkbottle import AudioUploader, Bot, DocUploader, Message, PhotoUploader

from gtts import gTTS
from PIL import Image

bot = Bot("token")

photo_uploader = PhotoUploader(bot.api, generate_attachment_strings=True)
doc_uploader = DocUploader(bot.api, generate_attachment_strings=True)
audio_uploader = AudioUploader(bot.api, generate_attachment_strings=True)


@bot.on.message_handler(text="photo_from_bytes", lower=True)
async def photo_from_bytes(ans: Message):
    image = Image.new("RGB", (320, 320), (0, 0, 0))
    fp = BytesIO()
    image.save(fp, "PNG")
    setattr(fp, "name", "image.png")
    photo = await photo_uploader.upload_message_photo(fp)
    await ans(attachment=photo)


@bot.on.message_handler(text="doc_from_file", lower=True)
async def doc_from_file(ans: Message):
    doc = Image.new("RGB", (320, 320), (0, 0, 0))
    doc.save("doc.png", "RGB")
    doc_output = await doc_uploader.upload_doc_to_message("doc.png", ans.peer_id)
    await ans(attachment=doc_output)


@bot.on.message_handler(text="audio_message", lower=True)
async def audio(ans: Message):
    tts = gTTS(text="бокале монада", lang="ru")
    fp = BytesIO()
    tts.write_to_fp(fp)
    audio_message = await audio_uploader.upload_audio_message(fp, ans.peer_id)
    await ans(attachment=audio_message)


if __name__ == "__main__":
    bot.run_polling()
