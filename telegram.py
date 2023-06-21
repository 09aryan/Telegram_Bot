import telegram.ext
Token="139716903:AAGtta4RpDh2hO3hP7GorRcmOb1G1B1LP4c"
updater=telegram.ext.Updater("6139716903:AAGtta4RpDh2hO3hP7GorRcmOb1G1B1LP4c")
dispatcher=updater.dispatcher

def start(update,context):
    update.message.reply_text("HEllo To My telegramBot")
    
def help(update,context):
       update.message.reply_text(
           """
           /start -> Welcome to the channel
    /help -> This message
    /content -> This bot offers various contents
    /Songs  -> The first video from Song Playlist
    /cartoons -> The first video cartoon
    /Anime -> The first video from Anime Playlist
    /contact -> contact information 
                                 """) 
def content(update,context):
    update.message.reply_text("We have various playlist avilable ")
    
def Songs(update,context):
    update.message.reply_text("link : https://youtu.be/DAqxAqq_jhg") 
def cartoon(update,context):
    update.message.reply_text("link : https://youtu.be/BstW5GDKVMU ") 
def Anime(update,context):
    update.message.reply_text("link: https://youtu.be/F8CoTOtjH9w ") 
def contact(update,context):
    update.message.reply_text("Contact us on our website") 
    
    
dispatcher.add_handler(telegram.ext.CommandHandler('start',start))
dispatcher.add_handler(telegram.ext.CommandHandler('Songs',Songs))
dispatcher.add_handler(telegram.ext.CommandHandler('cartoons',cartoon))
dispatcher.add_handler(telegram.ext.CommandHandler('Anime',Anime))
dispatcher.add_handler(telegram.ext.CommandHandler('contact',contact))
dispatcher.add_handler(telegram.ext.CommandHandler('help',help))
                    
updater.start_polling()
updater.idle()