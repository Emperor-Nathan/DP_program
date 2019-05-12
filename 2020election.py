from bs4 import BeautifulSoup
from requests import get
from tkinter import *
from location_data import *
tk = Tk()
c = Canvas(tk, width=600, height=700)
c.pack()
tk.update()

yes='ye'
no='no'
abstain='ab'

issues=[yes, yes, abstain, yes, yes, yes, yes, yes, no, no, yes, yes, yes, yes,
        yes, yes, yes, no, yes, yes, yes, yes, no, yes, yes, yes, yes, yes, yes,
        no, yes, yes, yes, abstain, yes, yes, yes, yes, yes, yes, yes, abstain,
        yes, yes, abstain, no, abstain, yes, yes, yes, yes, yes, yes, no, no,
        no, yes, yes, yes, yes, abstain, yes, no, yes, yes, yes, no, yes, yes,
        yes, yes]

user_local = [6, 6001, 626000, 615, 691070]

categories=[['Abortion', 0, 2],
            ['Campaign finance', 3, 6],
            ['Criminal justice', 7, 14],
            ['Economics', 15, 19],
            ['Education', 20, 25],
            ['Electoral reform', 26, 34],
            ['Environmental issues and climate change', 35, 40],
            ['Foreign policy', 41, 47],
            ['Gun control', 48, 49],
            ['Health care', 50, 53],
            ['Immigration and border security', 54, 60],
            ['Internet', 61, 61],
            ['Labor and welfare issues', 62, 67],
            ['LGBT issues', 68, 70]]

questions=['Pro-Choice',
           'Contraceptive mandate',
           'Fund Planned Parenthood',
           'No Corporate PAC Donations',
           'Overturn Citizens United',
           'Publicly funded elections',
           'Democracy vouchers',
           'End Capital Punishment',
           'Legalization of Marijuana',
           'Expunging Cannabis Conviction Records',
           'End Cash Bail',
           'End Private Prisons',
           'End Mandatory Minimum Sentencing for Nonviolent Drug Offenses',
           'Job Placement Services for Released Offenders',
           'Decriminalization of Sex Work',
           'Estate Tax',
           'Postal Banking',
           'Reparations for Slavery',
           'Wealth Tax',
           'Breaking up the largest banks',
           'Tuition-Free Public College',
           'Debt relief for student debt',
           'Affirmative Action',
           'Universal Child Care',
           'Public Pre-Kindergarten',
           'Increase funding for primary and secondary public education',
           'Abolish the Electoral College',
           'Abolish the filibuster',
           'Adoption of ranked-choice voting',
           'Ban Voter ID Laws',
           'District of Columbia statehood',
           'Puerto Rico statehood',
           'End Felony Disenfranchisement',
           'Expand/Reform Supreme Court',
           'Make Election Day a federal holiday',
           'Green New Deal',
           'Nuclear Power to Reduce Emissions',
           'Carbon Tax',
           'Paris Agreement',
           'Ban Fracking',
           'Ban Offshore Drilling',
           'Intervention in Syria',
           'Iran Nuclear Deal',
           'Recognize Juan Guadió as Interim President of Venezuela',
           'Military Intervention in Venezuela',
           'Intervention in Yemen',
           'Drone Strikes',
           'Decrease the annual military budget',
           'Universal Background Checks',
           'Ban Assault Weapons',
           'Support Single-Payer Healthcare System',
           'Support Public Health Insurance Option',
           'Import Prescription Drugs from Canada',
           'Support federal caps on medical malpractice lawsuits',
           'Proposed Trump Border Wall',
           'Trump Travel Ban',
           'Support DACA',
           'Allow More Visa Workers',
           'Demilitarize Mexico-United States border',
           'Invest in Ports of Entry',
           'Abolish ICE',
           'Reinstate Net Neutrality',
           'Raise Minimum Wage',
           'Basic Income',
           'Paid Family Leave',
           'Paid Sick Leave',
           'Limit "right-to-work" laws',
           'Job guarantee',
           'Laws against LGBT discrimination',
           'Same-sex marriage',
           'Transgender Military Service']

candidates={'Be':0, 'Bi':0, 'Bo':0, 'Bu':0, 'Ca':0,
            'De':0, 'Ga':0, 'Gi':0, 'Gr':0, 'Ha':0,
            'Hi':0, 'In':0, 'Kl':0, 'Me':0,
            'Mo':0, 'O\'':0, 'Ry':0, 'Sa':0, 'Sw':0,
            'Wa':0, 'Wi':0, 'Ya':0}

experience={'Be':4365/21, 'Bi':2922/2+13161/21, 'Bo':2621/21+2740/71,
            'Bu':2926/71, 'Ca':907/15+1877/71, 'De':2191/27,
            'Ga':2922/27+720/109, 'Gi':4360/21+754/27, 'Gr':4383/21+1460/109,
            'Ha':1461/21, 'Hi':2919/3+2731/71,
            'In':2919/3+4825/27+730/27+1463/109, 'Kl':5114/21, 'Me':2121/71,
            'Mo':2192/27, 'O\'':2191/27, 'Ry':6575/27+715/108,
            'Sa':5114/21+5844/27+2920/71, 'Sw':2922/27, 'Wa':2922/21, 'Wi':0,
            'Ya':0}

candidate_names={'Be':'Michael Bennet', 'Bi':'Joe Biden', 'Bo':'Cory Booker',
                 'Bu':'Pete Buttigieg', 'Ca':'Julián Castro',
                 'De':'John Delaney', 'Ga':'Tulsi Gabbard',
                 'Gi':'Kirsten Gillibrand', 'Gr':'Mike Gravel',
                 'Ha':'Kamala Harris', 'Hi':'John Hickenlooper',
                 'In':'Jay Inslee', 'Kl':'Amy Klobuchar', 'Me':'Wayne Messam',
                 'Mo':'Seth Moulton',  'O\'':'Beto O\'Rourke', 'Ry':'Tim Ryan',
                 'Sa':'Bernie Sanders', 'Sw':'Eric Swalwell',
                 'Wa':'Elizabeth Warren', 'Wi':'Marianne Williamson',
                 'Ya':'Andrew Yang'}

ages={'Be':20507, 'Bi':28551, 'Bo':18896, 'Bu':14246, 'Ca':16928, 'De':21099,
      'Ga':14528, 'Gi':19766, 'Gr':33125, 'Ha':20546, 'Hi':25185, 'In':25548,
      'Kl':22175, 'Me':17029, 'Mo':15429, 'O\'':17648, 'Ry':17355, 'Sa':28989,
      'Sw':14736, 'Wa':26145, 'Wi':25033, 'Ya':16809}

local = {'Be':[8, 8031, 820000, 801, 891007],
         'Bi':[10, 10003, 1077580, 1001, 1093996],
         'Bo':[34, 34013, 3451000, 0, 3451000],
         'Bu':[18, 18141, 1871000, 1802, 0],
         'Ca':[48, 0, 4865000, 0, 4865000],
         'De':[24, 24031, 2463300, 2406, 0],
         'Ga':[15, 15003, 0, 1502, 0],
         'Gi':[36, 36021, 3635969, 3619, 3635969],
         'Gr':[6, 6081, 609066, 614, 691370],
         'Ha':[6, 6037, 644000, 0, 691750],
         'Hi':[8, 8031, 820000, 801, 891007],
         'In':[53, 53035, 5303736, 5306, 5390120],
         'Kl':[27, 27053, 2744000, 2705, 2743000],
         'Me':[12, 12011, 1245975, 1220, 1292236],
         'Mo':[25, 25009, 2559105, 2506, 2559105],
         'O\'':[48, 48141, 4824000, 4816, 4824000],
         'Ry':[39, 39155, 3955196, 3913, 0],
         'Sa':[50, 50007, 5010675, 5001, 5010675],
         'Sw':[6, 6001, 620018, 615, 691660],
         'Wa':[25, 25017, 2511000, 0, 2511000],
         'Wi':[6, 6037, 0, 633, 0],
         'Ya':[36, 36061, 3651000, 0, 3644919]}

priority=[71, 21, 5, 5]

ide_priority=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

preference=[]

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def printIdeSettings():
    n = 0
    c.delete('all')
    while n < len(ide_priority):
        c.create_rectangle(50, 50*n+25, 50+ide_priority[n]*100, 50*(n+1), fill='red')
        c.create_text(50, 50*n+25, text=categories[n][0], anchor=SW)
        c.create_text(25, 50*(n+1)-12.5, text=ide_priority[n])
        n+=1
    tk.update()

def printSettings():
    c.delete('all')
    c.create_rectangle(50, 25, 50+priority[0]*5, 50, fill='red')
    c.create_rectangle(50, 75, 50+priority[1]*5, 100, fill='orange')
    c.create_rectangle(50, 125, 50+priority[2]*5, 150, fill='green')
    c.create_rectangle(50, 175, 50+priority[3]*5, 200, fill='blue')
    c.create_text(25, 37.5, text=priority[0])
    c.create_text(25, 87.5, text=priority[1])
    c.create_text(25, 137.5, text=priority[2])
    c.create_text(25, 187.5, text=priority[3])
    c.create_text(50+priority[0]*5, 37.5, anchor=W, text='   Ideology')
    c.create_text(50+priority[1]*5, 87.5, anchor=W, text='   Experience')
    c.create_text(50+priority[2]*5, 137.5, anchor=W, text='   Age')
    c.create_text(50+priority[3]*5, 187.5, anchor=W, text='   Locality')
    tk.update()

def setIdePrefs():
    n = 0
    printIdeSettings()
    while True:
        n = input('Type the number of what you want to set.\n0. Continue\n1. Abortion\n2. Campaign finance\n3. Criminal justice\n4. Economics\n5. Education\n6. Electoral reform\n7. Environmental issues and climate change\n8. Foreign policy\n9. Gun control\n10. Health care\n11. Immigration and border security\n12. Internet\n13. Labor and welfare issues\n14. LGBT issues\n')
        if not isInt(n):
            print('Invalid input.')
        else:
            n = int(n)
            printIdeSettings()
            if n == 0:
                break
            elif n > 0 and n < 15:
                a = input('Enter weight: ')
                if isInt(a):
                    ide_priority[n-1] = int(a)
                else:
                    print('Invalid input.')
            else:
                print('Invalid input.')
            printIdeSettings()
            

def setPrefs():
    printSettings()
    while True:
        n = input('Type the number of what you want to do.\n1. Set ideology weight\n2. Set experience weight\n3. Set age weight\n4. Set locality weight\n5. Continue\n')
        if n == '1':
            priority[0] = int(input('Enter ideology weight: '))
        elif n == '2':
            priority[1] = int(input('Enter experience weight: '))
        elif n == '3':
            priority[2] = int(input('Enter age weight: '))
        elif n == '4':
            priority[3] = int(input('Enter locality weight: '))
        elif n == '5':
            break
        else:
            print('Invalid input.')
        printSettings()
    setIdePrefs()

def locate():
    user_local[0] = 0
    user_local[1] = 0
    user_local[2] = 0
    user_local[3] = 0
    user_local[4] = 0
    print('This program will now ask you for your location. It supports the 50 states, the District of Columbia, and Puerto Rico, but does not support the other territories, or foreign countries.')
    while True:
        if user_local[0] != 0:
            break
        s = input('Enter your state-equivalent: ').lower()
        if s in states:
            user_local[0] = states[s]
            break
        else:
            print('Invalid input.')
    l = False
    for a in local:
        if local[a][0] == user_local[0]:
            l = True
    if not l:
        return
    for a in auto[0]:
        if user_local[0] == a:
            for b in auto[0][a]:
                user_local[b] = auto[0][a][b]
    if not (0 in user_local):
        return
    while True:
        if user_local[1] != 0:
            break
        s = input('Enter your county-equivalent: ').lower()
        if s in counties[user_local[0]]:
            user_local[1] = counties[user_local[0]][s]
            break
        elif s + ' county' in counties[user_local[0]] and user_local[0] != 22 and user_local[0] != 2 and user_local[0] != 72:
            s += ' county'
        elif s + ' parish' in counties[user_local[0]]:
            s += ' parish'
        elif s + ' borough' in counties[user_local[0]]:
            s += ' borough'
        elif s + ' census area' in counties[user_local[0]]:
            s += ' census area'
        elif s + ' municipality' in counties[user_local[0]]:
            s += ' municipality'
        if s in counties[user_local[0]]:
            user_local[1] = counties[user_local[0]][s]
            break
        else:
            print('Invalid input.')
    l = False
    for a in local:
        if local[a][1] == user_local[1]:
            l = True
    if not l:
        return
    for a in auto[1]:
        if user_local[1] == a:
            for b in auto[1][a]:
                user_local[b] = auto[1][a][b]
    if not (0 in user_local):
        return
    while True:
        if user_local[2] != 0:
            break
        s = input('Enter your city, town, village, or census-designated place. If you live outside one of these, enter "N/A". (Note: Do NOT enter a civil township. That will be dealt with later on.): ').lower()
        if s in cities[user_local[0]]:
            user_local[2] = cities[user_local[0]][s]
            break
        else:
            print('Invalid input.')
    l = False
    for a in local:
        if local[a][2] == user_local[2]:
            l = True
    if not l:
        return
    for a in auto[2]:
        if user_local[2] == a:
            for b in auto[2][a]:
                user_local[b] = auto[2][a][b]
    if not (0 in user_local):
        return

def takeQuiz():
    n = 0
    print('For each question, type "yes", "no", or "abstain". Typing "y" or "n" will also suffice. This is not case-sensitive.\n')
    while n < 71:
        a = input(questions[n] + ': ')
        if a.lower() == 'yes' or a.lower() == 'y':
            issues[n] = yes
        elif a.lower() == 'no' or a.lower() == 'n':
            issues[n] = no
        else:
            issues[n] = abstain
        n+=1

def sort():
    global preference
    n = len(preference)
    while n >= 1:
        newn = 0
        i = 1
        while i < n:
            if preference[i-1][1] < preference[i][1]:
                temp = preference[i-1]
                preference[i-1] = preference[i]
                preference[i] = temp
                newn = i
            i += 1
        n = newn

def getPreferences():
    global preference
    response1 = get('https://en.wikipedia.org/wiki/Political_positions_of_the_2020_Democratic_Party_presidential_primary_candidates')
    response = BeautifulSoup(response1.content, 'html.parser')
    tables = response.find_all('table')
    del tables[0]
    del tables[0]
    del tables[len(tables)-1]
    del tables[len(tables)-1]
    del tables[len(tables)-1]
    del tables[len(tables)-1]
    del tables[len(tables)-1]
    del tables[len(tables)-1]
    del tables[len(tables)-1]
    n = 0
    m = 0
    for a in tables:
        n += m
        m = 0
        rows = a.find_all('tr')
        del rows[0]
        for b in rows:
            m = 0
            columns = b.find_all('td')
            del columns[1]
            k = str(columns[0])[21] + str(columns[0])[22]
            del columns[0]
            for d in columns:
                v = 1
                q = 0
                while q < len(categories):
                    if n+m >= categories[q][1] and n+m <= categories[q][2]:
                        v *= ide_priority[q]
                    q += 1
                if str(d)[17]+str(d)[18] == issues[n+m]:
                    candidates[k] += v
                elif (str(d)[17]+str(d)[18] == no and issues[n+m]==yes) or (str(d)[17]+str(d)[18]==yes and issues[n+m]==no):
                    candidates[k] -= v
                m += 1
    for a in candidates:
        candidates[a] *= priority[0]/71
        candidates[a] += (experience[a]/100)*(priority[1]/21)
        candidates[a] -= (ages[a]/7300)*(priority[2]/5)
        y = 0
        while y < 5:
            if user_local[y] == local[a][y]:
                candidates[a] += priority[3]/5
            y+=1
        preference.append([candidate_names[a], candidates[a]])
    sort()
    n = 1
    c.delete('all')
    tk.update()

def sum_notation(x):
    n = 1
    r = 0
    while n < x:
        r += 55 - 2*n
        n+=1
    return r

def printResults():
    n = 0
    while n < len(preference):
        c.create_text(300, sum_notation(n+1), anchor=N, font=('Helvetica', int(50-2*n)), text = preference[n][0])
        c.create_text(20, sum_notation(n+1), anchor=NW, font=('Helvetica', int(50-2*n)), text = str(n+1)+'. ')
        n+=1

setPrefs()
locate()
c.delete('all')
tk.update()
#takeQuiz()
c.create_text(300, 350, font=('Helvetica', 50), text='Processing...')
tk.update()
getPreferences()
printResults()
    
