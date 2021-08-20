# (c) @AbirHasan2005

from pyrogram.errors import UserNotParticipant
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from configs import Config


async def handle_force_sub(bot, cmd):
    invite_link = await bot.create_chat_invite_link(int(Config.UPDATES_CHANNEL))
    try:
        user = await bot.get_chat_member(int(Config.UPDATES_CHANNEL), cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sorry Sir, You are Banned to use me. Contact my [Support Group](https://t.me/linux_repo).",
                parse_mode="markdown",
                disable_web_page_preview=True,
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Bergabunglah dengan Saluran Pembaruan Saya untuk menggunakan Bot ini!**\n\nKarena Kelebihan Beban, Hanya Pelanggan Saluran yang dapat menggunakan Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🤖 Join Updates Channel", url=invite_link.invite_link
                        )
                    ],
                    [InlineKeyboardButton("🔄 Refresh 🔄", callback_data="refreshmeh")],
                ]
            ),
            parse_mode="markdown",
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact my [Support Group](https://t.me/linux_repo).",
            parse_mode="markdown",
            disable_web_page_preview=True,
        )
        return 400
