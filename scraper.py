from bs4 import BeautifulSoup
import requests
import re
import csv

# Description :
# Script to scrap and save in csv file all type of smallarms listed on www.militaryfactory.com using BeautifulSoup.


def create_fields():
    csv_file = open('cms-scraper.csv', 'w')
    csv_writer = csv.writer(csv_file)
    fields = []
    source = requests.get(
        'https://www.militaryfactory.com/smallarms/detail.asp').text
    soup = BeautifulSoup(source, 'lxml')
    for specification in soup.find_all('div', class_='statsEntries'):
        for variable in specification.find_all('span', class_='textBold'):
            if(str(variable.text.split(':')[0]) != 'Roles'):
                print(variable.text.split(':')[0])
                fields.append(variable.text.split(':')[0])
    csv_writer.writerow(fields)
    csv_file.close()


def get_infos():
    csv_file = open('cms-scraper.csv', 'a')
    csv_writer = csv.writer(csv_file)
    for id in range(1, 1200):
        attributes = []
        source = requests.get(
            'https://www.militaryfactory.com/smallarms/detail.asp?smallarms_id='+str(id)).text
        soup = BeautifulSoup(source, 'lxml')
        for specification in soup.find_all('div', class_='statsEntries'):
            for span in specification('span'):
                span.decompose()
            info = specification.text.split('\r\n')[0].splitlines()
            for i in info:
                if(i != ''):
                    attributes.append(i)
        if attributes:
            print(attributes)
            csv_writer.writerow(attributes)
    csv_file.close()


create_fields()
get_infos()
