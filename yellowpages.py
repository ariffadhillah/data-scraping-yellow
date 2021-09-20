import requests
from bs4 import BeautifulSoup

InputSearch = input('enter name Search :')
location = input('enter name location :')
count = 0

for page in range(1, 6): 
    url = 'https://www.yellowpages.com.au/search/listings?clue={0}&locationClue={1}&pageNumber={2}'.format(InputSearch,location,page)

    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
        'cookie': 'bm_sz=85A77AE0B23C903F7FBF224ADA7CEAD5~YAAQPzArF6A1S+d7AQAAGywmAw0yMfD8q52NBd7WpotLHN0bcT6zDZeRiyx2er0THTcvaXHjAP+n8AWD4zPnCMAv6dkDRcDvjuXTSVAzIL0iQHbBDapyyOMLKSguUqTMuwSt+3m377Hy/DOZVMblaQDc/Mz+mHYivwLD4MYH2abUmIawrJWaJA3nk1bAQ7eZfV3j7tqkvs/3NfHhWXVGrP4+PcNsjoAc7nWKIoG+I2R7BxyCIY6WBVQhTckiWNFUfxyJ/Dm7SzkK6LlxTl9PzidcTo8bCJBwOnWOi1clb1Wg3Axtv5mwYidh1w==~4408882~3422519; ak_bmsc=3A7D46FF72F4E5A40ED37E6C238D0347~000000000000000000000000000000~YAAQPzArF6k1S+d7AQAAuzUmAw3kxZHg882aAIemHRgldFcTr6tHkNalXmO8tZMwBaOAHZjQr2tM5oSN/csjeNfgLoHzIDag2kCgxqkUZ9S+YMLWuv89MYEgd/K2dXlLfxV+nXizImPJzSV24tGXHpn+ooGwA4JYg9PFCIVVMdd3YR58Jn9gMHV7yyuEm/Oeq1tc3xmbzxXDvKqX4H0F3SvroUV6ZFz5qiQcWxoaWJlkXHiTAIwNcIZLbb9Nl81830eQbzdEBJqRbYPaLJJerpr0PiDmjREAjqYRICMLAJ/DpCmJEbpF/V1BkyLgiN/pUq5XQ9TXChAn8SL6pEGOCK/itqN6Stwiz/k3bLstUsDu2yXV7KknJELBJvJ01drKsMWL6Gzp0/h5Ys2/DZau; JSESSIONID=27D51702A4AACE74034CCCD4746DBE38; yellow-guid=07305cda-ab87-4e53-8596-4db7abdbedc7; AMCVS_8412403D53AC3D7E0A490D4C%40AdobeOrg=1; s_ecid=MCMID%7C27047168093730314941062463734019320782; _vwo_uuid_v2=D25F69AF1C257696F487AFA6A659D80F1|6d050e40948fa5dae062dc4bb7500b88; AMCV_8412403D53AC3D7E0A490D4C%40AdobeOrg=-1124106680%7CMCIDTS%7C18891%7CMCMID%7C27047168093730314941062463734019320782%7CMCAAMLH-1632745224%7C3%7CMCAAMB-1632745224%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1632147624s%7CNONE%7CMCAID%7CNONE%7CMCSYNCSOP%7C411-18898%7CvVersion%7C5.2.0; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=D25F69AF1C257696F487AFA6A659D80F1; _vwo_ds=3%3At_0%2Ca_0%3A-1%241632140424%3A37.60075558%3A%3A%3A3_0%2C2_0%3A1; s_cc=true; _wingify_pc_uuid=ec3a6a0422f24564861672af796d1dd8; wingify_donot_track_actions=0; s_sq=%5B%5BB%5D%5D; _vwo_sn=0%3A12; AKA_A2=A; _abck=6BE8A62128915119FB376EAE349CBA03~0~YAAQnfI3F94LJeR7AQAApMNjAwYE5PoOwQRBvvm0SYd36aLIBcFacjA6D3XfIE/2tUbYkwYM5IeqAAFdwquIAtb+dJ0pNFVzoVSTHYwBhNWSlA8kJBpf4TtsmxVhIAKpGR5cFg0ZS1sU2+VLMBda9vhmVxooAU9hmrehOE90FQ4seU/QUld7pUzwABZ0qRmRpr9d2gGkyoGNTUQo0clN/KnxMsubu02rj9fZCr0bhOXLf5KIUK5xirulhMx17LkQ8X+H1OO5nSOITt1o7UTEhRh1EEjyKyKQOoB6G63wNdTK2rxP37jU+/CdOWJum+8TqZyMq6UMJaK2Rvtz3o+WnPVR2bWXbFfnXliEDyyIUJ8YxoabHQnjDcNNcAc1XWj9Wf1H8QodHl5Yjw+9/jl7ClKMKV0RGn0uDdlV6zmtIg==~-1~||-1||~-1; RT="z=1&dm=www.yellowpages.com.au&si=239c3d74-0971-432e-8d9e-3df1784fc8a7&ss=ktsm97w1&sl=e&tt=1yei&obo=8&rl=1&nu=283aozcg&cl=2ero3&ld=2ero8&r=1e7n40kg1&ul=2erob'
    }

    res = requests.get(url, headers=headers)

    soup = BeautifulSoup(res.text, 'html.parser')
    item = soup.findAll('div', 'Box__Div-dws99b-0 bMUVdR MuiPaper-root MuiCard-root MuiPaper-elevation1 MuiPaper-rounded')
    for it in item:
        name = it.find('a', 'MuiTypography-root MuiLink-root MuiLink-underlineNone MuiTypography-colorPrimary').text 
        count +=1
        print(count, name)

