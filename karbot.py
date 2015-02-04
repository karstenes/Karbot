import ch
import time
prefix = ">" #Set > to a prefix of your choice
class bot(ch.RoomManager):
    def onInit(self):
        self.setNameColor("000000")
        self.setFontColor("000000")
        self.setFontFace("Typewriter")
        self.setFontSize(12)
        self.enableBg()
        self.enableRecording()

    def onConnect(self, room):
        room.message("Connected.")
        print("Connected to "+room.name)

    def onReconnect(self, room):
        print("Reconnected")

    def getAccess(self, user):
        no = 0
        with open("files\mods.txt", "r") as f:
             content = f.readlines()
        length = len(content)
        content = [x.strip('\n') for x in content]
        for x in range(0, length):
            if user.name.lower() == content[no]:
                return 1
            no += 1 
        if user.name.lower() == "karstenes": return 9001 #set karstenes to your username
        else: return 0
        mods.close

    def onMessage(self, room, user, message):
        msgdata = message.body.split(" ",1)
        if len(msgdata) > 1:
            cmd, args = msgdata[0], msgdata[1]
        else:
            cmd, args = msgdata[0],""
        cmd=cmd.lower()

        if len(cmd) >0:
            if cmd[0]==prefix:
                used_prefix = True
                cmd = cmd[1:]
            else:
                used_prefix= False
        else:
            return
        
        if used_prefix and cmd=="cmds":
            room.message("Commands: say, anc, shutup, addmod, mods (WIP), slap, db.")

        if used_prefix and cmd=="lvl":               
            if self.getAccess(user) > 9000:
                room.message(user.name.lower()+"'s level IS OVER 9000!")
            else:
                lvl = str(self.getAccess(user))
                room.message(user.name.lower() + " is level " + lvl)
        
        if used_prefix and cmd=="shutup":
            if args:
                room.message("SHUT UP "+args)
        
        if used_prefix and cmd=="addmod":
            if self.getAccess(user) >= 2:
                if args:
                    print "good"
                    b = args
                    print b
                    mods = open("mods.txt", "a")
                    mods.write(args + "\n");
                    mods.close
                    room.message("Made " + args + " a mod.")
                    print "good"
                else:
                    room.message("I've no one to mod.")
            else:
                room.message("You do not have the required permission to execute this command.")
                    
        if used_prefix and cmd=="say":
            if args:
                room.message(args)
            else: room.message("I've nothing to say.")
            
        if used_prefix and cmd=="slap":
            if args:
                if args == "me" or args == "Me" or args == "myself" or args == "Myself": room.message("slaps " + user.name.lower()) 
                else: room.message("slaps " + args)
            else: room.message("I've no one to slap.")

        if used_prefix and cmd=="db":
            if args:
                time.sleep(1)
                room.message(user.name.lower() + " gathers the dragon balls and summons Shenron.")
                time.sleep(3)
                room.message("Shenron: State your wish.")
                time.sleep(3)
                room.message(user.name.lower() + ": " + args)
                time.sleep(3)
                room.message("Shenron: Your wish has been granted")
                time.sleep(3)
                room.message(user.name.lower() + "'s wish has been granted")
        
        if used_prefix and cmd=="mods":
                no = 0
                with open("mods.txt", "r") as f:
                    content = f.readlines()
                length = len(content)
                content = [x.strip('\n') for x in content]
                for x in range(0, length):
                    if message == "":
                        message = content[no]
                    else:
                        message = message + ", " + content[no]
                    no += 1
                room.message(message)
                                 
        if used_prefix and cmd=="anc":
            if self.getAccess(user) >= 1:
                if args:
                    for _room in self.rooms:
                        _room.message("Announcement from "+user.name.capitalize()+": "+args)
                else:
                    room.message("I've nothing to announce.")
            else:
                room.message("You do not have the required permission to execute this command.")

rooms = ["vegetafanclub"] #set "your group" to the name of your group on chatango

if __name__ == "__main__":
    bot.easy_start(rooms, "kmath", "spr1te") #the sign-in information for your bot's account
