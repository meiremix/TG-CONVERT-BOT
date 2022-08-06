class Translation(object):


#This will be appeared when anyone use start command

      START = """שלום !
      אני בוט ש @meiremix יצר ואני יכול להמיר קבצי וידאו.
      
      לאופן השימוש כתוב לבוט @help .
"""


#This will be appeared when anyone use help command

      HELP = """**צריך עזרה ?**

1. שלח אליי קובץ או וידאו מטלגרם.

2. שלח אלי תמונה שתהיה על הקובץ או הוידאו.

3. תגיב על הוידאו ששלחת /converttovideo בשביל להפוך אותו לצפייה ישירה.

4. תגיב על הוידאו או הקובץ ששלחת /converttofile בשביל להפוך אותו לקובץ.


"""


#Please don't change this about command 🙏

      ABOUT = """
**📝 Language:** Python 3

**🧰 Framework:** Pyrogram

**👨‍💻 Developer:** 

**💻 Source Code:**[Press Me](https://github.com/meiremix/TG-CONVERT-BOT)

"""
#Ns anonymous
####################################################################################################################################################
####################################################################################################################################################



#If you set the password for the bot if anyone use the bot without logging in this text will appear

      NOT_LOGGED_TEXT = """ This bot was a private bot you need to login using the password.
For logging in use command <code>/login BotPassword</code>. And then use me 🥰"""


#This will be sent to the user when the user logged successfully

      SUCESS_LOGIN = """You are successfully logged in. So you can use me for today.
You access will be revoke by tomorrow"""


# This will be show when an user send wrong password

      WRONG_PWD = """This is a wrong password 🔐 please try with correct password"""


# This will appear if the user is already logged

      EXISTING_USER = "You are already logged in you can use me"

####################################################################################################################################################
####################################################################################################################################################


#DON'T CHANGE THE NUMBERS IN THE FLOWER BRACKETS AND THE ORDER OF PERCENTAGE, DONE, TOTAL, SPEED, ETA ONLY CHANGE THE THEME 

      PROGRESS = """
Percentage : {0}%
Done ✅: {1}
Total 🌀: {2}
Speed 🚀: {3}/s
ETA 🕰: {4}
"""
       
      DOWNLOAD_PROGRESS = "▪️"
      UPLOAD_PROGRESS = "▫️"

####################################################################################################################################################
####################################################################################################################################################



      DOWNLOAD_START = "Trying to Download 📥"
      DOWNLOAD_COMPLETE = "✅ Media Downloaded successfully\nPreparing for upload"
      UPLOAD_START = "Trying to Upload 📤"
      UPLOAD_COMPLETE = "THANKS FOR USING ME"
      SAVED_CUSTOM_THUMB_NAIL = "✅ Saved Thumbnail Successfully. This will be deleted in 24hrs"
      BANNED_TEXT = "YOU ARE BANNED. SO YOUR ARE NOT ABLE TO USE ME 🐒"
      REPLY_TEXT = "👩‍✈️ Reply to the media which you need to convert"
      DEL_ETED_CUSTOM_THUMB_NAIL = "Thumbnail Deleted Successfully ✅"
