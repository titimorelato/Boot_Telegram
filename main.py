from typing import LiteralString

import telebot

CHAVE_API = "6348037969:AAGKSPAbKFgBxPn1RnFV2CIcLAufu8wHL2w"
bot= telebot.TeleBot(CHAVE_API)
def verificar(mensagem):
        return false

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
       Escolha uma das opções para Continuar (Clique No item):
       /1 - Suporte Avacorp - 1
       /2 - Suporte Avacorp
       /3 - Suporte InfraEstrutura Matão
       Responder Qualque outra opção não vai funcionar , clique em uma das opções"""
       
bot.reply_to(mensagem, texto)

bot.polling()




