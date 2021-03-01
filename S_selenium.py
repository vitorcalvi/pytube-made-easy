from selenium import webdriver
import time 
import wget


list = [

'https://pucminas.instructure.com/courses/24705/pages/videoaula-arvore-de-decisao-principios?module_item_id=371832',
'https://pucminas.instructure.com/courses/24705/pages/videoaula-arvore-de-decisao-id3?module_item_id=371838',
'https://pucminas.instructure.com/courses/24705/pages/videoaula-arvore-de-decisao-overfitting?module_item_id=371844',
'https://pucminas.instructure.com/courses/24705/pages/videoaula-arvore-de-decisao-atributos-continuos?module_item_id=371850',
'https://pucminas.instructure.com/courses/24705/pages/aula-pratica-arvore-de-decisao?module_item_id=371856',
'https://pucminas.instructure.com/courses/24705/pages/videoaula-classificacao-bayesiana?module_item_id=371869',
'https://pucminas.instructure.com/courses/24705/pages/aula-pratica-colab-naive-bayes-iris?module_item_id=371872'

]




driver = webdriver.Firefox()
driver.get('https://pucminas.instructure.com/login/canvas')

# USER and Paasword
password = driver.find_element_by_id("pseudonym_session_password")
username = driver.find_element_by_id("pseudonym_session_unique_id")
username.send_keys("1289202")
password.send_keys("112233abcG.")
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
      wget.download(url2, "./video/" + converted_num + ' - ' + titulo2.replace(':','')  + extensao )







