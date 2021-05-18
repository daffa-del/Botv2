import amanobot
from amanobot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from amanobot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import random
import time
import os
import json
import pytz
from datetime import datetime

#TOKEN DISINI
token = "1811644814:AAHZBxwOo0k0N7CYJtjbouyLu6e75mQ1cmA"
bot = amanobot.Bot(token)


queue = {
	"free":[],
	"occupied":{}
}
users = []
use2 = []

def saveConfig(data):
	return open('config.json', 'w').write(json.dumps(data))

if __name__ == '__main__':
	s = time.time()
	print('[#] Engine On!\n[i] Created by @VinsxV\n')
	print('[#] mengecek config...')
	if not os.path.isfile('config.json'):
		print('[#] memebuat config file...')
		open('config.json', 'w').write('{}')
		print('[#] Done')
	else:
		print('[#] Config found!')
	print('[i] Bot online ' + str(time.time() - s) + 's')
def exList(list, par):
	a = list
	a.remove(par)
	return a

def handle(update):

	global queue
	try:
		config = json.loads(open('config.json', 'r').read())
		if 'text' in update:
			text = update["text"]
		else:
			text = ""
		uid = update["from"]["id"]

		if uid not in users:
			users.append(uid)

		if not uid in config and text != "/nopics":
			config[str(uid)]["pics"]:
			saveConfig(config)

		#MULAI
		if uid in queue["occupied"]:
			if 'text' in update:
				if text != "/start" and text != "/exit" and text != "/next" and text != '⛔ Exit' and text != 'Next ⏩' and text != "/refresh" and text != "/nopics":
					bot.sendMessage(queue["occupied"][uid], "" + text)

		if 'photo' in update:
			if config[str(queue["occupied"][uid])]["pics"]:
				photo = update['photo'][0]['file_id']
				bot.sendPhoto(queue["occupied"][uid], photo)
			else:
				bot.sendMessage(queue["occupied"][uid], "🗣️ Pasangan mengirim gambar ke kamu, mode Perlindungan Aktif. Nonaktifkan mode Perlindungan ketik /nopics")
				bot.sendMessage(uid, "🚫 Pasangan mengaktifkan mode Perlindungan, kamu tidak bisa kirim gambar")

		if 'video' in update:
			video = update['video']['file_id']
			bot.sendVideo(queue["occupied"][uid], video)

		if 'voice' in update:
			voice = update['voice']['file_id']
			bot.sendVoice(queue["occupied"][uid], voice)

		if 'video_note' in update:
			video_note = update['video_note']['file_id']
			bot.sendVideoNote(queue["occupied"][uid], video_note)

		if 'document' in update:
			document = update['document']['file_id']
			bot.sendDocument(queue["occupied"][uid], document)

		if 'audio' in update:
			audio = update['audio']['file_id']
			bot.sendAudio(queue["occupied"][uid], audio)

		if 'sticker' in update:
			sticker = update['sticker']['file_id']
			bot.sendDocument(queue["occupied"][uid], sticker)
			
		#START
		if text == "/start" or text == "/refresh":
			if not uid in queue["occupied"]:
				asw = ReplyKeyboardMarkup(keyboard=[['🚀 Cari Gebetan'], ['🔛 Online', '⬆️ Menu']], resize_keyboard=True, one_time_keyboard=True)
				bot.sendMessage(uid, "🗣️ Selamat bergabung di Bot FWB!\n\nSemangat cari Gebetan nya..", parse_mode= 'MarkDown',disable_web_page_preview= True ,
				reply_markup=asw)
		
		#REPORT REMOVE
		#if update["text"].split()[0] == "/p":
		#	text = update["text"].split()
		#	if len(text) == 0:
		#		bot.sendMessage(uid, "Masukan Pesan!")
		#	try:
		#		for uid in users:
		#			bot.sendMessage(uid," ".join(text[1:]) , parse_mode= 'MarkDown', disable_web_page_preview=True)
		#	except:
		#		pass

		#GENDER
		#if text == "/setting":
		#	bot.sendMessage(uid, "Pilih jenis kelamin anda", reply_markup={"inline_keyboard": [[{"text":"👨‍🦰 Cowok", "callback_data":"gender-laki"}, {"text":"👩🏻 Cewek", "callback_data":"gender-perempuan"}]]})
		#
		#if "data" in update:
		#	if update["data"] == "gender-laki":
		#		profil[uid] = {"data": update["from"]["gender-laki"], "gender": "👨‍🦰 Cowok/Male"}
		#		bot.sendMessage(uid, "Gender telah di setting ke : 👨‍🦰 Cowok")
		#	if update["data"] == "gender-perempuan":
		#		profil[uid] = {"name": update["from"]["gender-perempuan"], "gender": " 👩🏻 Cewek/Female"}
		#		bot.sendMessage(uid, "Gender telah di setting ke : 👩🏻 Cewek")

		#Admin REMOVE
		#elif text == 'Admin':
		#	bot.sendMessage(uid, "🗣️ Bot ini butuh kerja sama bantuan dari temen semua, bagi yang minat menjadi bagian dari keluarga silahkan PC..\n\n🛡️ @VinsxV\n\nUtamakan buat cewek!")

		#if text == "/pw":
		#	text = update["text"].split()[0]
		#	if len(text) == 0:
		#		bot.sendMessage(uid, "Masukan Pesan!")
		#	try:
		#		for uid in use2:
		#			if "username" not in update["from"]:
		#				_id1 = update["from"]["id"]
		#				return bot.sendMessage(_id1, "Mau Ngirim Pesan ke Admin\nIsi Username Kamu Dulu!!")
		#			name = update["from"]["username"]
		#			_id = update["from"]["id"]
		#			bot.sendMessage(uid, "Username :@" + str(name) + " ID :" + str(_id) + "\nText : " + " ".join(text[1:]), parse_mode='MarkDown', disable_web_page_preview=True)
		#			bot.sendMessage(_id, "@"+str(name)+"\n✅ Pesan Terkirim ke Admin")
		#	except:
		#		pass

		#Cek Online
		elif text == '🔛 Online':
			if not uid in queue["occupied"]:
				file = json.loads(open("config.json", "r").read())
				text = "👤 User Online saat ini : " + str(len(file)) + " User!"
				bot.sendMessage(uid, text)

		#PROMO + INFO + TOMOOL APA SAJA
		#elif text == '🔥 Promosi':
		#	if "first_name" not in update["from"]:
		#		return bot.sendMessage(uid, "Harap Isi Nama depan Kamu!!")
		#	if "last_name" not in update["from"]:
		#		return bot.sendMessage(uid, "Dinonaktifkan!")
		#	if update["from"]["first_name"] != None:
		#		name = update["from"]["first_name"] + " " + update["from"]["last_name"]
		#		_id = update["from"]["uid"]
		#		username = update["from"]["username"]
		#		date1 = datetime.fromtimestamp(update["date"], tz=pytz.timezone("asia/jakarta")).strftime("%d/%m/%Y %H:%M:%S").split()
		#		text = "*Nama : " + str(name)+"*" +"\n"
		#		text += "*ID Kamu :* " +"`"+ str(_id) +"`"+"\n"
		#		text += "*Username :* @" + str(username) + "\n"
		#		text += "*Tanggal :* " + str(date1[0]) +"\n"
		#		text += "*Waktu :* " + str(date1[1]) + " WIB" "\n"
		#		bot.sendMessage(uid, text, parse_mode='MarkDown')

		#CARI
		elif text == '🚀 Cari Gebetan' or text == "/cari" :
			if not uid in queue["occupied"]:
				keyboard = ReplyKeyboardMarkup(keyboard=[['/refresh']], resize_keyboard=True, one_time_keyboard=True)
			bot.sendMessage(uid, '⌛️ Sedang mencari pasangan kamu.. tunggu sebentar!\n\nTerlalu lama mencari tekan refresh\n\nNOTE: Mode Perlindungan Aktif secara default', reply_markup=keyboard)
			print("[SB] " + str(uid) + " ✅ Join ke obrolan!")
			queue["free"].append(uid)
                
		#EXIT
		elif text == '⛔ Exit' or text == "/exit" and uid in queue["occupied"]:
			print('[SB] ' + str(uid) + ' ⛔ Meninggalkan obrolan! ' + str(queue["occupied"][uid]))
			keyboard = ReplyKeyboardMarkup(keyboard=[['🚀 Cari Gebetan'], ['🔙 Kembali']], resize_keyboard=True, one_time_keyboard=True)
			bot.sendMessage(uid, "🛑 Obrolan telah berakhir!")
			bot.sendMessage(uid, "🗣️ Selamat bergabung di Bot FWB!\n\nSemangat cari Gebetan nya..\n\nJoin group : @fwbxchat", disable_web_page_preview=True, reply_markup=keyboard)
			bot.sendMessage(queue["occupied"][uid], "ℹ️ Pasangan keluar dari obrolan!", reply_markup=keyboard)
			del queue["occupied"][queue["occupied"][uid]]
			del queue["occupied"][uid]

		#MENU
		elif text == '⬆️ Menu':
			keyboard = ReplyKeyboardMarkup(keyboard=[
                ['ℹ️ Support', '🆙 Hit me'], ['🔙 Kembali']
            ], resize_keyboard=True, one_time_keyboard=True)
			bot.sendMessage(uid, "👣 Menu..", reply_markup=keyboard)

		#RATE ERROR
		#elif text == '🤤 Bot Rate':
		#	bot.sendMessage(uid, 'ℹ️ Rate your body!',reply_markup = InlineKeyboardMarkup(inline_keyboard=[
                #                   [InlineKeyboardButton(text="🤤 Bot Rate!", url='https"//t.me/Donasi88bot')],
                #              ]
                #            ))	
		#	bot.sendMessage(uid, "ℹ️ Keep privacy!")

		#ISI MENU 2 DALAM
		elif text == 'ℹ️ Support':
			bot.sendMessage(uid, "👀 Support terus ya..")

		elif text == '🆙 Hit me':
			bot.sendMessage(uid, "Donation :\n\n🔸Saweria : https://saweria.co/VinsxV\n\n🔸Sociabuzz : https://sociabuzz.com/vinsxv/tribe", parse_mode= 'MarkDown',disable_web_page_preview= True)

		elif text == '🔙 Kembali':
			keyboard = ReplyKeyboardMarkup(keyboard=[['🚀 Cari Gebetan'], ['🔛 Online', '⬆️ Menu']], resize_keyboard=True, one_time_keyboard=True)
			bot.sendMessage(uid, "👣 Kembali..", reply_markup=keyboard)

		#NEXT
		elif text == 'Next ⏩' or text == "/next" and uid in queue["occupied"]:
			print('[SB] ' + str(uid) + ' ⏩ Skip obrolan.. ' + str(queue["occupied"][uid]))
			keyboard = ReplyKeyboardMarkup(keyboard=[['🚀 Cari Gebetan'], ['🔙 Kembali']], resize_keyboard=True)
			bot.sendMessage(uid, "🛑 Mengakhiri obrolan!")
			bot.sendMessage(queue["occupied"][uid], "ℹ️ Pasangan keluar dari obrolan!", reply_markup=keyboard)
			del queue["occupied"][queue["occupied"][uid]]
			del queue["occupied"][uid] 
			if not uid in queue["occupied"]: 
				bot.sendMessage(uid, '⌛️ Sedang mencari pasangan.. tunggu sebentar!\n\nTerlalu lama mencari tekan /refresh')
				print("[SB] " + str(uid) + " ☑️ Join ke obrolan!")
				queue["free"].append(uid)

		#NOPICS
		if text == "/nopics":
			config[str(uid)]["pics"] = not config[str(uid)]["pics"] 
			if config[str(uid)]["pics"]:
				bot.sendMessage(uid, " 🚫 Mode Perlindungan Nonaktif")
			else:
				bot.sendMessage(uid, " 🛡️ Mode Perlindungan Aktif (default)")
			saveConfig(config)

		#AKHIR
		if len(queue["free"]) > 1 and not uid in queue["occupied"]:
			partner = random.choice(exList(queue["free"], uid))
			if partner != uid:
				keyboard = ReplyKeyboardMarkup(keyboard=[
					['Hii..', 'Cewe apa cowo?'], ['FWBan yuk..'], ['⛔ Exit', 'Next ⏩']
				],resize_keyboard=True, one_time_keyboard=True)
				print('[SB] ' + str(uid) + ' ☑️ Berjodoh dengan.. ' + str(partner))
				queue["free"].remove(partner)
				queue["occupied"][uid] = partner
				queue["occupied"][partner] = uid
				bot.sendMessage(uid, ' ✅ Pasangan ditemukan!', reply_markup=keyboard)
				bot.sendMessage(partner, ' ✅ Pasangan ditemukan!', reply_markup=keyboard)
	except 	Exception as e:
		print('[!] Error: ' + str(e))

if __name__ == '__main__':
	bot.message_loop(handle)

	while True:
		time.sleep(1)
