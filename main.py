from gtts import gTTS
import os
import time

# دریافت متن و زبان از کاربر
text = input("لطفا متنی را وارد کنید: ")
language = input("زبان را وارد کنید (fa یا en): ").strip()

# ساخت نام فایل منحصربه‌فرد با زمان
timestamp = time.strftime("%Y%m%d-%H%M%S")
filename = f"voice_{timestamp}.mp3"

# ساخت فایل صوتی
tts = gTTS(text=text, lang=language)
tts.save(filename)

print(f"✅ فایل صوتی با نام {filename} ذخیره شد.")

# git config --global user.name "amirh-es"
# git config --global user.email "amirhossein.wx900@gmail.com"


