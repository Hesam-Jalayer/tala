import requests
from celery import shared_task
from bs4 import BeautifulSoup


def get_mili_gold_price():
    result = {}
    res_mili = requests.get('https://milli.gold/api/v1/public/milli-price/external').json()
    res_price_change = requests.get('https://milli.gold/api/v1/public/milli-price/widget/external').json()
    price = res_mili['price18']
    
    data = res_price_change['data']['prices']['DAILY']
    last_element = data[-1]
    last_value = int(last_element['value'])
    change24 = (100 * ((price - last_value)/last_value))
   
    result['buy_price'] = (price * 0.5) /1000 + price
    result['sell_price'] = -(price * 0.5)/1000 + price
    result['change24h'] = change24

    return result



def get_talase_price():
    result = {}
    res_talase = requests.get('https://api.talasea.ir/api/market/getGoldPrice?').json()
    price = res_talase['price']
    change24h = res_talase['change24h']

    result['buy_price'] = (res_talase['feeTable'][0]['fee'] * price + price)
    result['sell_price'] = (-(res_talase['feeTable'][0]['fee'] * price)  +  price)
    result['change24h'] =  change24h
    return result



def get_tlyn_price():
    result = {}
    res_talin = requests.get('https://tlyn.ir/')
    soup = BeautifulSoup(res_talin.text, 'html.parser')

    p_element = soup.find('div', class_='elementor-element elementor-element-5980db09 elementor-widget elementor-widget-text-editor').find('p')
    p_element_sell = soup.find('div', class_='elementor-element elementor-element-1c0f63cf elementor-widget elementor-widget-text-editor').find('p')


    price_buy = p_element.text.replace('تومان', '').replace(",", "")
    price_sell = p_element_sell.text.replace('تومان', '').replace(",", "")
    result['buy_price']= int(price_buy)/100
    result['sell_price'] = int(price_sell)/100

    return result




