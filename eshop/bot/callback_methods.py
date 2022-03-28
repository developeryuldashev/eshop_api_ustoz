# callback methoods------------------------------------------------------
from telegram import Update
from telegram.ext import CallbackContext

from bot.inline_keyboards import products_keyboard
from bot.keyboards import main_markup, categories_markup
from bot.make_image import get_gr_photo


def start(update:Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Salom bu eshopning boti!!!",
        reply_markup=main_markup
    )

def text_message(update:Update, context: CallbackContext):
    message = update.message.text
    if message == 'Kategoriyalar':
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=f"Marhamat kerakli kategoriyani tanlang",
            reply_markup=categories_markup
        )
    elif message == "Ortga":
        context.bot.send_message(
            chat_id = update.effective_chat.id,
            text= "Bosh sahifa",
            reply_markup=main_markup
        )
    else:
        p_keyboard,keys = products_keyboard(message,page=1)
        context.bot.send_photo(chat_id=update.effective_chat.id,photo=open(get_gr_photo(keys),'rb'))
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text='Kerakli mahsulotni tanlang:',
            reply_markup=p_keyboard
        )

def photo_message(update:Update,context:CallbackContext):

    context.bot.send_photo(chat_id=update.effective_chat.id,photo=open('img.png','rb'))
# end callback methoods------------------------------------------------------
