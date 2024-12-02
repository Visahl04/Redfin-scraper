import requests,json
import urllib3

import requests
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

cities = {'Albuquerque': '513/NM/Albuquerque',
 'Alexandria': '250/VA/Alexandria',
 'Anchorage': '781/AK/Anchorage',
 'Arlington': '21282/VA/Arlington',
 'Ashburn': '29015/VA/Ashburn',
 'Atlanta': '30756/GA/Atlanta',
 'Aurora': '29459/IL/Aurora',
 'Austin': '30818/TX/Austin',
 'Bakersfield': '953/CA/Bakersfield',
 'Baltimore': '1073/MD/Baltimore',
 'Baton-Rouge': '1336/LA/Baton-Rouge',
 'Beaverton': '1432/OR/Beaverton',
 'Bend': '1543/OR/Bend',
 'Birmingham': '1823/AL/Birmingham',
 'Boca-Raton': '1903/FL/Boca-Raton',
 'Boise': '2287/ID/Boise',
 'Boston': '1826/MA/Boston',
 'Boulder': '2025/CO/Boulder',
 'Bowie': '2277/MD/Bowie',
 'Brentwood': '2112/CA/Brentwood',
 'Buffalo': '2832/NY/Buffalo',
 'Burlington': '2749/VT/Burlington',
 'Cape-Coral': '2654/FL/Cape-Coral',
 'Chandler': '3104/AZ/Chandler',
 'Charleston': '3478/SC/Charleston',
 'Charlotte': '3105/NC/Charlotte',
 'Chattanooga': '3641/TN/Chattanooga',
 'Chicago': '29470/IL/Chicago',
 'Cincinnati': '3879/OH/Cincinnati',
 'Colorado-Springs': '4147/CO/Colorado-Springs',
 'Columbia': '22307/MD/Columbia',
 'Columbus': '4664/OH/Columbus',
 'Dallas': '30794/TX/Dallas',
 'Denver': '5155/CO/Denver',
 'Des-Moines': '5415/IA/Des-Moines',
 'Detroit': '5665/MI/Detroit',
 'El-Paso': '6171/TX/El-Paso',
 'Elk-Grove': '5672/CA/Elk-Grove',
 'Eugene': '6142/OR/Eugene',
 'Fairfax': '6790/VA/Fairfax',
 'Flagstaff': '6089/AZ/Flagstaff',
 'Fort-Collins': '7006/CO/Fort-Collins',
 'Fort-Lauderdale': '6173/FL/Fort-Lauderdale',
 'Fort-Myers': '6208/FL/Fort-Myers',
 'Fort-Worth': '30827/TX/Fort-Worth',
 'Frederick': '7735/MD/Frederick',
 'Fremont': '6671/CA/Fremont',
 'Fresno': '6904/CA/Fresno',
 'Frisco': '30844/TX/Frisco',
 'Gilbert': '6998/AZ/Gilbert',
 'Glenview': '7628/IL/Glenview',
 'Henderson': '8147/NV/Henderson',
 'Honolulu': '34945/HI/Honolulu',
 'Houston': '8903/TX/Houston',
 'Indianapolis': '9170/IN/Indianapolis',
 'Irvine': '9361/CA/Irvine',
 'Jacksonville': '8907/FL/Jacksonville',
 'Jersey-City': '9168/NJ/Jersey-City',
 'Kansas-City': '35751/MO/Kansas-City',
 'Knoxville': '10200/TN/Knoxville',
 'Las-Vegas': '10201/NV/Las-Vegas',
 'Little-Rock': '10455/AR/Little-Rock',
 'Los-Angeles': '11203/CA/Los-Angeles',
 'Louisville': '12262/KY/Louisville',
 'Madison': '12257/WI/Madison',
 'Manhattan': '35948/NY/Manhattan',
 'Manteca': '11596/CA/Manteca',
 'Memphis': '12260/TN/Memphis',
 'Mesa': '11736/AZ/Mesa',
 'Miami': '11458/FL/Miami',
 'Milwaukee': '35759/WI/Milwaukee',
 'Minneapolis': '10943/MN/Minneapolis',
 'Modesto': '12359/CA/Modesto',
 'Myrtle-Beach': '12572/SC/Myrtle-Beach',
 'Naperville': '29501/IL/Naperville',
 'Naples': '12171/FL/Naples',
 'Nashua': '12918/NH/Nashua',
 'Nashville': '13415/TN/Nashville',
 'New-Orleans': '14233/LA/New-Orleans',
 'New-York': '30749/NY/New-York',
 'Newton': '11619/MA/Newton',
 'Oakland': '13654/CA/Oakland',
 'Oklahoma-City': '14237/OK/Oklahoma-City',
 'Omaha': '9417/NE/Omaha',
 'Orland-Park': '29503/IL/Orland-Park',
 'Orlando': '13655/FL/Orlando',
 'Palm-Springs': '14315/CA/Palm-Springs',
 'Philadelphia': '15502/PA/Philadelphia',
 'Phoenix': '14240/AZ/Phoenix',
 'Pittsburgh': '15702/PA/Pittsburgh',
 'Plainfield': '29505/IL/Plainfield',
 'Plano': '30868/TX/Plano',
 'Portland': '15614/ME/Portland',
 'Providence': '15272/RI/Providence',
 'Quincy': '14424/MA/Quincy',
 'Raleigh': '35711/NC/Raleigh',
 'Rancho-Cucamonga': '15390/CA/Rancho-Cucamonga',
 'Reno': '15627/NV/Reno',
 'Richmond': '17149/VA/Richmond',
 'Riverside': '15935/CA/Riverside',
 'Rochester': '16162/NY/Rochester',
 'Sacramento': '16409/CA/Sacramento',
 'Salem': '30778/OR/Salem',
 'Salt-Lake-City': '17150/UT/Salt-Lake-City',
 'San-Antonio': '16657/TX/San-Antonio',
 'San-Diego': '16904/CA/San-Diego',
 'San-Francisco': '17151/CA/San-Francisco',
 'San-Jose': '17420/CA/San-Jose',
 'San-Luis-Obispo': '17464/CA/San-Luis-Obispo',
 'Santa-Clarita': '17676/CA/Santa-Clarita',
 'Santa-Fe': '18007/NM/Santa-Fe',
 'Sarasota': '16463/FL/Sarasota',
 'Savannah': '17651/GA/Savannah',
 'Schaumburg': '29511/IL/Schaumburg',
 'Scottsdale': '16660/AZ/Scottsdale',
 'Seattle': '16163/WA/Seattle',
 'Silver-Spring': '26038/MD/Silver-Spring',
 'Sioux-Falls': '15282/SD/Sioux-Falls',
 'St-Louis': '16661/MO/St-Louis',
 'Stamford': '18605/CT/Stamford',
 'Stockton': '19009/CA/Stockton',
 'Tacoma': '17887/WA/Tacoma',
 'Tampa': '18142/FL/Tampa',
 'Temecula': '19701/CA/Temecula',
 'Truckee': '66715/CA/Truckee',
 'Tucson': '19459/AZ/Tucson',
 'Tulsa': '35765/OK/Tulsa',
 'Virginia-Beach': '20418/VA/Virginia-Beach',
 'Washington-DC': '12839/DC/Washington-DC',
 'West-Palm-Beach': '19373/FL/West-Palm-Beach',
 'Wilmington': '19583/DE/Wilmington',
 'Woodbridge': '26845/VA/Woodbridge',
 'Worcester': '20420/MA/Worcester'}

token = "026d44200cad4fbdb5faba7bec3cd785b4912d3e685"
proxyModeUrl = "http://{}:extraHeaders=true@proxy.scrape.do:8080".format(token)

proxies = {
    "http": proxyModeUrl,
    "https": proxyModeUrl,
}

def get_median_sale_prices(path):
    url = f"https://www.redfin.com/city/{path}/housing-market"
    payload = {}
    headers = {
      'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
      'accept-language': 'en-US,en;q=0.9',
      'cache-control': 'max-age=0',
      'cookie': 'RF_BROWSER_ID=GYqY8Tq_RRaFCYguxpkK8w; RF_BROWSER_ID_GREAT_FIRST_VISIT_TIMESTAMP=2024-11-30T21%3A55%3A05.684427; RF_BID_UPDATED=1; _gcl_au=1.1.187109766.1733032550; __pdst=fe60d6360cb141959b96946b73f61dc7; _scor_uid=9be5df04f26e4acf8bc05ea3d92cc59a; _fbp=fb.1.1733032549876.624482343594845648; _pin_unauth=dWlkPU1UZGpZV1psT0RrdE16ZzRaaTAwWWpkaUxXSTVPV1F0T0RZd016WTVNV1poT0dOaA; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.1503468655.1733032550; RF_BROWSER_CAPABILITIES=%7B%22screen-size%22%3A4%2C%22events-touch%22%3Afalse%2C%22ios-app-store%22%3Afalse%2C%22google-play-store%22%3Afalse%2C%22ios-web-view%22%3Afalse%2C%22android-web-view%22%3Afalse%7D; FEED_COUNT=%5B%22%22%2C%22f%22%5D; RF_VISITED=true; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Dec+01+2024+11%3A29%3A29+GMT%2B0530+(India+Standard+Time)&version=202403.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&consentId=d87d4d31-9797-4eae-9710-f5d293b351be&interactionCount=1&isAnonUser=1&landingPath=https%3A%2F%2Fwww.redfin.com%2Fcity%2F30818%2FTX%2FAustin%2Fhousing-market&groups=C0001%3A1%2CC0003%3A1%2CSPD_BG%3A1%2CC0002%3A1%2CC0004%3A1; _rdt_uuid=1733032549763.b54c6890-234c-4d13-8f2d-ff80958def53; _uetsid=eabe3120afa811ef9890eb1dfcffda9f; _uetvid=eabe6850afa811ef95c2279cb9eefea3; RF_CORVAIR_LAST_VERSION=551.1.0; _ga=GA1.2.272156238.1733032550; _ga_928P0PZ00X=GS1.1.1733032549.1.1.1733033041.50.0.0; aws-waf-token=21c35ecf-ad57-4df9-9fb3-8c88c7a92288:BQoApQQqjbQKAAAA:8FO+3Yw8sGaT15Vf2YA01K6g0UfRZtVklPkauQa2LVjRXUBrrquXI5f24iGmIbG+DgGb9oC1XmuesWsVYKN9Zzlcp79HRPDgrcctrRz1FHR7J7fPQCHhH1428Sc+aPLy08Ht7RsEn0ZVJR6J79cK+LTPBnvz8B9ufRdtnX9zaGG2xOJOKCBApl6WywAJpfAQNXljDOWYfO5/nDBEpXtQE+Swu3nFZCkeGGz1ISuPko6xCwsaNxf8hMlLdALTOabv8w==; _dd_s=rum=0&expire=1733034151059; RF_CORVAIR_LAST_VERSION=vLATEST; RF_TRAFFIC_SEGMENT=non-organic; RF_VISITED=true',
      'priority': 'u=0, i',
      'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'document',
      'sec-fetch-mode': 'navigate',
      'sec-fetch-site': 'none',
      'sec-fetch-user': '?1',
      'upgrade-insecure-requests': '1',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    response = requests.request("GET", url, headers=headers, data=payload, proxies=proxies, verify=False)
    print(response.status_code)
    tt = response.text.split('"ReactServerAgent.cache":')[1].split(',"deviceType":"desktop","webViewAppName":null}')[0]
    kk = json.loads(tt)

    p = kk.get('dataCache').get('/stingray/api/graph/6/30818/All/regional-housing-market/home_prices').get('res').get('text').split('{}&&')[1]
    ll = json.loads(p)
    qa = ll.get('payload').get('metrics')[0]
    return q


if __name__ == "__main__":
    city = 'austin'
    for ci,path in cities.items():
        if city.lower() == ci.lower():
            o = get_median_sale_prices(path)
            print(json.dumps(o))



