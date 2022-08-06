class Translation(object):


#This will be appeared when anyone use start command

      START = """שלום !
      אני בוט ש @meiremix יצר ואני יכול להמיר קבצי וידאו.
      
      לאופן השימוש כתוב לבוט /help .
"""


#This will be appeared when anyone use help command

      HELP = """**צריך עזרה ?**

1. שלח אליי קובץ או וידאו מטלגרם.

2. שלח אלי תמונה שתהיה על הקובץ או הוידאו.

3. תגיב על הוידאו ששלחת /converttovideo בשביל להפוך אותו לצפייה ישירה.

4. תגיב על הוידאו או הקובץ ששלחת /converttofile בשביל להפוך אותו לקובץ.

נ.ב. אם הבוט נתקע בשלב ההעלאה נסה להמיר מחדש


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
אחוזי התקדמות : {0}%
הושלם ✅: {1}
סך הכל משקל הקובץ 🌀: {2}
מהירות הורדה / העלאה 🚀: {3}/s
זמן סיום משוער 🕰: {4}
"""
       
      DOWNLOAD_PROGRESS = "▪️"
      UPLOAD_PROGRESS = "▫️"

####################################################################################################################################################
####################################################################################################################################################



      DOWNLOAD_START = "מנסה להוריד 📥"
      DOWNLOAD_COMPLETE = "✅ הורד בהצלחה\nמתכונן להעלאה"
      UPLOAD_START = "מנסה להעלות 📤"
      UPLOAD_COMPLETE = "תודה שהשתמשתם בי !"
      SAVED_CUSTOM_THUMB_NAIL = "✅ שמרתי את התמונה בהצלחה. אם לא תשתמש בתמונה היא תמחק בתוך 24 שעות"
      BANNED_TEXT = "אתה חסום. אז לא תוכל להשתמש בי 🐒"
      REPLY_TEXT = "👩‍✈️ הגב על הוידאו או הקובץ שברצונך להמיר"
      DEL_ETED_CUSTOM_THUMB_NAIL = "מחקתי את התמונה בהצלחה ✅"
