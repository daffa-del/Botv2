import amanobot
from amanobot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from amanobot.namedtuple import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
import random
import time
import os
import json
import pytz
from datetime import datetime

token = "AAET79YsdfsZ0xtYUbrz257cHv2KlPZzgY0"
bot = amanobot.Bot(token)


queue = {
	"free":[],
	"occupied":{}
}
users = []
use2 = ['1816906452']

def saveConfig(data):
	return open('config.json', 'w').write(json.dumps(data))

if __name__ == '__main__':
	s = time.time()
	print('[#] Buatan\n[i] Created by Davi ALFajr\n')
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
			config[str(uid)] = {"pics":True}
			saveConfig(config)

		if uid in queue["occupied"]:
			if 'text' in update:
				if text != "Hapus Keyboard" and text != "❌ Exit" and text !="Next ▶️" and text != "/refresh":
					bot.sendMessage(queue["occupied"][uid], "" + text)
			
		if 'photo' in update:
			if config[str(queue["occupied"][uid])]["pics"]:
				photo = update['photo'][0]['file_id']
				bot.sendPhoto(queue["occupied"][uid], photo)
			else:
				bot.sendMessage(queue["occupied"][uid], "Stranger tried to send you a photo, but you disabled this,  you can enable photos by using the /nopics command")
				bot.sendMessage(uid, "Stranger disabled photos, and will not receive your photos")
						
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

		if text == "/start" or text == "/refresh":
			if not uid in queue["occupied"]:
				asw = ReplyKeyboardMarkup(keyboard=[['Search 👥','Profile📌'], ['Total Users😈','Menu🐱']], resize_keyboard=True, one_time_keyboard=True)
				bot.sendMessage(uid, "Selamat Bergabung Di\nBot sange🙊\n\nJangan Lupa Grup @cewecowobersatu\nLINK BOKEP [FREE](https://semawur.com/ccRSCsI7u)", parse_mode= 'MarkDown',disable_web_page_preview= True ,
				reply_markup=asw)

		#if update["text"].split()[0] == "/p":
			#text = update["text"].split()
			#if len(text) == 0:
				#bot.sendMessage(uid, "Masukan Pesan!")
			#try:
				#for uid in users:
					#bot.sendMessage(uid," ".join(text[1:]) , parse_mode= 'MarkDown', disable_web_page_preview=True)
			#except:
				#pass

		#elif text == "/setting":
		#	bot.sendMessage(uid, "Pilih Jenis Kelamin Knda", reply_markup={"inline_keyboard": [[{"text":"Pria👨‍🦰", "callback_data":"gender-laki"}, {"text":"Wanita👩🏻", "callback_data":"gender-perempuan"}]]})

		#if "data" in update:
		#	if update["data"] == "gender-laki":
		#		profil[uid] = {"name": update["from"]["first_name"], "gender": "Pria/Male👨‍🦰"}
		#		bot.sendMessage(uid, "Gender telah di setting ke Pria👨‍🦰")
		#	elif update["data"] == "gender-perempuan":
		#			profil[uid] = {"name": update["from"]["first_name"], "gender": "Wanita/Female👩🏻"}
		#			bot.sendMessage(uid, "Gender telah di setting ke Wanita👩🏻")

		elif text == 'Admin':
				bot.sendMessage(uid, "Di Nonaktifkan Sementara!")

		#if text == "/pw":
		#	text = update["text"].split()[0]
		#	if len(text) == 0:
		#		bot.sendMessage(uid, "Masukan Pesan!")
		#	try:
		#		for uid in use2:
		#			if "username" not in update["from"]:
		#				_id1 = update["from"]["id"]
		#				return bot.sendMessage(_id1, "Mau Ngirim Pesan keadmin\nIsi Username Kamu Dulu!!")
		#			name = update["from"]["username"]
		#			_id = update["from"]["id"]
		#			bot.sendMessage(uid, "Username :@" + str(name) + " ID :" + str(_id) + "\nText : " + " ".join(text[1:]), parse_mode='MarkDown', disable_web_page_preview=True)
		#			bot.sendMessage(_id, "@"+str(name)+"\nPesan Terkirim ke admin")
		#	except:
		#		pass

		elif text == 'Total Users😈':
			if not uid in queue["occupied"]:
				file = json.loads(open("config.json", "r").read())
				text = "Users Sange saat ini : " + str(len(file)) + " User Sange"
				bot.sendMessage(uid, text)

		elif text == 'Profile📌':
			if "username" not in update["from"]:
				return bot.sendMessage(uid, "Harap Isi Username Kamu!!")
			if "last_name" not in update["from"]:
				return bot.sendMessage(uid, "Harap Isi Nama Belakang Kamu!!")
			if update["from"]["last_name"] != None:
				name = update["from"]["first_name"] + " " + update["from"]["last_name"]
				_id = update["from"]["id"]
				username = update["from"]["username"]
				date1 = datetime.fromtimestamp(update["date"], tz=pytz.timezone("asia/jakarta")).strftime("%d/%m/%Y %H:%M:%S").split()
				text = "*Nama : " + str(name)+"*" +"\n"
				text += "*ID Kamu :* " +"`"+ str(_id) +"`"+"\n"
				text += "*Username :* @" + str(username) + "\n"
				text += "*Tanggal :* " + str(date1[0]) +"\n"
				text += "*Waktu :* " + str(date1[1]) + " WIB" "\n"
				bot.sendMessage(uid, text, parse_mode='MarkDown')

		elif text == 'Search 👥':
			if not uid in queue["occupied"]:
				keyboard = ReplyKeyboardRemove()
			bot.sendMessage(uid, 'Sedang pasangan sange kamu.. tunggu sebentar', reply_markup=keyboard)
			print("[SB] " + str(uid) + " Join ke obrolan")
			queue["free"].append(uid)

		elif text == '❌ Exit' and uid in queue["occupied"]:
			print('[SB] ' + str(uid) + ' meninggalkan jodohnya ' + str(queue["occupied"][uid]))
			keyboard = ReplyKeyboardMarkup(keyboard=[['Search 👥','Profile📌'], ['Total Users😈','Menu🐱']], resize_keyboard=True,one_time_keyboard=True)
			bot.sendMessage(uid, "Obrolan telah berakhir\n\nLink Bokep : https://semawur.com/ccRSCsI7u")
			bot.sendMessage(uid, "Selamat Bergabung DiBot sange🙊\n\nJangan Lupa Grup @cewecowobersatu", reply_markup=keyboard)
			bot.sendMessage(queue["occupied"][uid], "Pasangan kamu keluar dari obrolan\n\nDia membagikan Link Bokep : https://semawur.com/ccRSCsI7u", reply_markup=keyboard)
			del queue["occupied"][queue["occupied"][uid]]
			del queue["occupied"][uid]

		elif text == 'Menu🐱':
			keyboard = ReplyKeyboardMarkup(keyboard=[
                ['Link Bokep', 'Donasi', 'Admin'],['Bot VCS'],['🔙 Main Menu']
            ], resize_keyboard=True, one_time_keyboard=True)
			bot.sendMessage(uid, "WAJIB JOIN GRUP INI @cewecowobersatu\nGAK JOIN GA VCS :v", reply_markup=keyboard)

		elif text == 'Link Bokep':
			bot.sendMessage(uid, 'Cek bokep viral, dan pap sex dibawah😙',reply_markup = InlineKeyboardMarkup(inline_keyboard=[
                                    [InlineKeyboardButton(text="Bokep Viral😍", url='https://semawur.com/ccRSCsI7u')],
                                    [InlineKeyboardButton(text="Keleksi Pap Viral😍", url='https://semawur.com/StJkG3lhFPa')]
                                ]
                            ))	
			bot.sendMessage(uid, "Wajib Join Grup @cewecowobersatu")
			
		elif text == 'Donasi':
			bot.sendMessage(uid, "Mau donasi ke admin?\nCukup dengan cara klik link aja🙂\nLink : https://realsht.mobi/GArv4")
			
		elif text == 'Bot VCS':
			bot.sendMessage(uid, "Coba Bot Vcs Free\n[BOT VCS FREE](https://t.me/VCS_TALENHIJAB_bot?start=r05827436540)", parse_mode= 'MarkDown',disable_web_page_preview= True)
			
		elif text == '🔙 Main Menu':
			keyboard = ReplyKeyboardMarkup(keyboard=[['Search 👥','Profile📌'], ['Total Users😈','Menu🐱']], resize_keyboard=True, one_time_keyboard=True)
			bot.sendMessage(uid, "Selamat Bergabung DiBot sange🙊\n\nJangan Lupa Grup @cewecowobersatu", reply_markup=keyboard)

		elif text == "Next ▶️" and uid in queue["occupied"]:
			print('[SB] ' + str(uid) + ' meninggalkan obrolan dengan ' + str(queue["occupied"][uid]))
			keyboard = ReplyKeyboardMarkup(keyboard=[['Search 👥', '🔙 Main Menu']], resize_keyboard=True)
			bot.sendMessage(uid, "Mengakhiri obrolan...")
			bot.sendMessage(uid, "Obrolan telah berakhir")
			bot.sendMessage(queue["occupied"][uid], "Obrolan telah berakhir")
			bot.sendMessage(queue["occupied"][uid], "Pasangan kamu keluar dari obrolan", reply_markup=keyboard)
			del queue["occupied"][queue["occupied"][uid]]
			del queue["occupied"][uid] 
			if not uid in queue["occupied"]: 
				bot.sendMessage(uid, 'Sedang mencari pasangan sange.. tunggu sebentar')
				print("[SB] " + str(uid) + " Join ke obrolan") 
				queue["free"].append(uid)


		if text == "/nopics":
			config[str(uid)]["pics"] = not config[str(uid)]["pics"] 
			if config[str(uid)]["pics"]:
				bot.sendMessage(uid, "Pasangan Dapat Mengirim Pap")
			else:
				bot.sendMessage(uid, "Pasangan Tidak Bisa Mengirim Pap")
			saveConfig(config)

		if len(queue["free"]) > 1 and not uid in queue["occupied"]:
			partner = random.choice(exList(queue["free"], uid))
			if partner != uid:
				keyboard = ReplyKeyboardMarkup(keyboard=[
					['Next ▶️', '❌ Exit']
				],resize_keyboard=True, one_time_keyboard=True)
				print('[SB] ' + str(uid) + ' Berjodoh dengan ' + str(partner))
				queue["free"].remove(partner)
				queue["occupied"][uid] = partner
				queue["occupied"][partner] = uid
				bot.sendMessage(uid, f'Pasangan sange ditemukan.., selamat ah aha ah😜', reply_markup=keyboard)
				bot.sendMessage(partner, f'Pasangan sange ditemukann.., selamat sange😜', reply_markup=keyboard)
	except 	Exception as e:
		print('[!] Error: ' + str(e))

if __name__ == '__main__':
	bot.message_loop(handle)

	while True:
		time.sleep(1)
