#data, loginy, pomocne radky atd

loginy = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}
meziradek = 30 * '-'
texts = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]



#zacatek
print(meziradek)
print('Welcome to the app. Please log in.')
jmeno = input('Username: ')
heslo = input('Password: ')
print(meziradek)

#kontrola loginu a hesla
if loginy.get(jmeno) == heslo :
	print('We know you! Hello and continue please.')
else:
    print('Get out, stranger.')
    exit()

#vyber textu
print(meziradek)
print('We have 3 texts to be analyzed.')
numtext = input('Enter number 1, 2 or 3 to select text: ')

if numtext == '1':
    selecttext = texts[0]
elif numtext == '2':
    selecttext = texts[1]
elif numtext == '3':
    selecttext = texts[2]
else:
    print('Wrong number, bye.')
    exit()

#prace s textem
print(meziradek)
countwords = len(selecttext.split())
print('There are ',countwords, 'words in the selected text.')

titlecount = 0
titletext = selecttext.split()
while titletext:
    titleword = titletext.pop(0)
    if titleword.istitle():
        titlecount = titlecount +1
print('There are ',titlecount, 'titlecase words.')

uppercount = 0
uppertext = selecttext.split()
while uppertext:
    upperword = uppertext.pop(0)
    if upperword.isupper():
        uppercount = uppercount +1
print('There are ', uppercount, 'uppercase words.')

lowercount = 0
lowertext = selecttext.split()
while lowertext:
    lowerword = lowertext.pop(0)
    if lowerword.islower():
        lowercount = lowercount +1
print('There are ', lowercount, 'lowercase words.')

numercount = 0
numertext = selecttext.split()
while numertext:
    numerword = numertext.pop(0)
    if numerword.isnumeric():
        numercount = numercount +1
print('There are ', numercount,'numeric strings.')

print(meziradek)


#graf
graftext = selecttext.replace(',','').replace('.','')
graftext = graftext.split()

print(graftext)
counts = {}
for i in graftext:
    if len(i) not in counts:
        counts[len(i)] = 1
    else:
        counts[len(i)]+=1

counts = sorted(counts.items(), key=lambda x:x[0])

for j in counts:
    print(str(j[0])+"\t\t"+(int(j[1])*'*')+' '+str(j[1]))

print(meziradek)

#soucet cisel
numersumm = 0
numertextsumm = selecttext.split()
while numertextsumm:
    numerwordsumm = numertextsumm.pop(0)
    if numerwordsumm.isnumeric():
        numersumm = numersumm + int(numerwordsumm)
print('If we summed all the numbers in this text we would get:', numersumm)

print(meziradek)















