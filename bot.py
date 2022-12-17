import telegram.ext

 

Token = "5736838466:AAFts2vIdn0LhBNY1mJF81LlPvoq_o5p-aE"

 

updater = telegram.ext.uodater("5736838466:AAFts2vIdn0LhBNY1mJF81LlPvoq_o5p-aE", use_context=True)

dispatcher = updater.dispatcher

 

 

def start(update, context):

    update.message.reply_text("Welcome aboard!This friendly bot will provide you with all the required resources and stuff you wish to learn.It doesn't matter if you don't know nothing about programming , we are here to help you out.Every pro began as an amateur")

def content(update, context):

    update.message.reply_text(

    """

 

    You have choosed the right path.This bot will provide you with:

    ➡Basics of programming

    ➡Downloading code editors

    ➡Programming languages

    ➡Roadmap

    ➡Mini Project

 

    """

    )

 

def start(update, context):

    update.message.reply_text("We have various learning resources available to boost your knowledge and skills")

 

def content (update, context):

    update.message.reply_text("")   

 

 