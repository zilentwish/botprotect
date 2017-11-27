# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess

azecure = LINETCR.LINE() # az # Login Akun Utama(fungsi Akun Utama Ke Kick bisa Terima Undangan dari Bot Otomatis)
azecure.login(qr=True)
azecure.loginResult()

cl = LINETCR.LINE() #x1
cl.login(qr=True)
cl.loginResult()

ki = LINETCR.LINE() #x2
ki.login(qr=True)
ki.loginResult()

kk = LINETCR.LINE() #x3
kk.login(qr=True)
kk.loginResult()

k1 = LINETCR.LINE() #x4 Backup 
k1.login(qr=True)
k1.loginResult()

print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" •[zilentwish Bot]•
 Coming soon"""

Setgroup =""" 
   [Admin Menu]
===============
•Protect QR
=> Qr on/off
•Protect Join
=> Join on/off
•Mid Via Contact
=> Contact on/off
•Cancel Invited
=> Cancel all
===============
   zilentwish BOT"""
KAC=[cl,ki,kk]
DEF1=[ki,kk] 
DEF2=[cl,kk] 
DEF3=[cl,ki] 
DEF4=[cl,ki,kk] 
DEF5=[cl,ki,kk] 
DEF6=[cl,ki,kk] 
DEF7=[cl,ki,kk] 
DEF8=[cl,ki,kk] 
DEF9=[cl,ki,kk] 
DEF10=[cl,ki,kk] 
mid = cl.getProfile().mid #X1
Amid = ki.getProfile().mid #X2
Bmid = kk.getProfile().mid #X3
Smid = azecure.getProfile().mid #Akun Utama
mid1 = k1.getProfile().mid #X4Backup

Bots=[mid,Amid,Bmid,Smid,mid1,"ud646a3a7064cdcb483df11c01adfdf56"]
admin=["ud646a3a7064cdcb483df11c01adfdf56"] 
owner=["ud646a3a7064cdcb483df11c01adfdf56"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"""Thank you for add me

i am BOT

Warm  regard
 zilentwish
 
""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "cName2":"",
    "cName3":"",
    "cName4":"",
    "cName5":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":True,
    #"Protectjoin":True, 
    "Protectcancl":True,
    "protectionOn":True,
    "atjointicket":True
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if op.param2 not in Bots:
              G = random.choice(KAC).getGroup(op.param1)
              G.preventJoinByTicket = True
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).updateGroup(G)
              random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Dont Open Link or QR Codes")
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if op.param2 not in Bots:
              group = cl.getGroup(op.param1)
              gMembMids = [contact.mid for contact in group.invitee]
              random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    
            if op.param3 in Bmid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)        

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        #------Joined User Kick start------#
        #if op.type == 17: #awal 17 ubah 13
           #if wait["Protectjoin"] == True:
               #if op.param2 not in admin and Bots : # Awalnya admin saja
                   #random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
        #------Joined User Kick start------#
        if op.type == 19: #Member Kena Kick
          if op.param2 not in Bots:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            cl.inviteIntoGroup(op.param1,[op.param3])
        
        if op.type == 19: 
          if op.param3 in admin: #Kalo Admin kena Kick
            if op.param2 in Bots:
              pass
            if op.param2 in owner:
              pass
            else:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                cl.inviteIntoGroup(op.param1,[op.param3])
              
        if op.type == 19:
          try:
            if op.param3 in Smid: #Akun Utama Ke Kick
              G = random.choice(KAC).getGroup(op.param1)
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              G.preventJoinByTicket = False
              random.choice(KAC).updateGroup(G)
              Ticket = random.choice(KAC).reissueGroupTicket(op.param1)
              azecure.acceptGroupInvitationByTicket(op.param1,Ticket)
              time.sleep(0.01)
              G.preventJoinByTicket = True
              random.choice(KAC).updateGroup(G)
              azecure.updateGroup(G)
              wait["blacklist"][op.param2] = True
                                
            if op.param3 in mid:
              if op.param2 in Amid:
                G = ki.getGroup(op.param1)
                G.preventJoinByTicket = False
                ki.updateGroup(G)
                Ticket = ki.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                G.preventJoinByTicket = True
                ki.updateGroup(G)
              else:
                G = ki.getGroup(op.param1)
                ki.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                ki.updateGroup(G)
                Ticket = ki.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)                
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                ki.updateGroup(G)
                wait["blacklist"][op.param2] = True
                
            if op.param3 in Amid:
              if op.param2 in Bmid:
                G = kk.getGroup(op.param1)
                G.preventJoinByTicket = False
                kk.updateGroup(G)
                Ticket = kk.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)                
                G.preventJoinByTicket = True
                kk.updateGroup(G)
              else:
                G = kk.getGroup(op.param1)
                kk.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kk.updateGroup(G)
                Ticket = kk.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)                
                G.preventJoinByTicket = True
                #cl.updateGroup(G)
                kk.updateGroup(G)
                #wait["blacklist"][op.param2] = True
                              
            if op.param3 in Bmid:
              if op.param2 in mid:
                G = cl.getGroup(op.param1)
                G.preventJoinByTicket = False
                cl.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)                
                G.preventJoinByTicket = True
                cl.updateGroup(G)
              else:
                G = cl.getGroup(op.param1)
                cl.kickoutFromGroup(op.param1,[op.param2])
                G.preventJoinByTicket = False
                kk.updateGroup(G)
                Ticket = cl.reissueGroupTicket(op.param1)
                cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)
                kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                time.sleep(0.01)               
                G.preventJoinByTicket = True
                cl.updateGroup(G)
                #ke.updateGroup(G)
                #wait["blacklist"][op.param2] = True
          except:
            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
            cl.inviteIntoGroup(op.param1,[op.param3])
#--------------------------------
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                              
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")                       
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")                        
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        ki.sendText(msg.to,"already")
                        kk.sendText(msg.to,"already")                        
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"aded")
                        ki.sendText(msg.to,"aded")
                        kk.sendText(msg.to,"aded")                        

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        ki.sendText(msg.to,"deleted")
                        kk.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
                        ki.sendText(msg.to,"It is not in the black list")
                        kk.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                else:
                    cl.sendText(msg.to,helpt)
            elif msg.text in ["Admin menu"]:
              if msg.from_ in admin:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                else:
                    cl.sendText(msg.to,Sett)
            elif ("Gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif ("x1 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv1 gn ","")
                    ki.updateGroup(X)
                else:
                    ki.sendText(msg.to,"It can't be used besides the group.")
            elif ("x2 gn " in msg.text):
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Cv2 gn ","")
                    kk.updateGroup(X)
                else:
                    kk.sendText(msg.to,"It can't be used besides the group.")           
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                random.choice(KAC).kickoutFromGroup(msg.to,[midd])
            elif "x2 kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_second kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "x3 kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("_third kick ","")
                kk.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "x2 invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
            elif "x3 invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tinvite ","")
                kk.findAndAddContactsByMid(midd)
                kk.inviteIntoGroup(msg.to,[midd])            
    #--------------- SC Add Admin ---------
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Admin add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
		gs = kk.getGroup(msg.to)
                gs = azecure.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            cl.sendText(msg.to,"admin has been added")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                cl.sendText(msg.to,"Command denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Admin remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)                
                gs = azecure.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            cl.sendText(msg.to,"admin has been deleted")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                cl.sendText(msg.to,"Access denied.")
                cl.sendText(msg.to,"Admin permission required.")
                
            elif msg.text in ["Adminlist","adminlist"]:
              if admin == []:
                  cl.sendText(msg.to,"Admin list is empty")
              else:
                  cl.sendText(msg.to,"Please wait...")
                  mc = "||zilentwish Bot||\n=====================\n"
                  for mi_d in admin:
                      mc += "••>" +cl.getContact(mi_d).displayName + "\n"
                  cl.sendText(msg.to,mc)
                  print "[Command]Admin list executed"
    #--------------------------------------
    #-------------- Add Friends ------------
            elif "Bot Add @" in msg.text:
              if msg.toType == 2:
                if msg.from_ in owner:
                  print "[Command]Add executing"
                  _name = msg.text.replace("Bot Add @","")
                  _nametarget = _name.rstrip('  ')
                  gs = cl.getGroup(msg.to)
                  gs = ki.getGroup(msg.to)
                  gs = kk.getGroup(msg.to)                  
                  targets = []
                  for g in gs.members:
                    if _nametarget == g.displayName:
                      targets.append(g.mid)
                  if targets == []:
                    random.choice(KAC).sendText(msg.to,"Contact not found")
                  else:
                    for target in targets:
                      try:
                        cl.findAndAddContactsByMid(target)
                        ki.findAndAddContactsByMid(target)
                        kk.findAndAddContactsByMid(target)                        
                      except:
                        cl.sendText(msg.to,"Error")
              else:
                cl.sendText(msg.to,"Access Denied")
                cl.sendText(msg.to,"This Command for Owner Only")
                  
    #-------------=SC AllBio=---------------- Ganti Bio Semua Bot Format => Allbio: SUKA SUKA KALIAN :D
            elif "Allbio:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                    cl.sendText(msg.to,"Bio Changes to " + string + "")
    #--------------=Finish=----------------
    #--------------= SC Ganti nama Owner=--------------
            elif "Myname:" in msg.text:
              if msg.from_ in owner:
                string = msg.text.replace("Myname:","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Update Name to : " + string + "")
    #-------------- copy profile----------
            elif "Spam: " in msg.text:
              if msg.from_ in admin:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam: ")+str(txt[1])+" "+str(jmlh + " ","")
                tulisan = jmlh * (teks+"\n")
                 #@reno.a.w
                if txt[1] == "on":
                    if jmlh <= 300:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Over Digit:v")
                elif txt[1] == "off":
                    if jmlh <= 300:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Over Digit :v")
    #-----------------=Selesai=------------------
            elif msg.text in ["Bot contact"]: #kirim Semua Kontak Bot
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
               
            elif msg.text in ["Me"]:
              if msg.from_ in admin:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["Cv2"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)               
            elif msg.text in ["Cancel invite"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        random.choice(KAC).cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Bot cancel invite"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    G = ki.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        ki.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            ki.sendText(msg.to,"No one is inviting")
                        else:
                            ki.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"QR Codes has opened")
                    else:
                        random.choice(KAC).sendText(msg.to,"already opened")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["x1 open qr"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done, QR Codes has opened")
                    else:
                        cl.sendText(msg.to,"QR Codes already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["x2 open qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done, QR Codes Has Opened")
                    else:
                        ki.sendText(msg.to,"QR Codes already open")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")           
            elif msg.text in ["Close qr"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = random.choice(KAC).getGroup(msg.to)
                    X.preventJoinByTicket = True
                    random.choice(KAC).updateGroup(X)
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Done, QR Codes has been closed")
                    else:
                        random.choice(KAC).sendText(msg.to,"QR Codes already closed")
                else:
                    if wait["lang"] == "JP":
                        random.choice(KAC).sendText(msg.to,"Can not be used outside the group")
                    else:
                        random.choice(KAC).sendText(msg.to,"Not for use less than group")
            elif msg.text in ["x2 close qr"]:
                if msg.toType == 2:
                    X = ki.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Done")
                    else:
                        ki.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        ki.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ki.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["x3 close qr"]:
                if msg.toType == 2:
                    X = kk.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Done, QR Codes has been Closed")
                    else:
                        kk.sendText(msg.to,"QR Codes already close")
                else:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kk.sendText(msg.to,"Not for use less than group")            
            elif "jointicket " in msg.text.lower():
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Done,, join group Succes %s" % str(group.name))
                     
            elif "Info group" == msg.text:
              if msg.toType == 2:
                if msg.from_ in admin:
                  ginfo = cl.getGroup(msg.to)
                  try:
                    gCreator = ginfo.creator.displayName
                  except:
                    gCreator = "Error"
                  if wait["lang"] == "JP":
                    if ginfo.invitee is None:
                      sinvitee = "0"
                    else:
                      sinvitee = str(len(ginfo.invitee))
                    if ginfo.preventJoinByTicket == True:
                      QR = "blocked"
                    else:
                      QR = "allowed"
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + "•" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + "•" + gCreator + "\n\n[Group Invitations]\n" + "•Status QR: " + QR + "\n\n[Group Picture]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\n▪Members: " + str(len(ginfo.members)) + "\n▪Pending: " + sinvitee)
                  else:
                    random.choice(KAC).sendText(msg.to,"[Group Name]\n" + str(ginfo.name) + "\n\n[Group ID]\n" + msg.to + "\n\n[Group Creator]\n" + gCreator + "\n\n[Group Invitations]\nGroup Picture:\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                  if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Can not be used outside the group")
                  else:
                    cl.sendText(msg.to,"Not for use less than group")
                
            elif "My mid" == msg.text:
              if msg.from_ in admin:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "Mid bot" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,mid)
                ki.sendText(msg.to,Amid)
                kk.sendText(msg.to,Bmid)
            elif "Mid 1" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,Smid)
            elif "Mid x1" == msg.text:
              if msg.from_ in admin:
                ki.sendText(msg.to,mid)
            elif "Mid x2" == msg.text:
              if msg.from_ in admin:
                kk.sendText(msg.to,Amid)
            elif "Mid x3" == msg.text:
              if msg.from_ in admin:
                cl.sendText(msg.to,Bmid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
              if msg.from_ in admin:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Bot1 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " Done")
            elif msg.text in ["Bot2 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv1 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = ki.getProfile()
                    profile_B.displayName = string
                    ki.updateProfile(profile_B)
                    ki.sendText(msg.to,"name " + string + " Done")
            elif msg.text in ["Bot3 rename "]:
              if msg.from_ in admin:
                string = msg.text.replace("Cv2 rename ","")
                if len(string.decode('utf-8')) <= 20:
                    profile_B = kk.getProfile()
                    profile_B.displayName = string
                    kk.updateProfile(profile_B)
                    kk.sendText(msg.to,"name " + string + " Done")
            elif msg.text in ["Mc "]:
              if msg.from_ in admin:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            #elif msg.text in ["Joinn on","joinn on"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == True:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"Done")
                #else:
                    #wait["Protectjoin"] = True
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"Kick Joined Group On")
                    #else:
                        #cl.sendText(msg.to,"done")
            #elif msg.text in ["Joinn off","joinn off"]:
              #if msg.from_ in admin:
                #if wait["Protectjoin"] == False:
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
                #else:
                    #wait["Protectjoin"] = False
                    #if wait["lang"] == "JP":
                        #cl.sendText(msg.to,"kick Joined Group Off")
                    #else:
                        #cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel all invitations is On")
                    else:
                        cl.sendText(msg.to,"Done, Cancel all invitations already On")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel all invitations is On")
                    else:
                        cl.sendText(msg.to,"Done, Cancel all invitations already On")
            elif msg.text in ["Cancel off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel all invitations is Off")
                    else:
                        cl.sendText(msg.to,"Done, Cancel all invitations already Off")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel all invitations is Off")
                    else:
                        cl.sendText(msg.to,"Done, Cancel all invitations already Off")
            elif msg.text in ["Qr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Codes is On")
                    else:
                        cl.sendText(msg.to,"Done, Protect QR Codes already On")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Codes is On")
                    else:
                        cl.sendText(msg.to,"Done, Protect QR Codes already On")
            elif msg.text in ["Qr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Codes is Off")
                    else:
                        cl.sendText(msg.to,"Done, Protect QR Codes already Off")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Codes already Off")
                    else:
                        cl.sendText(msg.to,"Done, Protect QR Codes already Off")
            elif msg.text in ["Contact On"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mid via Share contact is On")
                    else:
                        cl.sendText(msg.to,"Done, Mid via Share contact already On")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mid via Share contact is On")
                    else:
                        cl.sendText(msg.to,"Done, Mid via Share contact is On")
            elif msg.text in ["Contact off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mid via Share contact is Off")
                    else:
                        cl.sendText(msg.to,"Done, Mid via Share contact already Off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Mid via Share contact is Off")
                    else:
                        cl.sendText(msg.to,"Done, Mid via Share contact already Off")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Auto join on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join is On")
                    else:
                        cl.sendText(msg.to,"Done, Auto join is On")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done, Auto join already On")
                    else:
                        cl.sendText(msg.to,"Done, Auto join already On")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Auto join off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join is Off")
                    else:
                        cl.sendText(msg.to,"Done, Auto join is Off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto join already Off")
                    else:
                        cl.sendText(msg.to,"Done, Auto join already Off")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Auto leave on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto leave is On")
                    else:
                        cl.sendText(msg.to,"Auto leave already On")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done, Auto leave already On")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Auto leave off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto leave is off")
                    else:
                        cl.sendText(msg.to,"Auto leave already Off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto leave Off, Done")
                    else:
                        cl.sendText(msg.to,"Done, Auto leave already Off")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on"]:
              if msg.from_ in admin:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share is On")
                    else:
                        cl.sendText(msg.to,"Done, Share already On")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off"]:
              if msg.from_ in admin:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Share is Off")
                    else:
                        cl.sendText(msg.to,"Done, Share is Off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done, Share already Off")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Set","Status"]:
              if msg.from_ in admin:
                md = "Status Protections\n===============\n"
                if wait["Protectgr"] == True: md+="•Protect QR [On]\n"
                else: md+="•Protect QR [Off]\n"
                if wait["Protectcancl"] == True: md+="•Protect Invite [On]\n"
                else: md+="•Protect Invite [Off]\n"
                if wait["contact"] == True: md+="•Contact [On]\n"
                else: md+="•Contact [Off]\n"
                if wait["autoJoin"] == True: md+="•Auto Join [On]\n"
                else: md +="•Auto Join [Off]\n"
                if wait["autoCancel"]["on"] == True:md+="•Group Cancel " + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= "•Group Cancel [Off]\n"
                if wait["leaveRoom"] == True: md+="•Auto Leave [On]\n"
                else: md+="•Auto Leave [Off]\n"
                if wait["timeline"] == True: md+="•Share [On]\n"
                else:md+="•Share [Off]\n"
                if wait["autoAdd"] == True: md+="•Auto Add [On]\n"
                else:md+="•Auto Add [Off]\n"
                if wait["commentOn"] == True: md+="•Comment [On]\n"
                else:md+="•Comment [Off]\n===================\n   zilentwish   Bot   \n==================="
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Auto add on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add is On")
                    else:
                        cl.sendText(msg.to,"Done, Auto add On")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Auto add off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto add Off")
                    else:
                        cl.sendText(msg.to,"Done, Auto add Off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
#---------------------Sc invite owner ke group------
            elif "/inviteme: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/inviteme: ","")
                if gid == "":
                  cl.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    cl.findAndAddContactsByMid(msg.from_)
                    cl.inviteIntoGroup(gid,[msg.from_])
                  except:
                    cl.sendText(msg.to,"im Not in the Group, maybe")
#--------===---====--------------
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment is On")
                    else:
                        cl.sendText(msg.to,"Done, Comment is On")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Comment is off")
                    else:
                        cl.sendText(msg.to,"Done, Comment is off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv1 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ki.updateGroup(x)
                    gurl = ki.reissueGroupTicket(msg.to)
                    ki.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv2 gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kk.updateGroup(x)
                    gurl = kk.reissueGroupTicket(msg.to)
                    kk.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")                
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Time on"]:
              if msg.from_ in admin:
                if wait["clock"] == True:
                    kk.sendText(msg.to,"Bot 3 hours stay On")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = ki.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Time is On")
            elif msg.text in ["Time off"]:
              if msg.from_ in admin:
                if wait["clock"] == False:
                    kk.sendText(msg.to,"Bot 3 hours stay Off")
                else:
                    wait["clock"] = False
                    kk.sendText(msg.to,"Clock is Off")
        #-------------Fungsi Jam on/off Finish-------------------#           
         
        #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    cl.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"changed to\n\n" + n)
        #-------------Fungsi Change Clock Finish-----------------#           
        
         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Time update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = ki.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    ki.updateProfile(profile)
                    ki.sendText(msg.to,"Time update Succes")
                else:
                    ki.sendText(msg.to,"please, activate a clock")
        #-------------Fungsi Jam Update Finish-------------------#

            elif msg.text == "Cek":
              if msg.from_ in admin:
                cl.sendText(msg.to, "Cek Online/sider.....")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M:%S")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "View":
                 if msg.from_ in admin:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "is Online:%s\n\nis Siders:\n%s===============\n\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "First, Please Type command [Cek] \nand then Type Command [View]\nThank You")
#-----------------------------------------------

#-----------------------------------------------
         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["parabot join"]:
              if msg.from_ in owner:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Ready"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
  
            elif msg.text in ["Go all"]:
              if msg.from_ in owner:
                        G = azecure.getGroup(msg.to)
                        ginfo = azecure.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        azecure.updateGroup(G)
                        invsend = 0
                        Ticket = azecure.reissueGroupTicket(msg.to)
                        cl.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        time.sleep(0.01)
                        G = azecure.getGroup(msg.to)
                        ginfo = azecure.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        azecure.updateGroup(G)
                        print "Ready"
                        G.preventJoinByTicket(G)
                        azecure.updateGroup(G)

            elif msg.text in ["x1 join"]:
              if msg.form_ in admin:
                  x = ki.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  ki.updateGroup(x)
                  invsend = 0
                  Ti = ki.reissueGroupTicket(msg.to)
                  cl.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = ki.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(msg.to)

            elif msg.text in ["x2 join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  ki.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)

            elif msg.text in ["x3 join"]:
              if msg.from_ in admin:
                  x = cl.getGroup(msg.to)
                  x.preventJoinByTicket = False
                  cl.updateGroup(x)
                  invsend = 0
                  Ti = cl.reissueGroupTicket(msg.to)
                  kk.acceptGroupInvitationByTicket(msg.to,Ti)
                  G = cl.getGroup(msg.to)
                  G.preventJoinByTicket = True
                  cl.updateGroup(G)
                  Ticket = cl.reissueGroupTicket(msg.to)                  
            
    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#
            elif msg.text in ["Left all"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)                                             
                        cl.leaveGroup(msg.to)
                    except:
                        pass
            
            elif msg.text in ["Left2"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)                        
                        #cl.leaveGroup(msg.to)
                    except:
                        pass
                      
            elif msg.text in ["x2 left"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["x3 left"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["x2 left"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                    except:
                        pass
            elif msg.text in ["x3 left"]:
	      if msg.from_ in admin:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        kk.leaveGroup(msg.to)
                    except:
                        pass            
    #-------------Fungsi Leave Group Finish---------------#
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag all"]:
            	 if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@null \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["Bot like owner"]: #Semua Bot Ngelike Status Akun Utama
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Ready,, paraBot ready LIKE owner status")
                try:
                  likePost()
                except:
                  pass
                
            elif msg.text in ["Bot like teman"]: #Semua Bot Ngelike Status Teman
              if msg.from_ in owner:
                print "[Command]Like executed"
                cl.sendText(msg.to,"Ready,, paraBot LIKE Freind status")
                try:
                  autolike()
                except:
                  pass
        #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = random.choice(KAC).getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"Good bye")
                        random.choice(KAC).sendText(msg.to,"Please Don't Come Back OKey... Ahhhaaayyyy")
                        return
                    for jj in matched_list:
                        try:
                            klist=[cl,ki,kk,kc,ks,ka,kb,ku,ke,ko]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
        #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Ready bot" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("hai","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)                    
                    random.choice(KAC).sendText(msg.to,"i am sory")
                    random.choice(KAC).sendText(msg.to,"Thank you all..")                    
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    random.choice(KAC).sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KAC).sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in admin and Bots:
                            try:
                                klist=[cl,ki,kk]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                random.choice(KAC).sendText(msg.to,"Sorry Brader")
                                random.choice(KAC).sendText(msg.to,"Sorry Sister")
                                random.choice(KAC).sendText(msg.to,"Sorry Gaeeeessss")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
              if msg.from_ in admin:
                nk0 = msg.text.replace("Nk ","")
                nk1 = nk0.lstrip()
                nk2 = nk1.replace("@","")
                nk3 = nk2.rstrip()
                _name = nk3
                gs = cl.getGroup(msg.to)
                ginfo = cl.getGroup(msg.to)
                gs.preventJoinByTicket = False
                cl.updateGroup(gs)
                invsend = 0
                Ticket = cl.reissueGroupTicket(msg.to)
                azecure.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.01)
                targets = []
                for s in gs.members:
                    if _name in s.displayName:
                       targets.append(s.mid)
                if targets == []:
                   sendMessage(msg.to,"user does not exist")
                   pass
                else:
                   for target in targets:
                      try:
                        azecure.kickoutFromGroup(msg.to,[target])
                        print (msg.to,[g.mid])
                      except:
                        azecure.leaveGroup(msg.to)
                        gs = cl.getGroup(msg.to)
                        gs.preventJoinByTicket = True
                        cl.updateGroup(gs)
                        gs.preventJoinByTicket(gs)
                        cl.updateGroup(gs)
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
              if msg.from_ in admin:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = random.choice(KAC).getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            random.choice(KAC).sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    random.choice(KAC).sendText(msg.to,"Succes Plak")
                                except:
                                    random.choice(KAC).sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Banned] Succes"
                    _name = msg.text.replace("Banned @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)                   
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Please,Dont Banned Bot")
                        ki.sendText(msg.to,"Please,Dont Banned Bot")
                        kk.sendText(msg.to,"Please,DOnt Banned Bot")                        
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                random.choice(KAC).sendText(msg.to,"Succes... Account has been banned")
                            except:
                                random.choice(KAC).sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "[Unban] Succes"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)                    
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not Found.....")
                        ki.sendText(msg.to,"Not Found.....")
                        kk.sendText(msg.to,"Not Found.....")                        
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Account is Clear")
                            except:
                                ki.sendText(msg.to,"Error")
          #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["/cut"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"Calm down baby...!! z !!")
                ki.sendText(msg.to,"Calm down baby...!! i !!")
                kk.sendText(msg.to,"Calm down baby...!! l !!")
                cl.sendText(msg.to,"Calm down baby...!! e !!")
                ki.sendText(msg.to,"Calm down baby...!! n !!")
                kk.sendText(msg.to,"Calm down baby...!! t !!")
                cl.sendText(msg.to,"Calm down baby...!! w !!")
                ki.sendText(msg.to,"Calm down baby...!! i !!")
                kk.sendText(msg.to,"Calm down baby...!! s !!")
                cl.sendText(msg.to,"Calm down baby...!! h !!")
                ki.sendText(msg.to,"Calm down baby...!! B !!")
                kk.sendText(msg.to,"Calm down baby...!! O !!")
                cl.sendText(msg.to,"Calm down baby...!! T !!")
                ki.sendText(msg.to,"Calm down baby...!!•••!!")
                kk.sendText(msg.to,"Calm down baby...!! z !!")
                cl.sendText(msg.to,"Calm down baby...!! i !!")
                ki.sendText(msg.to,"Calm down baby...!! l !!")
                kk.sendText(msg.to,"Calm down baby...!! e !!")
                cl.sendText(msg.to,"Calm down baby...!! n !!")
                ki.sendText(msg.to,"Calm down baby...!! t !!")
                kk.sendText(msg.to,"Calm down baby...!! w !!")
                cl.sendText(msg.to,"Calm down baby...!! i !!")
                ki.sendText(msg.to,"Calm down baby...!! s !!")
                kk.sendText(msg.to,"Calm down baby...!! h !!")
                cl.sendText(msg.to,"Calm down baby...!! B !!")
                ki.sendText(msg.to,"Calm down baby...!! O !!")
                kk.sendText(msg.to,"Calm down baby...!! T !!")
                cl.sendText(msg.to,"Calm down baby...!!•••!!")
                ki.sendText(msg.to,"Calm down baby...!! z !!")
                kk.sendText(msg.to,"Calm down baby...!! i !!")
		cl.sendText(msg.to,"Calm down baby...!! l !!")
                ki.sendText(msg.to,"Calm down baby...!! e !!")
                kk.sendText(msg.to,"Calm down baby...!! n !!")
                cl.sendText(msg.to,"Calm down baby...!! t !!")
                ki.sendText(msg.to,"Calm down baby...!! w !!")
                kk.sendText(msg.to,"Calm down baby...!! i !!")
                cl.sendText(msg.to,"Calm down baby...!! s !!")
                ki.sendText(msg.to,"Calm down baby...!! h !!")
                kk.sendText(msg.to,"Calm down baby...!! B !!")
                cl.sendText(msg.to,"Calm down baby...!! O !!")
                ki.sendText(msg.to,"Calm down baby...!! T !!")
                kk.sendText(msg.to,"Calm down baby...!!•••!!")
                cl.sendText(msg.to,"Calm down baby...!!• •!!")
                ki.sendText(msg.to,"Calm down baby...!! • !!")
                kk.sendText(msg.to,"Calm down baby...!!cut!!")
                
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in owner:
                 bctxt = msg.text.replace("Bc ","")
                 a = cl.getGroupIdsJoined()
                 a = ki.getGroupIdsJoined()
                 a = kk.getGroupIdsJoined()                 
                 for taf in a:
                     cl.sendText(taf, (bctxt))
                     ki.sendText(taf, (bctxt))
                     kk.sendText(taf, (bctxt))                     
      #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["Lg"]: #Melihat List Group
              if msg.from_ in admin:
                 gids = cl.getGroupIdsJoined()
                 h = ""
                 for i in gids:
                  #####gn = cl.getGroup(i).name
                  h += "•%s Member\n" % (cl.getGroup(i).name   +": "+str(len(cl.getGroup(i).members)))
                 cl.sendText(msg.to,"=======[List BOT in Group]======\n"+ h +"Total Group: "+str(len(gids)))
                
            elif msg.text in ["Lg2"]: #Melihat List Group + ID Groupnya (Gunanya Untuk Perintah InviteMeTo:)
              if msg.from_ in owner:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "•%s:" "\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
      #--------------List Group------------
       #------------ Keluar Dari Semua Group------
            elif msg.text in ["Out all group"]: # Keluar Dari Semua Group Yang Di dalem nya  ada bot(Kalo Bot Kalian Nyangkut di Group lain :D)
              if msg.from_ in owner:
                 gid = cl.getGroupIdsJoined()
                 gid = ki.getGroupIdsJoined()
                 gid = kk.getGroupIdsJoined()                 
                 for i in gid:                   
                   ki.leaveGroup(i)
                   kk.leaveGroup(i)
                   cl.leaveGroup(i)
                 if wait["lang"] == "JP":
                   cl.sendText(msg.to,"Yiiiihhhaaaaaaa")
                 else:
                   cl.sendText(msg.to,"Declined all invitations")
 #------------------------End---------------------

 #-----------------End-----------
            elif msg.text in ["Hai"]:
                ki.sendText(msg.to,"Hi,, Bro/sis ")
                kk.sendText(msg.to,"Hi,, ono oppo ?")
                
#-----------------------------------------------
            elif msg.text in ["Cv say hinata pekok"]:
                ki.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Hinata pekok 􀜁􀅔Har Har􏿿")               
            elif msg.text in ["Cv say didik pekok"]:
                ki.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Didik pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say bobo ah","Bobo dulu ah"]:
                ki.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Have a nice dream Cv 􀜁􀅔Har Har􏿿")
            elif msg.text in ["Cv say chomel pekok"]:
                ki.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
                kk.sendText(msg.to,"Chomel pekok 􀜁􀅔Har Har􏿿")
            elif msg.text in ["#welcome"]:
                ki.sendText(msg.to,"Welcome to the jungle")
                kk.sendText(msg.to,"Please enjoy... ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                ki.sendText(msg.to,"Ping pong pang pung peng")
                kk.sendText(msg.to,"Ping pong pang pung peng")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Cek bot"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,"•Bot1 Active...√")
                ki.sendText(msg.to,"•Bot2 Active....√")
                kk.sendText(msg.to,"•Bot3 Active.....√")                
                cl.sendText(msg.to,"ParaBot ready for Protection Group")
      #-------------Fungsi Respon Finish---------------------#
                            

      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu dechhh ,,,, aahhaaayyyy")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed bot"]:
              if msg.from_ in admin and owner:
                start = time.time()
                cl.sendText(msg.to, "Please wait...")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%s Second" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
              if msg.from_ in owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"Send contact")
                ki.sendText(msg.to,"Send contact")
                kk.sendText(msg.to,"Send contact")
            elif msg.text in ["Unban"]:
              if msg.from_ in owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"Send contact")
                ki.sendText(msg.to,"Send contact")
                kk.sendText(msg.to,"Send contact")
      #-------------Fungsi Banned Send Contact Finish------------------#
            elif msg.text in ["Creator"]:
              msg.contentType = 13
              msg.contentMetadata = {'mid': 'ud646a3a7064cdcb483df11c01adfdf56'}
              cl.sendText(msg.to,"===zilentwish Creator===")
              cl.sendMessage(msg)
              #cl.sendText(msg.to,"======================")
              cl.sendText(msg.to,"Itu Creator PeA, peB, peC - peZ, Dudul, Oneng, Pemalu, Pemahat, Pemaku, Penjahat, kudisan, Panuan, Kurapan, Buncit, Cacingan kribo, Hitam, Hidup lagi")
                
      #-------------Fungsi Chat ----------------
            elif msg.text in ["bot","Bot"]:
                 quote = ['siap Bozz','Jelek lu','Istri yang baik itu Istri yang Mengizinkan Suaminya untuk Poligami 😂😂😂.','Kunci Untuk membuat pasangan Bahagia itu cuma satu..\nIzinkan pasagan kamu punya tikungan tanjakan turunan','Ah Kamvret Lu','Muke gileeee','Ada Orang gak disini']
                 psn = random.choice(quote)
                 cl.sendText(msg.to,psn)
            
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    random.choice(KAC).sendText(msg.to,"There was no banned user")
                else:
                    random.choice(KAC).sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
    #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    random.choice(KAC).sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        random.choice(KAC).sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                        random.choice(KAC).kickoutFromGroup(msg.to,[jj])
                    random.choice(KAC).sendText(msg.to,"Blacklist Go away")
                    random.choice(KAC).sendText(msg.to,"Blacklist Go away")
                    random.choice(KAC).sendText(msg.to,"Blacklist Go away")
                    random.choice(KAC).sendText(msg.to,"Blacklist Go away")
            elif msg.text in ["Clear"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = cl.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            cl.updateGroup(group)
                    except:
                        cl.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    cl.sendText(msg.to,str(cl.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        cl.sendText(msg.to,str(e))
                    except:
                        pass
#---------CCTV-----------
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n•" + Name
                wait2['ROM'][op.param1][op.param2] = "•" + Name
            else:
              cl.sendText
          except:
             pass
#---------------------
        if op.type == 17:
           if op.param2 in Bots:
              return
           ginfo = cl.getGroup(op.param1)
           random.choice(KAC).sendText(op.param1, "Welcome to Group" + str(ginfo.name))
           random.choice(KAC).sendText(op.param1, "Founder Group " + str(ginfo.name) + " :\n" + ginfo.creator.displayName)
           random.choice(KAC).sendText(op.param1,"Chat and have fun, anggap aja rumah sendiri ,,ahhaaayyyy")
           print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
           if op.param2 in Bots:
              return
           random.choice(KAC).sendText(op.param1, "aahhaaaayyy leave group")
           print "MEMBER HAS LEFT THE GROUP"
#------------------------
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def autolike():
    for zx in range(0,20):
      hasil = cl.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          azecure.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          azecure.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto Like by zilentwish")
          cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"")
          ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          ki.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"")
          kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          kk.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"")
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)
#thread3 = threading.Thread(target=autolike)
#thread3.daemon = True
#thread3.start()
#--------------------
def likePost():
    for zx in range(0,20):
        hasil = cl.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in owner:
                try:
                    cl.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    ki.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    kk.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)                    
                    cl.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"Auto like by zilentwish")
                    print "Like"
                except:
                    pass
            else:
                print "Status Done"
                
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)
                
                profile11 = azecure.getProfile()
                profile11.displayName = wait["cName11"]
                azecure.updateProfile(profile11)
                
                profile12 = k1.getProfile()
                profile12.displayName = wait["cName12"]
                k1.updateProfile(profile12)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
