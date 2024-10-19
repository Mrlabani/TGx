import os,webbrowser

webbrowser.open('https://t.me/NOOBPRivate')
#-------------[Colors]-----------------
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  #HMODE
a30 = '\x1b[38;5;255m'  #WATAN
#----------[BEGIN LOGO]-------------
print(f"""{a30}— — — — — — — — — — — — —
{a5}[{a3}1{a5}]{a30} - {a4}|{a3} Tool Usernamr Instagram {a4}|
{a5}[{a3}2{a5}]{a30} - {a4}|{a3} Tool Username Telegram  {a4}|
{a5}[{a3}3{a5}]{a30} - {a4}|{a3} Tool Username Bot Tele  {a4}|
{a5}[{a3}4{a5}]{a30} - {a4}|{a3} Tool Username Discord   {a4}|
{a5}[{a3}5{a5}]{a30} - {a4}|{a3} Tool Username Tiktok 4  {a4}|
{a30}— — — — — — — — — — — — —""")

HMODE = int(input(' - Choose '))	
os.system('clear')
webbrowser.open('https://t.me/NOOBPRivate')


if HMODE == 1:
	webbrowser.open('https://t.me/NOOBPRivate')
	from  rich import print
	import requests,os
	import random
	from rich.panel import Panel
	
	
	
	e1='\x1b[38;5;196m'#احمر
	a11 = '\x1b[38;5;8m'  # رمادي
	a14 = '\x1b[38;5;153m'  # أزرق فاتح
	a16 = '\x1b[38;5;48m'  # أخضر فاتح
	a19 = '\x1b[38;5;88m'  # أحمر داكن
	a32 = '\x1b[38;5;180m'  # بني فاتح
	a36 = '\x1b[38;5;228m'  # ذهبي فات
	
	
	
	ID = input(f'{a32} Enter Id Telegram : ')
	token = input(f'{a14} Enter Token Bot Telegram : ')
	os.system('clear')
	
	
	
	C = 0
	G = 0
	l = 'qwertyuiopasdfghjklzxcvbnm1234567890'
	
	while True:
		V1 = "".join(random.choice(l)for i in range(1))
		V2 = "".join(random.choice(l)for i in range(1))
		V3 = "".join(random.choice(l)for i in range(1))
		V4 = "".join(random.choice(l)for i in range(1))
	
		user1 = f'{V1}{V3}.{V4}{V2}'
		user2 = f'{V3}{V1}_{V2}{V4}'
		user3 = f'{V4}.{V3}_{V1}'
		user4 = f'{V3}_{V2}.{V1}'
		user5 = f'{V1}{V4}__{V2}'
		user6 = f'{V2}__{V4}{V3}'
		HMODE = (user1,user2,user3,user4,user5)
		user = random.choice(HMODE)
		url = "https://www.instagram.com/api/v1/users/check_username/"
		
		params = {
		  'hl': "ar"
		}
		
		payload = f"username={user}"
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36",
		#  'Accept-Encoding': "gzip, deflate, br, zstd",
		  'Content-Type': "application/x-www-form-urlencoded",
		  'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
		  'x-ig-www-claim': "0",
		  'sec-ch-ua-platform-version': "\"11.0.0\"",
		  'x-requested-with': "XMLHttpRequest",
		  'sec-ch-ua-full-version-list': "\"Not/A)Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"126.0.6478.188\", \"Google Chrome\";v=\"126.0.6478.188\"",
		  'sec-ch-prefers-color-scheme': "dark",
		  'x-csrftoken': "XKTR39rx_lkeJ2nTEGG9eB",
		  'sec-ch-ua-platform': "\"Android\"",
		  'x-ig-app-id': "1217981644879628",
		  'sec-ch-ua-model': "\"RMX2189\"",
		  'sec-ch-ua-mobile': "?1",
		  'x-instagram-ajax': "1015171929",
		  'x-asbd-id': "129477",
		  'origin': "https://www.instagram.com",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://www.instagram.com/accounts/signup/username/?hl=ar",
		  'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
		  'priority': "u=1, i",
		#  'Cookie': "csrftoken=XKTR39rx_lkeJ2nTEGG9eB; dpr=1.7000000476837158; mid=ZqNRDQABAAGuHUuWQHOLy6NbcbFc; ig_did=950C0754-CE9F-4F38-8342-9FF8E55AF9C6; ig_nrcb=1; datr=ClGjZmt2BNlC_aFKrDfH_Icp; wd=424x804"
		}
		
		response = requests.post(url, params=params, data=payload, headers=headers).text
		if 'true'in str(response):
			print(Panel(f"""[green]
	
	— — — — — — — — — — — — —
	- Good User Ig
	
	- User : @{user}
	
	- Dev : @NOOBPRivate _ WATAN
	— — — — — — — — — — — — —
	
	"""))
		
			god=f"""
	— — — — — — — — — — — — —
	- Good Username 
	
	- User ➠ {user}
	
	- By @NOOBPRivate ~ @noob_jee
	— — — — — — — — — — — — —
	"""
			requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(god))	
		else:
			print(f' - Bad User : {user} ')
			
			
if HMODE == 2:	
	webbrowser.open('https://t.me/NOOBPRivate')
	R = '\033[1;31m' #احمر
	SDM1 = '\033[1;33m' #اصفر
	F = '\033[2;32m' #اخضر
	C = "\033[1;97m" #ابيض
	B = '\033[2;36m'#سمائي
	Y = '\033[1;34m' #ازرق فاتح.
	E = '\033[1;31m'
	B = '\033[2;36m'
	G = '\033[1;32m'
	S = '\033[1;33m' 
	SA = '\x1b[38;5;216m'
	S2A = '\x1b[1;36m'
	S3A = '\x1b[38;5;180m'
	S4A= '\x1b[38;5;88m' 
	S5A = "\x1b[1;32m" 
	S6A= '\x1b[38;5;166m'
	K = '\033[2;35m'
	a1 = '\x1b[1;31m'  # أحمر
	a2 = '\x1b[1;34m'  # أزرق
	a3 = '\x1b[1;32m'  # أخضر
	a4 = '\033[1;97m'  # أصفر
	a5 = '\x1b[38;5;208m'  # برتقالي
	a6 = '\x1b[38;5;5m'  # أرجواني
	a7 = '\x1b[38;5;13m'  # وردي
	a8 = '\x1b[1;30m'  # أسود
	a9 = '\x1b[1;37m'  # أبيض
	a10 = '\x1b[38;5;52m'  # بني
	a11 = '\x1b[38;5;8m'  # رمادي
	a12 = '\x1b[38;5;220m'  # ذهبي
	a13 = '\x1b[38;5;7m'  # فضي
	a14 = '\x1b[38;5;153m'  # أزرق فاتح
	a15 = '\x1b[38;5;18m'  # أزرق داكن
	a16 = '\x1b[38;5;48m'  # أخضر فاتح
	a17 = '\x1b[38;5;22m'  # أخضر داكن
	a18 = '\x1b[38;5;196m'  # أحمر فاتح
	a19 = '\x1b[38;5;88m'  # أحمر داكن
	a20 = '\x1b[38;5;226m'  # أصفر فاتح
	a21 = '\x1b[38;5;136m'  # أصفر داكن
	a22 = '\x1b[38;5;216m'  # برتقالي فات
	a23 = '\x1b[38;5;166m'  # برتقالي داكن
	a24 = '\x1b[38;5;234m'  # أرجواني فاتح
	a25 = '\x1b[38;5;91m'  # أرجواني داكن
	a26 = '\x1b[38;5;205m'  # وردي فاتح
	a27 = '\x1b[38;5;161m'  # وردي داكن
	a28 = '\x1b[38;5;236m'  # أسود فاتح
	a29 = '\x1b[38;5;233m'  # أسود داكن
	a30 = '\x1b[38;5;255m'  # أبيض فاتح
	a31 = '\x1b[38;5;231m'  # أبيض داكن
	a32 = '\x1b[38;5;180m'  # بني فاتح
	a33 = '\x1b[38;5;94m'  # بني داكن
	a34 = '\x1b[38;5;252m'  # رمادي فاتح
	a35 = '\x1b[38;5;246m'  # رمادي داكن
	a36 = '\x1b[38;5;228m'  # ذهبي فاتح
	a37 = '\x1b[38;5;172m'  # ذهبي داكن
	a38 = '\x1b[38;5;188m'  # فضي فاتح
	a39 = '\x1b[38;5;247m'  # فضي داكن
	a40 = '\x1b[38;5;117m'  # أزرق سماوي
	
	import os
	ID = input(f'{a32} Enter Id Telegram : ')
	token = input(f'{a14} Enter Token Bot Telegram : ')
	os.system('clear')
	webbrowser.open('https://t.me/NOOBPRivate')
	
	l = 'qwertyuiopasdfghjklzxcvbnm1234567890'
	
	
	import requests
	from  rich import print
	import json
	import requests
	from  user_agent import generate_user_agent
	import random,telebot
	from rich.panel import Panel
	
	
	
	while True:
		V1 = "".join(random.choice(l)for i in range(1))
		V2 = "".join(random.choice(l)for i in range(1))
		V3 = "".join(random.choice(l)for i in range(1))
		V4 = "".join(random.choice(l)for i in range(1))
		
		user1 = f'{V1}{V3}_{V4}{V2}'
		user2 = f'{V3}{V1}_{V2}{V4}'
		user3 = f'{V4}_{V3}_{V1}'
		user4 = f'{V3}{V2}_{V1}{V4}'
		user5 = f'{V1}{V4}__{V2}'
		user6 = f'{V2}__{V4}{V3}'
		HMODE = (user1,user2,user3,user4,user5)
		user = random.choice(HMODE)
		url = "https://fragment.com/api"
		
		params = {
		  'hash': "a04a4cc7971b4d1173"
		}
		
		payload = f"type=usernames&query={user}=&sort=&method=searchAuctions"
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36",
		  'Accept': "application/json, text/javascript, */*; q=0.01",
		  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		  'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
		  'x-requested-with': "XMLHttpRequest",
		  'sec-ch-ua-mobile': "?1",
		  'sec-ch-ua-platform': "\"Android\"",
		  'origin': "https://fragment.com",
		  'sec-fetch-site': "same-origin",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://fragment.com/?query=jsjsjnsajnajwbqb",
		  'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7,ar-AE;q=0.6",
		  'Cookie': "stel_ssid=707a93bd68ae7949e2_11798633595069971704; stel_dt=-180"
		}
		
		response = requests.post(url, params=params, data=payload, headers=headers)
	
		if 'Unavailable' in response.text:
			print(Panel(f"""[green]
		
	— — — — — — — — — — — — —
	- Good User Ig
		
	- User : {user}
		
	- Dev : @NOOBPRivate _ WATAN
	— — — — — — — — — — — — —
		
		"""))
		
			god=f"""
— — — — — — — — — — — — —
- Good Username 
	
- User ➠ @{user}
	
- By @NOOBPRivate ~ @noob_jee
— — — — — — — — — — — — —
	"""
			requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(god))		
		
		else:
			print(f'User bad     :    @{user}     ')


#— — — — — — — — — — — — —


if HMODE == 3:
	webbrowser.open('https://t.me/NOOBPRivate')
	from rich.panel import Panel
	from  rich import print
	import requests, os, threading
	try:
	    import pazok
	except:
	    os.system('pip install pazok')             
	#====الوان====
	Z = '\033[1;31m'  # أحمر
	X = '\033[1;33m'  # أصفر
	F = '\033[2;32m'  # أخضر
	C = "\033[1;97m"  # أبيض
	B = '\033[2;36m'  # أزرق
	Y = '\033[1;34m'  # أزرق داكن
	W = '\033[0;37m'  # رمادي
	e = "\u001b[38;5;242m" #رمادي داكن
	m = "\u001b[38;5;15m" #ابيض
	E = "\u001b[38;5;8m" #رمادي فاتح
	p = '\x1b[1m'#عريض
	#====الوان====
	
	token = input(f' {E} Enter The {B}Token :{E} ')
	id = input(f' {E} Enter The {B}ID :{E} ')
	os.system('clear')
	def cc():
	    while True:
	        u = pazok.user_ran('1')
	        s = pazok.user_ran('1')
	        r = pazok.user_ran('1')
	        user = u+s+r+'_BoT'
	        headers = {'user-agent': pazok.agnt()}
	        re = requests.get(f"https://fragment.com/username/{user}", headers=headers).text
	        if '104' in re:
	            print(f'{Z} BAD USER : {user} ')        
	        elif 'class="table-cell-status-thin thin-only tm-status-unavail">Unavailable</div>' in re:
	            print(Panel(f"""[green]
		
	— — — — — — — — — — — — —
	- Good User Ig
		
	- User : {user}
		
	- Dev : @NOOBPRivate _ WATAN
	— — — — — — — — — — — — —
		
		"""))
	            RRT = f"""
	            user → `{user}`
	            """
	            pooo = [
	                "قناتي", "https://t.me/NOOBPRivate/","المطور","https://t.me/NOOBPRivate" 
	            ]
	            pazok.tele_ms(token, id, txt=RRT, buttons=pooo)
	
	        else:
	            print(f'{X} eror USER : {user} ')
	
	Threads = []
	for t in range(3):
	    x = threading.Thread(target=cc)
	    x.start()
	    Threads.append(x)
	for Th in Threads:
	    Th.join()	
	    
	    							
	    														
	    																					
if HMODE == 4:
	webbrowser.open('https://t.me/NOOBPRivate')
	import requests,random,os
	from user_agent import generate_user_agent 
	import json,re
	from  rich import print
	import requests,os
	import random
	from rich.panel import Panel
	
	
	e1='\x1b[38;5;196m'#احمر
	a11 = '\x1b[38;5;8m'  # رمادي
	a14 = '\x1b[38;5;153m'  # أزرق فاتح
	a16 = '\x1b[38;5;48m'  # أخضر فاتح
	a19 = '\x1b[38;5;88m'  # أحمر داكن
	a32 = '\x1b[38;5;180m'  # بني فاتح
	a36 = '\x1b[38;5;228m'  # ذهبي فات
	
	l = 'qwertyuiopasdfghjklzxcvbnm1234567890'
	
	ID = input(f'{a32} Enter Id Telegram : ')
	token = input(f'{a14} Enter Token Bot Telegram : ')
	
	while True:
		V1 = "".join(random.choice(l)for i in range(1))
		V2 = "".join(random.choice(l)for i in range(1))
		V3 = "".join(random.choice(l)for i in range(1))
		V4 = "".join(random.choice(l)for i in range(1))
		
		user1 = f'{V1}{V3}.{V4}{V2}'
		user2 = f'{V3}{V1}_{V2}{V4}'
		user3 = f'{V4}.{V3}_{V1}'
		user4 = f'{V3}_{V2}.{V1}'
		user5 = f'{V1}{V4}__{V2}'
		user6 = f'{V2}__{V4}{V3}'
		HMODE = (user1,user2,user3,user4,user5)
		user = random.choice(HMODE)
		url = "https://discord.com/api/v9/auth/register"
		payload = json.dumps({
			  "fingerprint": "1251066764461215794.0hGmY_Ie2DF1XDaXm0bTdSEDLaM",
			  "email": "223chjdbn@gmail.com",
			  "username": user,
			  "global_name": "SIN IS STRONG ",
			  "password": "12341234rfd",
			  "invite": None,
			  "consent": True,
			  "date_of_birth": "2017-05-01",
			  "gift_code_sku_id": None,
			  "promotional_email_opt_in": True
		})
			
		headers = {
			  'User-Agent':str(generate_user_agent()),
			  'Accept-Encoding': "gzip, deflate, br, zstd",
			  'Content-Type': "application/json",
			  'sec-ch-ua': "\"Google Chrome\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
			  'x-fingerprint': "1251066764461215794.0hGmY_Ie2DF1XDaXm0bTdSEDLaM",
			  'x-debug-options': "bugReporterEnabled",
			  'sec-ch-ua-mobile': "?1",
			  'x-discord-timezone': "Asia/Baghdad",
			  'x-discord-locale': "en-US",
			  'sec-ch-ua-platform': "\"Android\"",
			  'origin': "https://discord.com",
			  'sec-fetch-site': "same-origin",
			  'sec-fetch-mode': "cors",
			  'sec-fetch-dest': "empty",
			  'referer': "https://discord.com/register",
			  'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
			  'priority': "u=1, i",
		}
			
		response = requests.post(url, data=payload, headers=headers).json()
		if re.search('USERNAME_ALREADY_TAKEN',str(response)):
			print(Panel(f'[yellow ]BAD  USER :- {user}'))
		elif 'The resource is being rate limited' in str(response):
			print('تم حضرك عد مره اخره بعد خمس دقائق')
			exit()
				
		else:
			print(Panel(f"""[green]
		
		— — — — — — — — — — — — —
		- Good User Ig
		
		- User : @{user}
		
		- Dev : @NOOBPRivate _ WATAN
		— — — — — — — — — — — — —
		
		"""))
		god=f"""
		— — — — — — — — — — — — —
		- Good Username 
		
		- User ➠ {user}
		
		- By @NOOBPRivate ~ @noob_jee
		— — — — — — — — — — — — —
		"""
		requests.get("https://api.telegram.org/bot"+str(token)+"/sendMessage?chat_id="+str(ID)+"&text="+str(god))															


if HMODE == 5:
	webbrowser.open('https://t.me/NOOBPRivate')
	import requests
	import random,os
	from pyfiglet import Figlet
	from colorama import init, Fore, Style
	init(autoreset=True)
	
	
	
	e1='\x1b[38;5;196m'#احمر
	a11 = '\x1b[38;5;8m'  # رمادي
	a14 = '\x1b[38;5;153m'  # أزرق فاتح
	a16 = '\x1b[38;5;48m'  # أخضر فاتح
	a19 = '\x1b[38;5;88m'  # أحمر داكن
	a32 = '\x1b[38;5;180m'  # بني فاتح
	a36 = '\x1b[38;5;228m'  # ذهبي فات
	
	
	
	
	def print_header():
	    fig = Figlet(font='slant')
	    
	def get_user_input():
	    id = input(f'{a32} Enter Id Telegram : ')
	    token = input(f'{a14} Enter Token Bot Telegram : ')
	    webbrowser.open('https://t.me/NOOBPRivate')
	    os.system('clear')
	    return id, token
	
	def check_username_availability(usernames, headers, session):
	    url = f'https://www.tiktok.com/@{usernames}?'
	    response = session.get(url, headers=headers)
	    return response.status_code == 404
	
	def notify_telegram(token, chat_id, message):
	    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}\n𝘽𝙔 @NOOBPRivate"
	    requests.get(url)
	
	def main():
	    print_header()
	    
	    rt = requests.session()
	    litters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
	
	    headers = {
	        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	        'accept-encoding': 'gzip, deflate, br',
	        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
	        'cache-control': 'max-age=0',
	        'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
	        'sec-ch-ua-mobile': '?0',
	        'sec-fetch-dest': 'document',
	        'sec-fetch-mode': 'navigate',
	        'sec-fetch-site': 'same-origin',
	        'sec-fetch-user': '?1',
	        'upgrade-insecure-requests': '1',
	        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
	    }
	    
	    id, token = get_user_input()
	
	    while True:
	        user1 = ''.join(random.choice(litters) for _ in range(4))
	        usernames = user1
	        
	        if check_username_availability(usernames, headers, rt):
	            print(Fore.GREEN + f' [+] {usernames} User is available or blocked | ')# :) user ....
	            notify_telegram(token, id, f'User is available or blocked |  {usernames}')
	        else:
	            print(f' - Bad User : {usernames} ')
	    
	    fig = Figlet(font='slant')
	    print(Fore.BLUE + fig.renderText("HMODE DEV"))
	
	if __name__ == "__main__":
	    main()
		