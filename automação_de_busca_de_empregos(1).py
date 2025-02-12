# -*- coding: utf-8 -*-
"""Automação de Busca de Empregos

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17FTYqQbyPh-td4lN0xjrXSTX8sJSvcmB
"""

!pip install selenium

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


os.environ['BROWSERSTACK_USERNAME'] = ''
os.environ['BROWSERSTACK_ACCESS_KEY'] = ''


USERNAME = os.getenv('BROWSERSTACK_USERNAME')
ACCESS_KEY = os.getenv('BROWSERSTACK_ACCESS_KEY')


REMOTE_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"


options = Options()
options.set_capability('browserName', 'Chrome')
options.set_capability('browser_version', 'latest')
options.set_capability('os', 'Windows')
options.set_capability('os_version', '10')
options.set_capability('name', 'Colab Selenium Test')


driver = webdriver.Remote(
    command_executor=REMOTE_URL,
    options=options
)


driver.get("https://www.google.com")
print(driver.title)


driver.quit()

!pip install selenium openai pandas


import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


os.environ['BROWSERSTACK_USERNAME'] = ''
os.environ['BROWSERSTACK_ACCESS_KEY'] = ''

USERNAME = os.getenv('BROWSERSTACK_USERNAME')
ACCESS_KEY = os.getenv('BROWSERSTACK_ACCESS_KEY')
REMOTE_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"


options = Options()
options.set_capability('browserName', 'Chrome')
options.set_capability('browser_version', 'latest')
options.set_capability('os', 'Windows')
options.set_capability('os_version', '10')
options.set_capability('name', 'JobScraper Automation')


def job_scraper(site_url, css_selectors, pages=1):
    driver = webdriver.Remote(command_executor=REMOTE_URL, options=options)
    all_jobs = []

    for page in range(1, pages + 1):
        driver.get(f"{site_url}?page={page}")
        time.sleep(3)

        titles = driver.find_elements(By.CSS_SELECTOR, css_selectors['title'])
        dates = driver.find_elements(By.CSS_SELECTOR, css_selectors['date'])
        links = driver.find_elements(By.CSS_SELECTOR, css_selectors['link'])

        for i in range(len(titles)):
            job = {
                'Título': titles[i].text,
                'Data de Publicação': dates[i].text,
                'Link': links[i].get_attribute('href')
            }
            all_jobs.append(job)

        print(f"Página {page} processada com sucesso!")

    driver.quit()
    return pd.DataFrame(all_jobs)


css_selectors_infojobs = {
    'title': '.vaga h2',
    'date': '.vaga .data-publicacao',
    'link': '.vaga a'
}


css_selectors_gupy = {
    'title': 'h2[data-testid="job-title"]',
    'date': 'span[data-testid="publication-date"]',
    'link': 'a[data-testid="job-link"]'
}


vagas_infojobs = job_scraper('https://www.infojobs.com.br/empregos.aspx', css_selectors_infojobs, pages=2)


vagas_gupy = job_scraper('https://www.gupy.io/vagas', css_selectors_gupy, pages=2)


vagas_infojobs.to_csv('vagas_infojobs.csv', index=False)
vagas_gupy.to_csv('vagas_gupy.csv', index=False)
print("Vagas salvas em 'vagas_infojobs.csv' e 'vagas_gupy.csv'")


def enviar_alerta(vagas):
    for index, vaga in vagas.iterrows():
        mensagem = f"🚀 Nova Vaga: {vaga['Título']}\n📅 Publicada em: {vaga['Data de Publicação']}\n🔗 Link: {vaga['Link']}"
        print(mensagem)
        time.sleep(1)


print("Enviando alertas via WhatsApp...")
enviar_alerta(vagas_infojobs.head(3))
enviar_alerta(vagas_gupy.head(3))