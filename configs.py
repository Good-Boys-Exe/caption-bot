# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	BOT_NAME = os.environ.get("BOT_NAME")
	OWNER_USERNAME = os.environ.get("OWNER_USERNAME")
	USERNAME_GROUP = os.environ.get("USERNAME_GROUP")
	USERNAME_CHANNEL = os.environ.get("USERNAME_CHANNEL")
	DONATE_LINK = os.environ.get("DONATE_LINK")
	ABOUT_BOT_TEXT = f"""
Ini adalah Bot Toko Berkas Permanen!
Kirimi saya file apa pun, saya akan menyimpannya di Database saya. Juga berfungsi untuk saluran. Tambahkan saya ke saluran sebagai Admin dengan Izin Edit, saya akan menambahkan Simpan File Unggahan di Saluran & tambahkan Tautan Tombol yang Dapat Dibagikan.

🤖 **Namaku:** [{BOT_NAME}](https://t.me/{BOT_USERNAME})

📝 **Bahasa:** [Python3](https://www.python.org)

📚 **Perpustakaan:** [Pyrogram](https://docs.pyrogram.org)

📡 **Diselenggarakan pada:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Pengembang:** @{OWNER_USERNAME}

👥 **Support Group:** @{USERNAME_GROUP}

📢 **Updates Channel:** @{USERNAME_CHANNEL}
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Pengembang:** @{OWNER_USERNAME}

Pengembang adalah Super Noob. Baru Belajar dari Dokumen Resmi. Harap Donasi pengembang untuk Menjaga Layanan Tetap Hidup.

Juga ingat bahwa pengembang akan Menghapus Konten Dewasa dari Database. Jadi lebih baik 
[Donate Now](DONATE_LINK)
"""
	HOME_TEXT = f"""
Hi, {}](tg://user?id={})\n\nIni Permanen **{BOT_NAME}**.

Kirimi saya file apa pun, saya akan memberi Anda Tautan yang Dapat Dibagikan secara permanen. Saya Mendukung Saluran Juga! Centang Tombol **About Bot**.
""",
