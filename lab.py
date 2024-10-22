import requests
from celery import shared_task
from bs4 import BeautifulSoup



def get_mili_gold_price():
    result = {}
    res_mili = requests.get('https://milli.gold/api/v1/public/milli-price/external').json()
    price = res_mili['price18']
    result['buy_price'] = (price * 0.5) /1000 + price
    result['sell_price'] = -(price * 0.5)/1000 + price

    return result



def get_talase_price():
    result = {}
    res_talase = requests.get('https://api.talasea.ir/api/market/getGoldPrice?').json()
    price = res_talase['price']

    result['buy_price'] = (res_talase['feeTable'][0]['fee'] * price + price)
    result['sell_price'] = (-(res_talase['feeTable'][0]['fee'] * price)  + price)


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


print(get_mili_gold_price())
print(get_talase_price())
print(get_tlyn_price())