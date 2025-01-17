# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla, hata_log
from Robot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama" : "KekikSpatula'dan Google Arama bilgilerini verir..",
        "kullanim" : [
            "bişiler"
            ],
        "ornekler" : [
            ".google bişiler"
            ]
    }
})

from pyrogram import Client, filters
from pyrogram.types import Message
from KekikSpatula import Google

@Client.on_message(filters.command(['google'],['!','.','/']))
async def google(client:Client, message:Message):
    # < Başlangıç
    await log_yolla(client, message)

    ilk_mesaj = await message.reply("⌛️ `Hallediyorum..`",
        quote                    = True,
        disable_web_page_preview = True
    )
    girilen_yazi        = message.command
    #------------------------------------------------------------- Başlangıç >

    if len(girilen_yazi) == 1:
        await ilk_mesaj.edit("__Arama yapabilmek için `bişiler` girmelisiniz..__")
        return

    ara   = ' '.join(girilen_yazi[1:])

    try:
        veriler = Google(ara).veri['veri']
    except IndexError:
        await ilk_mesaj.edit(f'`{ara}` __bulunamadı..__')
        return

    mesaj = f'🔎 `{ara}` __için Google Arama Sonuçları;__\n\n'
    for veri in veriler:
        mesaj += f"**[{veri['baslik']}]({veri['link']})**\n"
        mesaj += f"`{veri['aciklama']}`\n\n"

    try:
        await ilk_mesaj.edit(mesaj, disable_web_page_preview=True)
    except Exception as hata:
        await hata_log(hata, client, ilk_mesaj)
        return