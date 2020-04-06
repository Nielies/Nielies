from Wabot import Wabot

bot = Wabot('Nielies', 'edited2.txt')
bot.start('Silasbtc')
bot.mensagem('Olá, eu sou o Nielies, utilize ! antes da mensagem para falar comigo!')
ultimo_texto = ""

while True:
	texto = bot.escutar(ultimo_texto)
	if (texto != ultimo_texto and texto[0] == '!'):		
		ultimo_texto = texto
		print(ultimo_texto)
		texto = texto.replace('!', "")
		texto = texto.lower()
		
		try:	
			if(texto == 'notícias' or texto == 'noticias'):
				bot.noticias()

			elif(texto == 'bot.sair()'):
				bot.mensagem('Saindo...')
				break
			
			elif(texto == 'aprender'):
				bot.aprender(texto)
			
			elif(texto == 'valor dólar' or texto == 'valor bitcoin' or texto == 'valor euro'):
				bot.cotacao(texto)
			
			elif(len(texto) >= 15):
				if (texto[:17] == 'previsao do tempo' or texto[:17] == 'previsão do tempo'):
					try:
						city = texto[21:]				
						bot.previsao(city)
					except:		
						bot.mensagem('Formato correto: pergunta + cidade')
			elif(texto == 'help'):
				bot.mensagem('Olá, eu sou o Nielies, você pode usar coisas como, (!noticias)... digite (!O que você faz) e saiba mais')

			elif(texto == 'o que você faz?'):
				bot.responder('Te mostrar as principais noticias do dia (!noticias) Informar a previsão do tempo (!previsão do tempo em são paulo) Mostrar a cotação de moedas (!valor dolar) Para me ensinar algo novo, experimente (!aprender)')
			else:
				bot.responder(texto)
		except:
			pass