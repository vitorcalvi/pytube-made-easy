from selenium import webdriver
import time 
import wget


list = ['https://pucminas.instructure.com/courses/26522/pages/introducao-aos-testes-de-hipoteses?module_item_id=1028755',
        'https://pucminas.instructure.com/courses/26522/pages/valor-p-parte-1?module_item_id=1028758',
        'https://pucminas.instructure.com/courses/26522/pages/valor-p-parte-2?module_item_id=1028760',
        'https://pucminas.instructure.com/courses/26522/pages/teste-para-duas-variancias?module_item_id=1028766'
]




driver = webdriver.Firefox()
driver.get('https://pucminas.instructure.com/login/canvas')

# USER and Paasword
password = driver.find_element_by_id("pseudonym_session_password")
username = driver.find_element_by_id("pseudonym_session_unique_id")
username.send_keys("1289202")
password.send_keys("senha")
driver.find_element_by_xpath('//*[@id="login_form"]/div[3]/div[2]/button').click()

my_dict = {}
numero = 0
for i in list:
    driver.get(i)
    time.sleep(7)
    titulo = driver.find_element_by_xpath('//*[@id="wiki_page_show"]/div[3]/h1').get_attribute("innerHTML")
    iframe = driver.find_element_by_xpath('//*[@id="wiki_page_show"]/div[3]/p/iframe')
    driver.switch_to.frame(iframe)
    url = driver.find_element_by_xpath('.//video/source').get_attribute('src')
    
    my_dict = {titulo:url}

  
    
    extensao = ".mp4"
    for titulo2, url2 in my_dict.items():
      numero += 1
      print(titulo2)
      print(url2)
      print('Baixando ' + titulo2)
      converted_num = f'{numero}'
      wget.download(url2, "./videos/ESTATISTICA/TESTES DE HIPOTESES/" + converted_num + ' - ' + titulo2  + extensao )








