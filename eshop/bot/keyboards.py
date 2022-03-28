from telegram import ReplyKeyboardMarkup
from .api import get_categories
main_markup = ReplyKeyboardMarkup(
    [['Kategoriyalar'],
    ['🛒Savatcha','⏱Buyurtmalar tarixi']],
    resize_keyboard=True
)

categories_markup = ReplyKeyboardMarkup(
    [
        [c['name']]
        for c in get_categories()
    ],
    resize_keyboard=Truezz
)


