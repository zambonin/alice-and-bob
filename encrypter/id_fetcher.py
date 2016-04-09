#!/usr/bin/env python
# -*- coding: utf-8 -*-

from getpass import getpass
from robobrowser import RoboBrowser

browser = RoboBrowser(history=True, parser='html.parser')
browser.open('https://sistemas.ufsc.br/login')

form = browser.get_form(id='fm1')
form['username'].value = input("Insira sua matrícula: ")
form['password'].value = getpass("Insira sua senha do CAGR: ")
browser.submit_form(form)

url = input("URL da sala: ")
browser.open(url)
results = browser.find_all(class_="texto_pequeno3")

with open("temp", "w") as f:
    f.write(" ".join([i.text for i in results[::4]][1:]))
