from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
import requests
import json
import time

mensagem = ''
resposta = ''
last = ''
class Wabot:
	def __init__(self, nome_bot, name_list):
		self.bot = ChatBot(nome_bot)
		self.trainer = ListTrainer(self.bot)
		file = open(name_list, 'r').readlines()
		self.trainer.train(file)
		self.options = webdriver.ChromeOptions()
		self.options.add_argument("user-data-dir=/home/nielies/.config/google-chrome")
		self.driver = webdriver.Chrome(executable_path=r'./chromedriver', chrome_options=self.options)
		
	def start(self, nome_contato):
		self.driver.get('https://web.whatsapp.com/')
		self.driver.implicitly_wait(20)
		self.pesquisa = self.driver.find_element_by_class_name('_3F6QL')
		print(self.pesquisa)
		self.pesquisa.click()
		self.pesquisa.send_keys(nome_contato)
		time.sleep(2)
		print(nome_contato)
		self.contato = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(nome_contato))
		self.contato.click()
		time.sleep(2)
	
	def pula_linha(self):
		self.driver.key_down(Keys.SHIFT)
		self.driver.send_keys(Keys.ENTER)
		self.driver.key_up(Keys.SHIFT)

	def mensagem(self, frase_inicial):
		self.chat = self.driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
		self.chat.send_keys(frase_inicial)
		self.chat.send_keys('\n')

	def escutar(self, ultima_mensagem):
		post = self.driver.find_elements_by_class_name('_3_7SH')
		ultimo = len(post) - 1
		texto = post[ultimo].find_element_by_css_selector('span.selectable-text').text
		return texto

	def responder(self, ultima_resposta):
		response = self.bot.get_response(ultima_resposta)
		response = str(response)
		self.chat.send_keys(response)
		self.chat.send_keys('\n')

	def noticias(self):
		a = requests.get('https://newsapi.org/v2/top-headlines?sources=globo&pageSize=5&apiKey=f6fdb7cb0f2a497d92dbe719a29b197f')
		news = json.loads(a.text)
		count = 0
		for b in news['articles']:
			if count != 5:
				titulo = b['title']
				link = b['url']
				self.chat.send_keys(titulo,' ', link)
				self.chat.send_keys('\n')
				count += 1

	def aprender(self, texto):
		mensagem = texto
		self.mensagem('Digite a primeira mensagem:')
		
		while (mensagem == texto or mensagem == 'Digite a primeira mensagem:'):
			mensagem = self.escutar()
			resposta = mensagem

		self.mensagem('Digite a resposta:')

		while (resposta == mensagem or resposta == 'Digite a resposta:'):
			resposta = self.escutar()

		ensinar = []
		ensinar.append(mensagem)
		ensinar.append(resposta)
		print(ensinar)
		self.trainer.train(ensinar)
		self.mensagem('Obrigado pela ajuda :)')

	def cotacao(self, moeda):
		if moeda == 'valor dólar':
			procurar = 'USD'
		elif moeda == 'valor euro':
			procurar = 'EUR'
		elif moeda == 'valor bitcoin':
			procurar = 'BTC'

		a = requests.get("https://economia.awesomeapi.com.br/all/{}-BRL".format(procurar))
		valor = a.json()
		self.mensagem(valor[procurar]['bid'][:5])
	
	def previsao(self, city, country=None):
		if not country:
			country = 'BR'
		apikey = 'b421ffcc5697f833ea46a336dacd915b'
		weather = requests.get('http://api.openweathermap.org/data/2.5/weather?appid={}&q={},{}&lang=pt_br&units=metric'.format(apikey, city, country)).json()

		a1 = weather['main']['temp']
		a2 = weather['main']['feels_like']
		a3 = weather['main']['temp_max']
		a4 = weather['main']['temp_min']
		a5 = weather['weather'][0]['description']

		information = ('Temperatura: {}°C\nSensação termica: {}°C\nTemperatura maxima: {}°C\nTemperatura minima: {}°C\nCéu: {}\n'.format(a1, a2, a3, a4, a5))
		self.chat.send_keys(information)