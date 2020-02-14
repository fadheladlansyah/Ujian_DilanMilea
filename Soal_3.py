import requests

url_prov = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
url_postcode = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/kodepos.json'
province = requests.get(url_prov).json()
postcode = requests.get(url_postcode).json()
province_r = {value: key for key, value in province.items()}

def cek_postcode(kel, kec, kab, prov):
    prov_code = province_r[prov]
    for data in postcode[prov_code]:
        if data['urban'] == kel and data['sub_district'] == kec and data['city'] == kab:
            return data['postal_code']
        
zip_code1 = cek_postcode(kel="SAMPORA", kec="CISAUK", kab="TANGERANG", prov="BANTEN") #Dilan
print(f"Kode Pos lokasi Dilan adalah {zip_code1}")
zip_code2 = cek_postcode(kel="CITARUM", kec="BANDUNG WETAN", kab="BANDUNG", prov="JAWA BARAT") #Milea
print(f"Kode Pos lokasi Milea adalah {zip_code2}")

api_key = 'bJ04hwme0xCPOA2nK4gNxTOE2rrX8bX9Y3JA33hNNIAhCyEzcrSefSMOUTernhHR'
format_ = 'json'
units = 'km'
url = f'http://www.zipcodeapi.com/rest/{api_key}/distance.{format_}/{zip_code1}/{zip_code2}/{units}'

response = requests.get(url)
data = response.json()

distance = data['distance']
print(f"Jarak Dilan & Milea adalah {distance} km")