
# import webdriver 
from selenium import webdriver 
import time 
# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys






dia = '22'
ano = '2021'
mes = '09'
origem = 'VIX'
destino = 'FRA'

site_ida_dinheiro = ('https://www.latam.com/pt_br/apps/personas/booking' 
+'?fecha1_dia=' + dia
+'&fecha1_anomes=' + ano +'-'+ mes
+'&auAvailability=1'
+'&ida_vuelta=ida'
+'&vuelos_origen=Vit%C3%B3ria'
+'&from_city1=VIX'
+'&vuelos_destino=Frankfurt'
+'&to_city1=FRA'
+'&flex=1'
+'&vuelos_fecha_salida_ddmmaaaa='
+ dia + '/' + mes + '/' + ano
+'&cabina=Y'
+'&nadults=1'
+'&nchildren=0'
+'&ninfants=0'
+'&cod_promo='
+'&stopover_outbound_days=0'
+'&stopover_inbound_days=0#')



site_ida_pontos = 'https://www.latam.com/pt_br/apps/personas/booking?fecha1_dia=22&fecha1_anomes=2021-09&from_city1=VIX&to_city1=FRA&nadults=1&nchildren=0&ninfants=0&ida_vuelta=ida&cabina=Y&application=lanpass#/'

# create webdriver object 
driver = webdriver.Firefox() 

# get geeksforgeeks.org 
driver.get(site_ida_dinheiro)

import time 

time.sleep(6)


origem = ''
destino = ''
tempo_total = ''
precos = driver.find_elements_by_xpath('//*[@id="main-content"]/div[4]/div/div[2]/section[1]/ul/li/div/button/div/div/span/span/span/span')



for item in items:
    print(item.text)