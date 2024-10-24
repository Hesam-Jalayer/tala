# import requests
# from bs4 import BeautifulSoup
from datetime import datetime,  timedelta

# def get_tlyn_price():
#     result = {}
#     res_talin = requests.get('https://tlyn.ir/')
#     soup = BeautifulSoup(res_talin.text, 'html.parser')

#     p_element = soup.find('div', class_='elementor-element elementor-element-5980db09 elementor-widget elementor-widget-text-editor').find('p')
#     p_element_sell = soup.find('div', class_='elementor-element elementor-element-1c0f63cf elementor-widget elementor-widget-text-editor').find('p')


#     price_buy = p_element.text.replace('تومان', '').replace(",", "")
#     price_sell = p_element_sell.text.replace('تومان', '').replace(",", "")
#     result['buy_price']= int(price_buy)/100
#     result['sell_price'] = int(price_sell)/100

#     return result

# print(get_tlyn_price())


current_time = datetime.now()

one_day_ago = current_time - timedelta(days=1)

print(current_time)
print(one_day_ago)