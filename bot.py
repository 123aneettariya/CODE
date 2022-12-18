import telegram.ext

from telegram.ext import CommandHandler, Updater
from telegram.error import Conflict

updater =Updater (token=&#39;5736838466:AAFts2vIdn0LhBNY1mJF81LlPvoq_o5p-aE&#39;,
use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
update.message.reply_text(&quot;Welcome aboard!This friendly bot will provide you with all the
required resources and stuff you wish to learn.It doesn&#39;t matter if you don&#39;t know nothing about
programming , we are here to help you out.Every pro began as an amateur&quot;)
def content(update, context):
update.message.reply_text(

&quot;&quot;&quot;
You have choosed the right path.This bot will provide you with:
➡Basics_of_programming
➡Roadmaps
➡Downloading_code_editors
➡Programming_languages

&quot;&quot;&quot;

)

def start(update, context):
update.message.reply_text(&quot;We have various learning resources available to boost your
knowledge and skills&quot;)

def Basics_of_programming(update, context):
update.message.reply_text(&quot;https://www.educative.io/answers/what-are-the-basic-fundamental-
concepts-of-programming&quot;)
update.message.reply_text(&quot;https://youtu.be/zOjov-2OZ0E&quot;)

def Roadmaps(update, context):
update.message.reply_text(
&quot;&quot;&quot;
➡Python
➡C
➡CSS
➡HTML
➡Java
➡Node.js

&quot;&quot;&quot;)
def Python(update, context):
update.message.reply_text(&quot;https://copyassignment.com/complete-python-roadmap-for-
beginners-in-2022/&quot;)
def C(update, context):
update.message.reply_text(&quot;https://www.geeksforgeeks.org/c-programming-for-beginners-a-20-
day-curriculum/amp/&quot;)
def CSS(update, context):
update.message.reply_text(&quot;https://plainenglish.io/blog/the-modern-css-developer-roadmap&quot;)
def HTML(update, context):
update.message.reply_text(&quot;https://blog.kritikapattalam.com/html-roadmap&quot;)
def Java(update, context):
update.message.reply_text(&quot;https://roadmap.sh/java&quot;)
def Nodejs(update, context):
update.message.reply_text(&quot;https://roadmap.sh/nodejs&quot;)

def Downloading_code_editors(update, context):
update.message.reply_text(&quot;&quot;&quot;
➡Visual Studio Code
➡Sublime Text
➡Atom
&quot;&quot;&quot;)

def VScode(update, context):
update.message.reply_text(&quot;https://youtu.be/JPZsB_6yHVo&quot;)
def Sublime(update, context):
update.message.reply_text(&quot;https://youtu.be/JPZsB_6yHVo&quot;)
def Atom(update, context):
update.message.reply_text(&quot;https://youtu.be/yPFi103-G08&quot;)

def Programming_languages(update, context):
update.message.reply_text(&quot;&quot;&quot;
➡Python_tutorial
➡C_tutorial
➡CSS_tutorial
➡HTML_tutorial
➡Java_tutorial
➡Node.js_tutorial

&quot;&quot;&quot;)

def Python_tutorial(update, context):
update.message.reply_text(&quot;https://www.w3schools.com/python/&quot;)
update.messahe.reply_text(&quot;https://youtu.be/kqtD5dpn9C8&quot;)

def C_tutorial(update, context):
update.message.reply_text(&quot;https://www.w3schools.com/c/&quot;)
update.message.reply_text(&quot;https://youtu.be/8PopR3x-VMY&quot;)
def CSS_tutorial(update, context):
update.message.reply_text(&quot;https://www.w3schools.com/w3css/defaulT.asp&quot;)
update.message.reply_text(&quot;https://youtu.be/1PnVor36_40&quot;)
def HTML_tutorial(update, context):
update.message.reply_text(&quot;https://www.w3schools.com/html/&quot;)
update.message.reply_text(&quot;https://youtu.be/qz0aGYrrlhU&quot;)
def Java_tutorial(update, context):
update.message.reply_text(&quot;https://www.w3schools.com/java/default.asp&quot;)
update.message.reply_text(&quot;https://youtu.be/eIrMbAQSU34&quot;)
def Nodejs_tutorial(update, context):
update.message.reply_text(&quot;https://www.w3schools.com/nodejs/&quot;)
update.message.reply_text(&quot;https://youtu.be/TlB_eWDSMt4&quot;)

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;start&#39;,start))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;content&#39;,content))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Basics_of_programming&#39;,Basics_of_progra
mming))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Roadmaps&#39;,Roadmaps))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Python&#39;,Python))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;C&#39;,C))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;CSS&#39;,CSS))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;HTML&#39;,HTML))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Java&#39;,Java))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Nodejs&#39;,Nodejs))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Downloading_code_editors&#39;,Downloading_
code_editors))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;VScode&#39;,VScode))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Sublime&#39;,Sublime))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Atom&#39;,Atom))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Programming_languages&#39;,Programming_la
nguages))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Python_tutorial&#39;,Python_tutorial))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;C_tutorial&#39;,C_tutorial))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;CSS_tutorial&#39;,CSS_tutorial))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;HTML_tutorial&#39;,HTML_tutorial))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Java_tutorial&#39;,Java_tutorial))

dispatcher.add_handler(telegram.ext.CommandHandler(&#39;Nodejs_tutorial&#39;,Nodejs_tutorial))

updater.start_polling()
updater.idle()