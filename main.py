from Wabot import wabot

conversation = [
"Oi",
"Olá",
"Como você está?",
"Eu estou bem, e você?",
"Estou otimo!",
"Fico feliz em saber",
"Obrigado.",
"Denada.",
"Olá nielies, quem é você?"
"Eu sou o Nielies, inteligencia artificial desenvolvida por @luide__, como posso te ajudar?"
]
ultima_mensagem = ''
Wabot = wabot('Nielies', conversation)
Wabot.Start('Whatsappbot')
Wabot.Saudacao('Olá, eu sou o Nielies, tudo bem? utilize & antes da mensagem para falar comigo.')

while True:
    mensagem = Wabot.Escutar()
    if mensagem[0] == '&' and mensagem != ultima_mensagem:
        texto = mensagem.replace('&', '')
        print (texto)
        Wabot.Responder(texto)
    else:
        a = 'a'
