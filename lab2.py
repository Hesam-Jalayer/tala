
import requests

res_talase = requests.get('https://api.talasea.ir/api/market/getGoldPrice?').json()

print(res_talase['change24h'])