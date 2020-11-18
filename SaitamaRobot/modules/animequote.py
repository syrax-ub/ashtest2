import html
import random
import SaitamaRobot.modules.animequote_string as animequote_string
from SaitamaRobot import dispatcher
from telegram import ParseMode, Update, Bot
from SaitamaRobot.modules.disable import DisableAbleCommandHandler
from telegram.ext import CallbackContext, run_async

@run_async
def animequote(update: Update, context: CallbackContext):
    args = context.args
    update.effective_message.reply_text(random.choice(animequotestring.ANIMEQUOTE))

__help__ = """
 • `/animequote`*:* for random animequote
"""

ANIMEQUOTE_HANDLER = DisableAbleCommandHandler("animequote", animequote)

dispatcher.add_handler(ANIMEQUOTE_HANDLER)

__mod_name__ = "Animequote"
