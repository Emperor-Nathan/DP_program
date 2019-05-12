from bs4 import BeautifulSoup
from requests import get

def getCounties(state, fips):
    response1=get('https://www2.census.gov/geo/pvs/bas/bas19maps/st'+str(fips)+'_'+state+'/cou/')
    response=BeautifulSoup(response1.content, 'html.parser')
    table=response.find('table')
    rows=response.find_all('tr')
    data=[]
    del rows[0]
    del rows[0]
    del rows[0]
    del rows[len(rows)-1]
    for a in rows:
        data.append(a.find_all('td')[1].find('a'))
    for a in data:
        n = 16
        s = ''
        while str(a)[n] != '/':
            if str(a)[n] == '_':
                s += ' '
            else:
                s += str(a)[n]
            n += 1
        s += ' county'
        print('              \''+s+'\':'+str(a)[10]+str(a)[11]+str(a)[12]+str(a)[13]+str(a)[14]+',')
