import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime
import random
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.


def parsehtml(url):
    try:
        time.sleep(2)
        executable_path = "chromedriver"
        browser = webdriver.Chrome(executable_path=executable_path, chrome_options=options)
        browser.get(url)
        # result_count = requests.get(url)
        # ebay_page_count = result_count.content
        ebay_page_count = browser.page_source
        soup_count = BeautifulSoup(ebay_page_count, 'html.parser')
        zg_browseRoot = soup_count.findAll('ul', {'id': 'zg_browseRoot'})[0]
        try:
            ul = zg_browseRoot.find('ul')
            for x in range(6):
                try:
                    ullatest = ul.find('ul')
                    if ullatest != None:
                        ul = ullatest
                except Exception:
                    pass
            try:
                alllist = ul.findAll('li')
            except Exception:
                alllist = []
                pass
        except Exception:
            alllist = []
            pass
    except Exception as e:
        print(url)
        time.sleep(300)
        alllist = []
        pass
    return alllist


def main():
    fruits = ["new-releases", "movers-and-shakers", "most-wished-for", "most-gifted"]
    for x in fruits:
        fnme = x.replace('-', '')
        timenow = str(datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3])
        file_name = fnme + '_' + timenow + '.csv'

        dfObj = pd.DataFrame(
            columns=['select', 'amazon_url', 'cat1', 'cat2', 'cat3', 'cat4', 'cat5', 'cat6', 'cat7', 'cat8'])
        dfObj.to_csv(file_name)
        _pgn = 0

        ebay_main_url_count = "https://www.amazon.com/gp/" + str(x)
        alllist = parsehtml(ebay_main_url_count)
        select = ''
        amazon_url = ''
        cat1 = ''
        cat2 = ''
        cat3 = ''
        cat4 = ''
        cat5 = ''
        cat6 = ''
        cat7 = ''
        cat8 = ''
        skip = False
        for index1, item1 in enumerate(alllist):
            try:
                select = "True"
                amazon_url = item1.find('a').attrs['href']
                cat1 = item1.text.replace('‹', '').strip()

                # if cat1 == 'Video Games':
                #     skip = True
                # if skip == False:
                #     raise ValueError('A very specific bad thing happened.')
                cat2 = ''
                cat3 = ''
                cat4 = ''
                cat5 = ''
                cat6 = ''
                cat7 = ''
                cat8 = ''
                if 'Amazon' in cat1:
                    raise ValueError('A very specific bad thing happened.')
                with open(file_name, 'a') as f:
                    dfObj.to_csv(f, header=False)
                dfObj = dfObj.append(
                    {'select': select, 'amazon_url': amazon_url, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3, 'cat4': cat4
                        , 'cat5': cat5, 'cat6': cat6, 'cat7': cat7, 'cat8': cat8}, ignore_index=True)
                dfObj.to_csv(file_name)
                itemcat2 = parsehtml(amazon_url)
                for index2, item2 in enumerate(itemcat2):
                    try:
                        amazon_url = ''
                        amazon_url = item2.find('a').attrs['href']
                        cat2 = item2.text.replace('‹', '').strip()
                        cat3 = ''
                        cat4 = ''
                        cat5 = ''
                        cat6 = ''
                        cat7 = ''
                        cat8 = ''
                        with open(file_name, 'a') as f:
                            dfObj.to_csv(f, header=False)
                        dfObj = dfObj.append(
                            {'select': select, 'amazon_url': amazon_url, 'cat1': cat1, 'cat2': cat2, 'cat3': cat3,
                             'cat4': cat4
                                , 'cat5': cat5, 'cat6': cat6, 'cat7': cat7, 'cat8': cat8}, ignore_index=True)
                        dfObj.to_csv(file_name)
                        itemcat3 = parsehtml(amazon_url)
                        for index3, item3 in enumerate(itemcat3):
                            try:
                                isselected3 = False
                                for index_3, item_3 in enumerate(itemcat3):
                                    try:
                                        if item_3.next.attrs['class'][0] == 'zg_selected':
                                            isselected3 = True
                                    except Exception as e:
                                        pass

                                if isselected3 == True:
                                    raise ValueError('A very specific bad thing happened.')
                                amazon_url = ''
                                amazon_url = item3.find('a').attrs['href']
                                cat3 = item3.text.replace('‹', '').strip()
                                cat4 = ''
                                cat5 = ''
                                cat6 = ''
                                cat7 = ''
                                cat8 = ''
                                with open(file_name, 'a') as f:
                                    dfObj.to_csv(f, header=False)
                                dfObj = dfObj.append(
                                    {'select': select, 'amazon_url': amazon_url, 'cat1': cat1, 'cat2': cat2,
                                     'cat3': cat3,
                                     'cat4': cat4
                                        , 'cat5': cat5, 'cat6': cat6, 'cat7': cat7, 'cat8': cat8},
                                    ignore_index=True)
                                dfObj.to_csv(file_name)
                                itemcat4 = parsehtml(amazon_url)
                                for index4, item4 in enumerate(itemcat4):
                                    try:
                                        isselected4 = False
                                        for index_4, item_4 in enumerate(itemcat4):
                                            try:
                                                if item_4.next.attrs['class'][0] == 'zg_selected':
                                                    isselected4 = True
                                            except Exception as e:
                                                pass

                                        if isselected4 == True:
                                            raise ValueError('A very specific bad thing happened.')

                                        amazon_url = ''
                                        amazon_url = item4.find('a').attrs['href']
                                        cat4 = item4.text.replace('‹', '').strip()
                                        cat5 = ''
                                        cat6 = ''
                                        cat7 = ''
                                        cat8 = ''
                                        with open(file_name, 'a') as f:
                                            dfObj.to_csv(f, header=False)
                                        dfObj = dfObj.append(
                                            {'select': select, 'amazon_url': amazon_url, 'cat1': cat1, 'cat2': cat2,
                                             'cat3': cat3,
                                             'cat4': cat4
                                                , 'cat5': cat5, 'cat6': cat6, 'cat7': cat7, 'cat8': cat8},
                                            ignore_index=True)
                                        dfObj.to_csv(file_name)
                                        itemcat5 = parsehtml(amazon_url)
                                        for index5, item5 in enumerate(itemcat5):
                                            try:
                                                isselected5 = False
                                                for index_5, item_5 in enumerate(itemcat5):
                                                    try:
                                                        if item_5.next.attrs['class'][0] == 'zg_selected':
                                                            isselected5 = True
                                                    except Exception as e:
                                                        pass

                                                if isselected5 == True:
                                                    raise ValueError('A very specific bad thing happened.')
                                                amazon_url = ''
                                                amazon_url = item5.find('a').attrs['href']
                                                cat5 = item5.text.replace('‹', '').strip()
                                                cat6 = ''
                                                cat7 = ''
                                                cat8 = ''
                                                with open(file_name, 'a') as f:
                                                    dfObj.to_csv(f, header=False)
                                                dfObj = dfObj.append(
                                                    {'select': select, 'amazon_url': amazon_url, 'cat1': cat1,
                                                     'cat2': cat2,
                                                     'cat3': cat3,
                                                     'cat4': cat4
                                                        , 'cat5': cat5, 'cat6': cat6, 'cat7': cat7, 'cat8': cat8},
                                                    ignore_index=True)
                                                dfObj.to_csv(file_name)
                                                itemcat6 = parsehtml(amazon_url)
                                                for index6, item6 in enumerate(itemcat6):
                                                    try:
                                                        isselected6 = False
                                                        for index_6, item_6 in enumerate(itemcat6):
                                                            try:
                                                                if item_6.next.attrs['class'][0] == 'zg_selected':
                                                                    isselected6 = True
                                                            except Exception as e:
                                                                pass

                                                        if isselected6 == True:
                                                            raise ValueError('A very specific bad thing happened.')
                                                        amazon_url = ''
                                                        amazon_url = item6.find('a').attrs['href']
                                                        cat6 = item6.text.replace('‹', '').strip()
                                                        cat7 = ''
                                                        cat8 = ''
                                                        with open(file_name, 'a') as f:
                                                            dfObj.to_csv(f, header=False)
                                                        dfObj = dfObj.append(
                                                            {'select': select, 'amazon_url': amazon_url, 'cat1': cat1,
                                                             'cat2': cat2,
                                                             'cat3': cat3,
                                                             'cat4': cat4
                                                                , 'cat5': cat5, 'cat6': cat6, 'cat7': cat7,
                                                             'cat8': cat8},
                                                            ignore_index=True)
                                                        dfObj.to_csv(file_name)
                                                        itemcat7 = parsehtml(amazon_url)
                                                        for index7, item7 in enumerate(itemcat7):
                                                            try:
                                                                isselected7 = False
                                                                for index_7, item_7 in enumerate(itemcat7):
                                                                    try:
                                                                        if item_7.next.attrs['class'][
                                                                            0] == 'zg_selected':
                                                                            isselected7 = True
                                                                    except Exception as e:
                                                                        pass

                                                                if isselected7 == True:
                                                                    raise ValueError(
                                                                        'A very specific bad thing happened.')
                                                                amazon_url = ''
                                                                amazon_url = item7.find('a').attrs['href']
                                                                cat7 = item7.text.replace('‹', '').strip()
                                                                cat8 = ''
                                                                with open(file_name, 'a') as f:
                                                                    dfObj.to_csv(f, header=False)
                                                                dfObj = dfObj.append(
                                                                    {'select': select, 'amazon_url': amazon_url,
                                                                     'cat1': cat1,
                                                                     'cat2': cat2,
                                                                     'cat3': cat3,
                                                                     'cat4': cat4
                                                                        , 'cat5': cat5, 'cat6': cat6, 'cat7': cat7,
                                                                     'cat8': cat8},
                                                                    ignore_index=True)
                                                                dfObj.to_csv(file_name)
                                                                itemcat8 = parsehtml(amazon_url)
                                                                for index8, item8 in enumerate(itemcat8):
                                                                    try:
                                                                        isselected8 = False
                                                                        for index_8, item_8 in enumerate(itemcat8):
                                                                            try:
                                                                                if item_8.next.attrs['class'][
                                                                                    0] == 'zg_selected':
                                                                                    isselected8 = True
                                                                            except Exception as e:
                                                                                pass

                                                                        if isselected8 == True:
                                                                            raise ValueError(
                                                                                'A very specific bad thing happened.')
                                                                        amazon_url = ''
                                                                        amazon_url = item8.find('a').attrs['href']
                                                                        cat8 = item8.text.replace('‹', '').strip()
                                                                        with open(file_name, 'a') as f:
                                                                            dfObj.to_csv(f, header=False)
                                                                        dfObj = dfObj.append(
                                                                            {'select': select, 'amazon_url': amazon_url,
                                                                             'cat1': cat1,
                                                                             'cat2': cat2,
                                                                             'cat3': cat3,
                                                                             'cat4': cat4
                                                                                , 'cat5': cat5, 'cat6': cat6,
                                                                             'cat7': cat7,
                                                                             'cat8': cat8},
                                                                            ignore_index=True)
                                                                        dfObj.to_csv(file_name)
                                                                    except Exception as e:
                                                                        break
                                                            except Exception as e:
                                                                break
                                                    except Exception as e:
                                                        break
                                            except Exception as e:
                                                break
                                    except Exception as e:
                                        break
                            except Exception as e:
                                break
                    except Exception as e:

                        break
            except Exception as e:
                pass


if __name__ == "__main__":
    print("script start...!!")
    try:
        main()
    except Exception as e:
        print(str(e))
