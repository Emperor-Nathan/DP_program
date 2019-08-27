from bs4 import BeautifulSoup
from requests import get
from tkinter import *
from location_data import *
tk = Tk()
c = Canvas(tk, width=700, height=800)
c.pack()
tk.update()

yes='ye'
no='no'
abstain='ab'
 
issues=[yes, yes, no, yes, yes, yes, #Education
        yes, yes, yes, yes, yes, yes, yes, #Environmental issues
        yes, yes, yes, #Gun control
        yes, yes, yes, #Health care
        yes, #Technology
        yes, yes, no, yes, yes, #Economics
        no, yes, yes, yes, no, yes, #Labor and welfare issues
        abstain, yes, yes, abstain, no, abstain, yes, #Foreign involvement
        no, no, yes, yes, yes, yes, abstain, yes, #Immigration and border security
        yes, #Donald Trump
        yes, yes, yes, no, yes, yes, yes, abstain, yes, #Electoral reform
        yes, yes, yes, yes, #Campaign finance
        yes, yes, abstain, no, #Abortion
        yes, abstain, abstain, yes, yes, yes, yes, yes, #Criminal justice
        yes, yes, yes, #LGBT issues
        yes] #Candidate solidarity

user_local = [6, 6001, 626000, 615, 691070]

categories=[['Education', 0, 5],
            ['Environmental issues', 6, 12],
            ['Gun control', 13, 15],
            ['Health care', 16, 18],
            ['Technology', 19, 19],
            ['Economics', 20, 24],
            ['Labor and welfare issues', 25, 30],
            ['Foreign involvement', 31, 37],
            ['Immigration and border security', 38, 45],
            ['Donald Trump', 46, 46],
            ['Electoral reform', 47, 55],
            ['Campaign finance', 56, 59],
            ['Abortion', 60, 63],
            ['Criminal justice', 64, 71],
            ['LGBT issues', 72, 74],
            ['Candidate solidarity', 75, 75]]

questions=['Tuition-Free Public College', #Education
           'Debt relief for student loans', #Education
           'Affirmative Action', #Education
           'Universal Child Care', #Education
           'Public Pre-Kindergarten', #Education
           'Increase funding for primary and secondary public education', #Education
           'Green New Deal', #Environment
           'No Fossil Fuel Money pledge', #Environment
           'Nuclear Power to Reduce Emissions', #Environment
           'Carbon Tax', #Environment
           'Paris Agreement', #Environment
           'Ban Fracking', #Environment
           'Ban Offshore Drilling', #Environment
           'Universal Background Checks', #Gun
           'Ban Assault Weapons', #Gun
           'Mandatory gun buybacks', #Gun
           'Support Single-Payer Healthcare System', #Health
           'Support Public Health Insurance Option', #Health
           'Import Prescription Drugs from Canada', #Health
           'Reinstate Net Neutrality', #Technology
           'Estate Tax', #Economics
           'Postal Banking', #Economics
           'Reparations for Slavery', #Economics
           'Wealth Tax', #Economics
           'Breaking up the largest banks', #Economics
           'Raise Minimum Wage', #Labor
           'Basic Income', #Labor
           'Paid Family Leave', #Labor
           'Paid Sick Leave', #Labor
           'Limit "right-to-work" laws', #Labor
           'Job guarantee', #Labor
           'Intervention in Syria', #Foreign
           'Iran Nuclear Deal', #Foreign
           'Recognize Juan Guadió as Interim President of Venezuela', #Foreign
           'Military Intervention in Venezuela', #Foreign
           'Intervention in Yemen', #Foreign
           'Drone Strikes', #Foreign
           'Decrease the annual military budget', #Foreign
           'Proposed Trump Border Wall', #Immigration
           'Trump Travel Ban', #Immigration
           'Support DACA', #Immigration
           'Allow More Visa Workers', #Immigration
           'Demilitarize Mexico-United States border', #Immigration
           'Invest in Ports of Entry', #Immigration
           'Abolish ICE', #Immigration
           'Decriminalize entering the US illegally', #Immigration
           'Impeachment of Donald Trump', #Trump
           'Abolish the Electoral College', #Electoral
           'Abolish the filibuster', #Electoral
           'Adoption of ranked-choice voting', #Electoral
           'Ban Voter ID Laws', #Electoral
           'District of Columbia statehood', #Electoral
           'Puerto Rico statehood', #Electoral
           'End Felony Disenfranchisement', #Electoral
           'Expand/Reform Supreme Court', #Electoral
           'Make Election Day a federal holiday', #Electoral
           'No Corporate PAC Donations', #Campaign finance
           'Overturn Citizens United', #Campaign finance
           'Publicly funded elections', #Campaign finance
           'Democracy vouchers', #Campaign finance
           'Support right to abortion', #Abortion
           'Contraceptive mandate', #Abortion
           'Fund Planned Parenthood', #Abortion
           'Retain Hyde Amendment', #Abortion
           'End Capital Punishment', #Criminal
           'Legalization of Marijuana', #Criminal
           'Expunging Cannabis Conviction Records', #Criminal
           'End Cash Bail', #Criminal
           'End Private Prisons', #Criminal
           'End Mandatory Minimum Sentencing for Nonviolent Drug Offenses', #Criminal
           'Job Placement Services for Released Offenders', #Criminal
           'Decriminalization of Sex Work', #Criminal
           'Laws against LGBT discrimination',
           'Same-sex marriage',
           'Transgender Military Service',
           'Support the eventual Democratic nominee']

candidates={'Ben':0, 'Bid':0, 'Boo':0, 'Bul':0, 'But':0, 'Cas':0, 'de ':0,
            'Del':0, 'Gab':0, 'Gil':0, 'Gra':0, 'Har':0,
            'Hic':0, 'Ins':0, 'Klo':0, 'Mes':0,
            'Mou':0, 'Oje':0, 'O\'R':0, 'Rya':0, 'San':0, 'Ses':0, 'Ste':0, 'Swa':0,
            'War':0, 'Wil':0, 'Yan':0}

withdrawn = []

experience={'Ben':4365/21, 'Bid':2922/2+13161/21, 'Boo':2621/21+2740/71, 'Bul':2919/3,
            'But':2926/71, 'Cas':907/15+1877/71, 'de ':2576/71, 'Del':2191/27,
            'Gab':2922/27+720/109, 'Gil':4360/21+754/27, 'Gra':4383/21+1460/109,
            'Har':1461/21, 'Hic':2919/3+2731/71,
            'Ins':2919/3+4825/27+730/27+1463/109, 'Klo':5114/21, 'Mes':2121/71,
            'Mou':2192/27, 'Oje':774/108, 'O\'R':2191/27, 'Rya':6575/27+715/108,
            'San':5114/21+5844/27+2920/71, 'Ses':1461/27, 'Ste':0, 'Swa':2922/27, 'War':2922/21, 'Wil':0,
            'Yan':0}

candidate_names={'Ben':'Michael Bennet', 'Bid':'Joe Biden', 'Boo':'Cory Booker',
                 'Bul':'Steve Bullock',
                 'But':'Pete Buttigieg', 'Cas':'Julián Castro',
                 'de ':'Bill de Blasio',
                 'Del':'John Delaney', 'Gab':'Tulsi Gabbard',
                 'Gil':'Kirsten Gillibrand', 'Gra':'Mike Gravel',
                 'Har':'Kamala Harris', 'Hic':'John Hickenlooper',
                 'Ins':'Jay Inslee', 'Klo':'Amy Klobuchar', 'Mes':'Wayne Messam',
                 'Mou':'Seth Moulton',  'Oje':'Richard Ojeda', 'O\'R':'Beto O\'Rourke', 'Rya':'Tim Ryan',
                 'San':'Bernie Sanders', 'Ses':'Joe Sestak', 'Ste':'Tom Steyer', 'Swa':'Eric Swalwell',
                 'War':'Elizabeth Warren', 'Wil':'Marianne Williamson',
                 'Yan':'Andrew Yang'}

ages={'Ben':20507, 'Bid':28551, 'Boo':18896, 'Bul':20008, 'But':14246, 'Cas':16928, 'Del':21099,
      'de ':21807,
      'Gab':14528, 'Gil':19766, 'Gra':33125, 'Har':20546, 'Hic':25185, 'Ins':25548,
      'Klo':22175, 'Mes':17029, 'Mou':15429, 'Oje':18380, 'O\'R':17648, 'Rya':17355, 'San':28989, 'Ses':25242, 'Ste':23218, 'Swa':14675,
      'War':26145, 'Wil':25033, 'Yan':16809}

local = {'Ben':[8, 8031, 820000, 801, 891007],
         'Bid':[10, 10003, 1077580, 1001, 1093996],
         'Boo':[34, 34013, 3451000, -1, 3451000],
         'Bul':[30, 30049, 3035600, 3001, 3091722],
         'But':[18, 18141, 1871000, 1802, -1],
         'Cas':[48, -1, 4865000, -1, 4865000],
         'de ':[36, 36047, 3651000, -1, 3610022],
         'Del':[24, 24031, 2463300, 2406, -1],
         'Gab':[15, 15003, -1, 1502, -1],
         'Gil':[36, 36021, 3635969, 3619, 3635969],
         'Gra':[6, 6081, 609066, 614, 691370],
         'Har':[6, 6037, 644000, -1, -1],
         'Hic':[8, 8031, 820000, 801, 891007],
         'Ins':[53, 53035, 5303736, 5306, 5390120],
         'Klo':[27, 27053, 2744000, 2705, 2743000],
         'Mes':[12, 12011, 1245975, 1220, 1292236],
         'Mou':[25, 25009, 2559105, 2506, 2559105],
         'Oje':[54, -1, -1, 5403, -1],
         'O\'R':[48, 48141, 4824000, 4816, 4824000],
         'Rya':[39, 39155, 3955196, 3913, -1],
         'San':[50, 50007, 5010675, 5001, 5010675],
         'Ses':[42, -1, -1, -1, -1],
         'Ste':[6, -1, -1, -1, -1],
         'Swa':[6, 6001, 620018, 615, 691660],
         'War':[25, 25017, 2511000, -1, 2511000],
         'Wil':[19, -1, 1921000, 1903, -1],
         'Yan':[36, 36061, 3651000, -1, 3644919]}

#==BEGIN==
abcounttotal = {'Ben':0,'Bid':0,'Boo':0,'Bul':0,'But':0,'Cas':0,'de ':0,'Del':0,
                'Gab':0,'Gil':0,'Gra':0,'Har':0,'Hic':0,'Ins':0,'Klo':0,'Mes':0,
                'Mou':0,'Oje':0,'O\'R':0,'Rya':0,'San':0,'Ses':0,'Ste':0,'Swa':0,
                'War':0,'Wil':0,'Yan':0}
#==END==

priority=[len(questions), 21, 5, 5]

ide_priority=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

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
        s='Type the number of what you want to set.\n0. Continue'
        q=0
        while q<len(categories):
            s+='\n'+str(q+1)+'. '+categories[q][0]
            q+=1
        s+='\n'
        n = input(s)
        if not isInt(n):
            print('Invalid input.')
        else:
            n = int(n)
            printIdeSettings()
            if n == 0:
                break
            elif n > 0 and n < 16:
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
        if s == 'N/A':
            user_local[2] = 0
        elif s in cities[user_local[0]]:
            user_local[2] = cities[user_local[0]][s]
            break
        else:
            print('Invalid input.')
    for a in auto[2]:
        if user_local[2] == a:
            for b in auto[2][a]:
                user_local[b] = auto[2][a][b]
    if not (0 in user_local):
        return
    while True:
        if user_local[3] != 0:
            break
        s = int(input('Enter your U.S. house district number: '))
        if not isInt(s):
            print('Invalid input.')
        elif s >= 1 and s <= cds[user_local[0]]:
            user_local[3] = user_local[0]*100+s
            break
        else:
            print('Invalid input.')
    for a in auto[3]:
        if user_local[3] == a:
            for b in auto[3][a]:
                user_local[b] = auto[3][a][b]
    if not (0 in user_local):
        return

def takeQuiz():
    n = 0
    print('For each question, type "yes", "no", or "abstain". Typing "y" or "n" will also suffice. This is not case-sensitive.\n')
    while n < 72:
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
            k = str(columns[0])[21] + str(columns[0])[22] + str(columns[0])[23]
            if 'Withdrawn' in str(columns[1]):
                withdrawn.append(candidate_names[k])
            del columns[1]
            if k in candidates:
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
                        candidates[k] -= v #==BEGIN==
                    elif str(d)[17]+str(d)[18] != 'pa':
                        abcounttotal[k]+=1
                    #==END==
                    m += 1
    for a in candidates:
        candidates[a] *= priority[0]/len(questions)
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
        r += 56 - 1.9*n
        n+=1
    return r

def printResults():
    n = 0
    while n < len(preference):
        if preference[n][0] in withdrawn:
            c.create_text(350, sum_notation(n+1), anchor=N, font=('Helvetica', int(55-1.9*n)), text = preference[n][0], fill='red')
            c.create_text(20, sum_notation(n+1), anchor=NW, font=('Helvetica', int(55-1.9*n)), text = str(n+1)+'. ', fill='red')
        else:
            c.create_text(350, sum_notation(n+1), anchor=N, font=('Helvetica', int(55-1.9*n)), text = preference[n][0])
            c.create_text(20, sum_notation(n+1), anchor=NW, font=('Helvetica', int(55-1.9*n)), text = str(n+1)+'. ')
        n+=1

setPrefs()
#locate()
c.delete('all')
tk.update()
#takeQuiz()
c.create_text(350, 400, font=('Helvetica', 50), text='Processing...')
tk.update()
getPreferences()
printResults()
    
