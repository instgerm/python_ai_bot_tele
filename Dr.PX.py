import telebot
import requests
import json
from telebot import types

# 🔥 توكن البوت
API_TOKEN = '7590971159:AAEKdP-eSEE99hsy1rTEUAi0zba7BginDoA'
bot = telebot.TeleBot(API_TOKEN)

# 🔥 رابط API الجديد
SERVER_URL = "https://api.blackbox.ai/api/chat"

# 🔥 دالة إرسال البيانات إلى API
def send_to_server(message_text):
    payload = json.dumps({
        "messages": [{"content": message_text, "role": "user"}],
        "model": "deepseek-ai/DeepSeek-V3",  # تم تغيير الموديل إلى DeepSeek-V3
        "max_tokens": 1024
    })
    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(SERVER_URL, headers=headers, data=payload, timeout=30000)
        if response.status_code == 200:
            try:
                data = response.json()
                return data.get("response", response.text)
            except Exception:
                return response.text
        else:
            return f"خطأ: {response.status_code}"
    except Exception as e:
        return f"استثناء: {str(e)}"

# 🔥 أوامر البوت
@bot.message_handler(commands=['start', 's', 'S', 'Start', 'X', 'x', 'hi'])
def send_welcome(message):
    bot.reply_to(message, "✨⚜ *مرحبًا بك في Black GPT mini 3E!* ⚜✨\n\n"
    "🤖 *أقوى بوت ذكاء اصطناعي تم تطويره خلال 47 يوم و 15 ساعة!*\n\n"
    "🚀 *مميزاته:*\n"
    "🔹 حل المسائل الرياضية المعقدة 🧮\n"
    "🔹 البرمجة بجميع لغاتها 💻\n"
    "🔹 الترجمة الاحترافية لأي لغة 🌍\n"
    "🔹 توليد النصوص والإبداع في التعبير ✍️\n"
    "🔹 تحليل الصور واستخراج النصوص منها 🖼️\n"
    "🔹 الردود الذكية في جميع المجالات 🎓\n\n"
    "👑 *تم تطويره وبرمجته بواسطة يوسف احمد ذياب  @tx_5w")

@bot.message_handler(commands=['Info', 'info', 'i', 'I', 'INFO', 'help', 'Help', 'h', 'H'])
def send_info(message):
    bot.reply_to(message, "🤖 *ذكاء اصطناعي متقدم:* يقدم إجابات دقيقة وسريعة باستخدام أحدث التقنيات.\n"
    "🧮 *حل المسائل الرياضية:* يستطيع حل المسائل الرياضية المعقدة بكل سهولة.\n"
    "💻 *دعم لغات البرمجة:* يقدم حلول برمجية وأمثلة على شيفرات بجميع لغات البرمجة.\n"
    "🌍 *ترجمة احترافية:* يترجم النصوص بين عدة لغات بدقة عالية.\n"
    "✍️ *توليد النصوص والإبداع:* يقوم بإنشاء نصوص إبداعية، قصص، أو شروحات تقنية.\n"
    "🖼️ *تحليل الصور واستخراج النصوص:* يستخرج النصوص من الصور ويحللها لتحويلها إلى نصوص قابلة للتفاعل.\n"
    "🎓 *ردود ذكية ومفصلة:* يقدم إجابات مدروسة في مختلف المجالات العلمية والثقافية.\n"
    "🚀 *سرعة استجابة فائقة:* يعمل بسرعة عالية لضمان تجربة مستخدم مريحة.\n"
    "🔒 *أمان وحماية:* يحافظ على خصوصية بياناتك وسرية المحادثات.\n\n"
    "المطور يوسف احمد ذياب @tx_5w 🎲☣")

# 🔥 التعامل مع جميع أنواع الرسائل والوسائط
@bot.message_handler(func=lambda m: True, content_types=[
    'text', 'audio', 'document', 'photo', 'sticker', 'video',
    'video_note', 'voice', 'location', 'contact'
])
def handle_all_messages(message):
    # 🔥 تجهيز الرسالة
    if message.text:
        user_input = message.text
    elif message.photo:
        user_input = "📸 صورة مستلمة!"
    elif message.video:
        user_input = "🎥 فيديو مستلم!"
    elif message.voice:
        user_input = "🎧 رسالة صوتية مستلمة!"
    elif message.document:
        user_input = "📄 ملف مستلم!"
    elif message.audio:
        user_input = "🎵 ملف صوتي مستلم!"
    else:
        user_input = "📌 وسائط أخرى مستلمة!"

    # 🔥 إرسال الرسالة إلى الذكاء الاصطناعي
    server_reply = send_to_server(user_input)

    # 🔥 أزرار التواصل
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("⚡ المطور", url="https://t.me/tx_5w"),
        types.InlineKeyboardButton("🤖 البوت", url="https://t.me/Dark_Gpt_tbot")
    )

    # 🔥 إرسال الرد
    formatted_reply = f"[⚜Black GPT mini 3E⚜]\n\n{server_reply}\n\n تم التطوير بواسطة يوسف احمد ذياب ملاحظة: حالياً البوت مجاني 100%  @tx_5w"
    bot.reply_to(message, formatted_reply, reply_markup=markup)

# 🔥 تشغيل البوت بدون توقف
if __name__ == '__main__':
    print("🚀 البوت يعمل الآن...")
    bot.infinity_polling()
