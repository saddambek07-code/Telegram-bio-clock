import asyncio
import datetime
import pytz
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# 1-bosqichda olgan kodlaringizni shu yerga yozasiz:
API_ID = 1234567  # O'zingizning api_id ni raqam ko'rinishida yozing
API_HASH = 'sizning_api_hash_kodingiz'  # O'zingizning api_hash ni yozing

# Vaqt zonasi (O'zbekiston uchun)
TIMEZONE = pytz.timezone('Asia/Tashkent')

async def main():
    # Telegram bilan bog'lanish
    client = TelegramClient('session_name', API_ID, API_HASH)
    await client.start()
    print("Userbot muvaffaqiyatli ishga tushdi!")

    while True:
        try:
            # Hozirgi vaqtni olish (HH:MM formatida)
            current_time = datetime.datetime.now(TIMEZONE).strftime("%H:%M")
            
            # Biografiyaga yoziladigan matn
            bio_text = f"Hozirgi vaqt: {current_time} | Men doim onlayndman."
            
            # Profilni yangilash
            await client(UpdateProfileRequest(about=bio_text))
            print(f"Bio yangilandi: {current_time}")
            
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")
            
        # Har 60 soniyada (1 daqiqa) vaqtni yangilab turadi
        await asyncio.sleep(60)

if __name__ == '__main__':
    asyncio.run(main())
  
