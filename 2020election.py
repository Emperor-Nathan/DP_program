from bs4 import BeautifulSoup
from requests import get
from tkinter import *
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

states={'alabama':1,
        'alaska':2,
        'arizona':4,
        'arkansas':5,
        'california':6,
        'colorado':8,
        'connecticut':9,
        'delaware':10,
        'district of columbia':11,
        'd.c.':11,
        'dc':11,
        'washington, d.c.':11,
        'washington, dc':11,
        'washington dc':11,
        'washington d.c.':11,
        'florida':12,
        'georgia':13,
        'hawaii':15,
        'idaho':16,
        'illinois':17,
        'indiana':18,
        'iowa':19,
        'kansas':20,
        'kentucky':21,
        'louisiana':22,
        'maine':23,
        'maryland':24,
        'massachusetts':25,
        'michigan':26,
        'minnesota':27,
        'mississippi':28,
        'missouri':29,
        'montana':30,
        'nebraska':31,
        'nevada':32,
        'new hampshire':33,
        'new jersey':34,
        'new mexico':35,
        'new york':36,
        'north carolina':37,
        'north dakota':38,
        'ohio':39,
        'oklahoma':40,
        'oregon':41,
        'pennsylvania':42,
        'rhode island':44,
        'south carolina':45,
        'south dakota':46,
        'tennessee':47,
        'texas':48,
        'utah':49,
        'vermont':50,
        'virginia':51,
        'washington':53,
        'washington state':53,
        'washington (state)':53,
        'west virginia':54,
        'wisconsin':55,
        'wyoming':56,
        'puerto rico':72}

counties={6:{'alameda county':6001,
             'alpine county':6003,
             'amador county':6005,
             'butte county':6007,
             'calaveras county':6009,
             'colusa county':6011,
             'contra costa county':6013,
             'del norte county':6015,
             'el dorado county':6017,
             'fresno county':6019,
             'glenn county':6021,
             'humboldt county':6023,
             'imperial county':6025,
             'inyo county':6027,
             'kern county':6029,
             'kings county':6031,
             'lake county':6033,
             'lassen county':6035,
             'los angeles county':6037,
             'madera county':6039,
             'marin county':6041,
             'mariposa county':6043,
             'mendocino county':6045,
             'merced county':6047,
             'modoc county':6049,
             'mono county':6051,
             'monterey county':6053,
             'napa county':6055,
             'nevada county':6057,
             'orange county':6059,
             'placer county':6061,
             'plumas county':6063,
             'riverside county':6065,
             'sacramento county':6067,
             'san benito county':6069,
             'san bernardino county':6071,
             'san diego county':6073,
             'san francisco county':6075,
             'san joaquin county':6077,
             'san luis obispo county':6079,
             'san mateo county':6081,
             'santa barbara county':6083,
             'santa clara county':6085,
             'santa cruz county':6087,
             'shasta county':6089,
             'sierra county':6091,
             'siskiyou county':6093,
             'solano county':6095,
             'sonoma county':6097,
             'stanislaus county':6099,
             'sutter county':6101,
             'tehama county':6103,
             'trinity county':6105,
             'tulare county':6107,
             'tuolumne county':6109,
             'ventura county':6111,
             'yolo county':6113,
             'yuba county':6115},
          32:{'churchill county':32001,
              'clark county':32003,
              'douglas county':32005,
              'elko county':32007,
              'esmeralda county':32009,
              'eureka county':32011,
              'humboldt county':32013,
              'lander county':32015,
              'lincoln county':32017,
              'lyon county':32019,
              'mineral county':32021,
              'nye county':32023,
              'pershing county':32027,
              'storey county':32029,
              'washoe county':32031,
              'white pine county':32033,
              'carson city':32510},
          36:{'albany county':36001,
              'allegany county':36003,
              'bronx county':36005,
              'broome county':36007,
              'cattaraugus county':36009,
              'cayuga county':36011,
              'chautauqua county':36013,
              'chemung county':36015,
              'chenango county':36017,
              'clinton county':36019,
              'columbia county':36021,
              'cortland county':36023,
              'delaware county':36025,
              'dutchess county':36027,
              'erie county':36029,
              'essex county':36031,
              'franklin county':36033,
              'fulton county':36035,
              'genesee county':36037,
              'greene county':36039,
              'hamilton county':36041,
              'herkimer county':36043,
              'jefferson county':36045,
              'kings county':36047,
              'lewis county':36049,
              'livingston county':36051,
              'madison county':36053,
              'monroe county':36055,
              'montgomery county':36057,
              'nassau county':36059,
              'new york county':36061,
              'niagara county':36063,
              'oneida county':36065,
              'onondaga county':36067,
              'ontario county':36069,
              'orange county':36071,
              'orleans county':36073,
              'oswego county':36075,
              'otsego county':36077,
              'putnam county':36079,
              'queens county':36081,
              'rensselaer county':36083,
              'richmond county':36085,
              'rockland county':36087,
              'st lawrence county':36089,
              'saint lawrence county':36089,
              'st. lawrence county':36089,
              'saratoga county':36091,
              'schenectady county':36093,
              'schoharie county':36095,
              'schuyler county':36097,
              'seneca county':36099,
              'steuben county':36101,
              'suffolk county':36103,
              'sullivan county':36105,
              'tioga county':36107,
              'tompkins county':36109,
              'ulster county':36111,
              'warren county':36113,
              'washington county':36115,
              'wayne county':36117,
              'westchester county':36119,
              'wyoming county':36121,
              'yates county':36123},
          48:{'anderson county':48001,
              'andrews county':48003,
              'angelina county':48005,
              'aransas county':48007,
              'archer county':48009,
              'armstrong county':48011,
              'atascosa county':48013,
              'austin county':48015,
              'bailey county':48017,
              'bandera county':48019,
              'bastrop county':48021,
              'baylor county':48023,
              'bee county':48025,
              'bell county':48027,
              'bexar county':48029,
              'blanco county':48031,
              'borden county':48033,
              'bosque county':48035,
              'bowie county':48037,
              'brazoria county':48039,
              'brazos county':48041,
              'brewster county':48043,
              'briscoe county':48045,
              'brooks county':48047,
              'brown county':48049,
              'burleson county':48051,
              'burnet county':48053,
              'caldwell county':48055,
              'calhoun county':48057,
              'callahan county':48059,
              'cameron county':48061,
              'camp county':48063,
              'carson county':48065,
              'cass county':48067,
              'castro county':48069,
              'chambers county':48071,
              'cherokee county':48073,
              'childress county':48075,
              'clay county':48077,
              'cochran county':48079,
              'coke county':48081,
              'coleman county':48083,
              'collin county':48085,
              'collingsworth county':48087,
              'colorado county':48089,
              'comal county':48091,
              'comanche county':48093,
              'concho county':48095,
              'cooke county':48097,
              'coryell county':48099,
              'cottle county':48101,
              'crane county':48103,
              'crockett county':48105,
              'crosby county':48107,
              'culberson county':48109,
              'dallam county':48111,
              'dallas county':48113,
              'dawson county':48115,
              'deaf smith county':48117,
              'delta county':48119,
              'denton county':48121,
              'dewitt county':48123,
              'dickens county':48125,
              'dimmit county':48127,
              'donley county':48129,
              'duval county':48131,
              'eastland county':48133,
              'ector county':48135,
              'edwards county':48137,
              'ellis county':48139,
              'el paso county':48141,
              'erath county':48143,
              'falls county':48145,
              'fannin county':48147,
              'fayette county':48149,
              'fisher county':48151,
              'floyd county':48153,
              'foard county':48155,
              'fort bend county':48157,
              'franklin county':48159,
              'freestone county':48161,
              'frio county':48163,
              'gaines county':48165,
              'galveston county':48167,
              'garza county':48169,
              'gillespie county':48171,
              'glasscock county':48173,
              'goliad county':48175,
              'gonzales county':48177,
              'gray county':48179,
              'grayson county':48181,
              'gregg county':48183,
              'grimes county':48185,
              'guadalupe county':48187,
              'hale county':48189,
              'hall county':48191,
              'hamilton county':48193,
              'hansford county':48195,
              'hardeman county':48197,
              'hardin county':48199,
              'harris county':48201,
              'harrison county':48203,
              'hartley county':48205,
              'haskell county':48207,
              'hays county':48209,
              'hemphill county':48211,
              'henderson county':48213,
              'hidalgo county':48215,
              'hill county':48217,
              'hockley county':48219,
              'hood county':48221,
              'hopkins county':48223,
              'houston county':48225,
              'howard county':48227,
              'hudspeth county':48229,
              'hunt county':48231,
              'hutchinson county':48233,
              'irion county':48235,
              'jack county':48237,
              'jackson county':48239,
              'jasper county':48241,
              'jeff davis county':48243,
              'jefferson county':48245,
              'jim hogg county':48247,
              'jim wells county':48249,
              'johnson county':48251,
              'jones county':48253,
              'karnes county':48255,
              'kaufman county':48257,
              'kendall county':48259,
              'kenedy county':48261,
              'kent county':48263,
              'kerr county':48265,
              'kimble county':48267,
              'king county':48269,
              'kinney county':48271,
              'kleberg county':48273,
              'knox county':48275,
              'lamar county':48277,
              'lamb county':48279,
              'lampasas county':48281,
              'la salle county':48283,
              'lavaca county':48285,
              'lee county':48287,
              'leon county':48289,
              'liberty county':48291,
              'limestone county':48293,
              'lipscomb county':48295,
              'live oak county':48297,
              'llano county':48299,
              'loving county':48301,
              'lubbock county':48303,
              'lynn county':48305,
              'mcculloch county':48307,
              'mclennan county':48309,
              'mcmullen county':48311,
              'madison county':48313,
              'marion county':48315,
              'martin county':48317,
              'mason county':48319,
              'matagorda county':48321,
              'maverick county':48323,
              'medina county':48325,
              'menard county':48327,
              'midland county':48329,
              'milam county':48331,
              'mills county':48333,
              'mitchell county':48335,
              'montague county':48337,
              'montgomery county':48339,
              'moore county':48341,
              'morris county':48343,
              'motley county':48345,
              'nacogdoches county':48347,
              'navarro county':48349,
              'newton county':48351,
              'nolan county':48353,
              'nueces county':48355,
              'ochiltree county':48357,
              'oldham county':48359,
              'orange county':48361,
              'palo pinto county':48363,
              'panola county':48365,
              'parker county':48367,
              'parmer county':48369,
              'pecos county':48371,
              'polk county':48373,
              'potter county':48375,
              'presidio county':48377,
              'rains county':48379,
              'randall county':48381,
              'reagan county':48383,
              'real county':48385,
              'red river county':48387,
              'reeves county':48389,
              'refugio county':48391,
              'roberts county':48393,
              'robertson county':48395,
              'rockwall county':48397,
              'runnels county':48399,
              'rusk county':48401,
              'sabine county':48403,
              'san augustine county':48405,
              'san jacinto county':48407,
              'san patricio county':48409,
              'san saba county':48411,
              'schleicher county':48413,
              'scurry county':48415,
              'shackelford county':48417,
              'shelby county':48419,
              'sherman county':48421,
              'smith county':48423,
              'somervell county':48425,
              'starr county':48427,
              'stephens county':48429,
              'sterling county':48431,
              'stonewall county':48433,
              'sutton county':48435,
              'swisher county':48437,
              'tarrant county':48439,
              'taylor county':48441,
              'terrell county':48443,
              'terry county':48445,
              'throckmorton county':48447,
              'titus county':48449,
              'tom green county':48451,
              'travis county':48453,
              'trinity county':48455,
              'tyler county':48457,
              'upshur county':48459,
              'upton county':48461,
              'uvalde county':48463,
              'val verde county':48465,
              'van zandt county':48467,
              'victoria county':48469,
              'walker county':48471,
              'waller county':48473,
              'ward county':48475,
              'washington county':48477,
              'webb county':48479,
              'wharton county':48481,
              'wheeler county':48483,
              'wichita county':48485,
              'wilbarger county':48487,
              'willacy county':48489,
              'williamson county':48491,
              'wilson county':48493,
              'winkler county':48495,
              'wise county':48497,
              'wood county':48499,
              'yoakum county':48501,
              'young county':48503,
              'zapata county':48505,
              'zavala county':48507}}

auto={0:{2:{3:201}, # Alaska
         10:{3:1001}, # Delaware
         11:{1:11001, # District of Columbia
             2:1150000,
             3:1101,
             4:1150000},
         30:{3:3001}, # Montana
         38:{3:3801}, # North Dakota
         46:{3:4601}, # South Dakota
         50:{3:5001}, # Vermont
         56:{3:5601}, # Wyoming
         72:{3:7201}}, # Puerto Rico
      1:{32510:{2:3209700, # Carson City, NV
                3:3202,
                4:3294140},
         36005:{2:3651000, # Bronx County, NY
                4:3608510},
         36047:{2:3651000, # Kings County, NY
                4:3610022},
         36061:{2:3651000, # New York County, NY
                4:3644919},
         36081:{2:3651000, # Queens County, NY
                4:3660323},
         36085:{2:3651000, # Richmond County, NY
                3:3611,
                4:3670915}}}

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
        s = input('Enter your county-equivalent: ').lower()
        if s + ' county' in counties[user_local[0]] and user_local[0] != 22 and user_local[0] != 2 and user_local[0] != 72:
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
            user_local[1] = counties[s]
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
    
