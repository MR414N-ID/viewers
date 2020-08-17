
#ihh mau recode😒 dasar nob nggak bisa buat sendiri apa
#wkwkwkw kalo mau nggak apa apa lah aku ikhlas


import os,sys,time,json,requests,re,random
def clear():
    os.system("clear")
def balik():
    f = input("\033[1;92m Coba Lagi yah bang YouTubers 🤣😂😂🤣🤣?\033[1;97m (y/t): ")
    if f == "y":
        subprocess.call("python views.py",shell=True)
    elif f == "t":
        print ("\033[1;91mExit!!\033[1;97m")
        sys.exit()

def load():
    for x in range(1,101):
        time.sleep(1./15)
        print ("\r\033[1;97m{\033[1;91m!\033[1;97m}Loading\033[90m...\033[1;93m"+str(x)+"\033[1;97m%", end="", flush=True)
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./25)
clear()
os.system("print MR.414N|figlet -f banner|lolcat -a")
os.system("print LOVE️|figlet -f banner|lolcat -a -i")
os.system("print LIA|figlet -f banner|lolcat -a")

clear()
os.system("print ==========================================|lolcat -a")
os.system("print author=MR.414N|lolcat -a")
os.system("print CINTA KU LIA😙😙😙❤️❤️❤️😙😙😙|lolcat -a")
os.system("print WA=082292838634|lolcat -a")
os.system("print TEAM=INDONESIAN MULTITALENTED COMUNITY|lolcat -a")
os.system("print ==========================================|lolcat -a")
f=input("""
\033[1;93m(1) \033[1;93mambil point
\033[1;93m(2) \033[1;93mbeli Views
\033[98m> \033[1;93m""")
if f == "1":
   try:
       mail=input("\033[1;97m{\033[1;92m+\033[1;97m}Email: \033[1;92m")
       ua={
       "Content-Type": "application/x-www-form-urlencoded",
       "Host": "video.sub4subnow.com",
       "Connection": "Keep-Alive",
       "Accept-Encoding": "gzip",
       "User-Agent": "okhttp/3.11.0"}
       dat={
       "checksum":"943e7b4ad1515616f5392af47c459199",
       "millis":"1595652080233",
       "thumbUrl":"",
       "userName":"",
       "version":"61",
       "email":mail}
       r=requests.post("https://video.sub4subnow.com/users.logInvaaa3", data=dat, headers=ua).text
       js=json.loads(r)
       su=js["accessToken"]
       si=js["userInfor"]["userId"]
       xi=js["userInfor"]["userName"]
       se=js["userInfor"]["point"]
       print ("\033[1;97m[\033[1;96m•\033[1;97m]YourPoint:\033[1;92m",se)
       while True:
             ji={
             "maxResult":"1",
             "lastCampaignId":"393646",
             "orderBy":"0",
             "accessToken":su,
             "type":"0",
             "userId":si,
             "version":"61",
             "countryId":"0"}
             d=requests.post("https://video.sub4subnow.com/campaign.getAllViewCampaigns", data=ji, headers=ua).text
             hh=json.loads(d)
             for x in hh["campaigns"]:
                 ne=x['campaignId']
                 be=x['thumbUrl']
             w={
             "campaignId":ne,
             "accessToken":su,
             "thumbUrl":be,
             "userName":xi,
             "userId":si,
             "version":"61"
             }
             for i in range(1,4):
                 s=requests.post("https://video.sub4subnow.com/campaign.updateCampaignProgress", data=w, headers=ua).text
             c={
             "userId":si,
             "millis":"1595652080233",
             "version":"61",
             "accessToken":su,
             "userName":xi,
             "thumbUrl":be,
             "campaignId":ne,
             "checksum":"943e7b4ad1515616f5392af47c459199"
             }
             g=requests.post("https://video.sub4subnow.com/campaign.subOrView", data=c, headers=ua).text
             jj=json.loads(g)
             if jj["success"]==True:
                print ("\033[1;97m{\033[1;92m+\033[1;97m}Reward: \033[1;92m",jj["point"])
             else:
                print ("\033[1;97m{\033[1;91m!\033[1;97m}Reward: \033[1;91mFailed!!\033[00m")
   except NameError:
          print ("Wrong!!")
   except KeyError:
          print ("exit")
   except KeyboardInterrupt:
          print ("exit")
   except requests.exceptions.ConnectionError:
          print ("Connection error")

elif f == "2":
     mail=input("\033[1;97m{\033[1;92m+\033[1;97m}Email: \033[1;92m")
     hd={
     "Content-Type": "application/x-www-form-urlencoded",
     "Host": "video.sub4subnow.com",
     "Connection": "Keep-Alive",
     "Accept-Encoding": "gzip",
     "User-Agent": "okhttp/3.11.0"
     }
     dat={
     "checksum":"943e7b4ad1515616f5392af47c459199",
     "millis":"1595652080233",
     "thumbUrl":"",
     "userName":"",
     "version":"61",
     "email":mail}
     r=requests.post("https://video.sub4subnow.com/users.logInvaaa3", data=dat, headers=hd).text
     js=json.loads(r)
     su=js["accessToken"]
     hi=js["userInfor"]["userId"]
     xi=js["userInfor"]["userName"]
     he=js["userInfor"]["point"]
     print ("\033[1;97m[\033[1;96m•\033[1;97m]YourPoint:\033[1;92m",he)
     print ("""
\033[1;97m\t\t\033[1;91mMENU😗
\n\033[1;97m10😀views = 100Point  | 50😁views = 500Point
100😂views = 1000 Point | 300🤣iews = 3000 Point
500😂😂views = 5000 Point | 1000🤣🤣views = 10000 Point
\033[1;94m________________________________________________""")
     ur=input('\033[1;96m{\033[1;92m•\033[1;96m}id vidio?😗: \033[1;93m')
     ua={
     "Accept-Encoding": "gzip",
     "User-Agent": "Google-API-Java-Client Google-HTTP-Java-Client/1.22.0 (gzip)",
     "x-android-package": "subexchange.hdcstudio.dev.subexchange",
     "x-android-cert": "7FAB56149399CE1B3D56AD22C9B847BC0B0B596A",
     "Host": "www.googleapis.com",
     "Connection": "Keep-Alive",
     }
     r=requests.get(f"https://www.googleapis.com/youtube/v3/videos?id={ur}&key=AIzaSyAlwz_Vj6mWIBgqgKD0rQwI82Fa4S3cskk&part=id,%20snippet", headers=ua).text
     h=json.loads(r)
     w=h["items"]
     for x in w:
         tb=x["snippet"]["thumbnails"]["default"]["url"]
         tit=x["snippet"]["title"]
         id=x["id"]
     mb=requests.get(tb, headers={"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; SM-A107F Build/QP1A.190711.020)","Host": "i.ytimg.com","Connection": "Keep-Alive","Accept-Encoding": "gzip"})
     tl=input("\033[1;97m{\033[1;91m•\033[1;97m}tambah tontonan?: \033[1;92m")
     dt={
     "videoId":ur,
     "accessToken":su,
     "type":"0",
     "userName":xi,
     "userId":hi,
     "version":"61",
     "countryId":"0",
     "total":tl,
     "videoName":tit,
     "checksum":"05d9da390e6eb65fb64a580a2a27a95e",
     "videoTime":"60",
     "millis":"1597342739366",
     "thumbUrl":tb
     }
     kata("\033[1;97m{\033[1;92m+\033[1;97m}judul: \033[1;92m"+str(tit))
     kata("\033[1;97m{\033[1;92m+\033[1;97m}Views: \033[1;92m"+str(tl))
     load()
     br=requests.post("https://video.sub4subnow.com/campaign.createNewvaaa3", data=dt, headers=hd).text
     c=json.loads(br)
     tod=c["campaignId"]
     if c['success'] == True:
        print ("\r\n\033[1;94m________________________________________________\n\033[1;96m{\033[1;92m+\033[1;96m}\033[1;93mRespon: \033[1;92mberhasil\n\033[1;96m{\033[1;92m•\033[1;96m}Id:\033[1;92m",tod,"\n\033[1;97m{\033[1;96m•\033[1;96m}sisa point:\033[1;99m",c["point"])
        balik()
     else:
        print ("\033[1;97m{\033[1;93m!\033[1;97m}Respon: \033[1;91mgagal😂!\033[00m")
        balik()
