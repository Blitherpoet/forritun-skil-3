#Þröstur Haraldsson
import random
def samlagning(a,b):
    x = a+b
    return x
def margfoldun(fall):
    def inner(a,b):
        return fall(a,b) * 2
    return inner
def margfelditalna(x):
    y = 1
    for i in range(x):
        y=y*(i+1)
    return y
def faeribreyta(func):
            def inner(a):
                if a > 0:
                    x = (func(a))
                    return a
                else:
                    return"Talan er mínustala"
                return inner

def margfelditala(a):
    margfeldi = 1
    for x in range (a):
        margfeldi = margfeldi*(x+1)
    return margfeldi
#liður 4
def samtala(a,b):
                notandalisti = []
                tölvulisti = []
                for i in randomlisti:
                    if i % a == 0:
                        notandalisti.append(i)
                    if i % b == 0:
                        tölvulisti.append(i)
                a = len(notandalisti)
                b = len(tölvulisti)
                return notandalisti, tölvulisti
#liður 10
def afturkvaemt():
            utkoma = 1
            for x in listi:
                if x == 0:
                    utkoma = 0
                else:
                    utkoma = utkoma * x
            return utkoma
#liður 11
def generator(x):
            print(x)
            yield x

afram=0
margfoldun = margfoldun(samlagning)
#while lykkja
while afram==0:
    #valkostir
    print("-------------------BIL--------------------")
    print("Liður 1-11")
    print("12 til að hætta")
    print("-------------------BIL--------------------")
    #notandi veldur lið
    val=int(input("hvað villt þú gera?"))
    if val==1:
        #liður 1
        print("-------------------BIL--------------------")
        a=int(input("Veldu tölu"))
        b=int(input("Veldu aðra tölu"))
        print(samlagning(a,b))
        print(margfoldun(a,b))
    elif val==2:
        #liður 2
        print("-------------------BIL--------------------")
        yey=0
        a2=int(input("Veldu slétta tölu"))
        b2=int(input("Veldu aðra slétta tölu"))
        if a2 % 2!=0:
            yey=1
        if b2 % 2!=0:
            yey=1
        if yey==1:
            print("Þetta þurfa að vera sléttar tölur!")
        #Hér eru tölur lagt saman tölur
        print(samlagning(a2,b2))
        #Hér eru tölur margfaldaðar saman
        print(margfoldun(a2,b2))
    elif val == 3:
        print("-------------------BIL--------------------")
        print(margfelditala(5))
    elif val == 4:
        print("-------------------BIL--------------------")
        svar = "j"
        while svar == "j":
            randomlisti = []
            for x in range(20):
                randomlisti.append(random.randint(1,100))
            notandi = int(input("Sláðu inn eina tölu á milli 1-10 "))
            talva = random.randint(1, 10)
            print("Talvan kaus:",talva)
            x = samtala(notandi,talva)
            notandalisti = x[0]
            tölvulisti= x[1]
            a = len(notandalisti)
            b = len(tölvulisti)
            print("Notandi:",x[0])
            print("Notandinn var með:",a,"tölur")
            print("Talva:",x[1])
            print("Talvan var með:",b,"tölur")
            if a>b:
                print("Notandi vann!")
            elif a<b:
                print("Talvan vann!")
            else:
                print("Jafntefli")
            if notandi >= 1 and notandi <= 10:
                print(samtala(notandi,talva))
            else:
                print("Talan þarf að vera á milli 1-10")
            svar = input("Sláðu inn J ef þú villt spila aftur ").lower()

    elif val == 5:
        print("-------------------BIL--------------------")
        randomlisti = []
        for x in range(100):
            randomlisti.append(random.randint(200,600))
        print("Listinn:", randomlisti)
        jafnlist = list(filter(lambda x:(x%2==0), randomlisti))
        print("Jafnar tölurnar úr listanum:",jafnlist)

    elif val == 6:
        print("-------------------BIL--------------------")
        randomlisti = []
        for x in range(100):
            randomlisti.append(random.randint(200, 600))
        print("Listinn:", randomlisti)
        fimmlist = list(filter(lambda x:(x%5==0 and x>350), randomlisti))
        print("Tölur í listanum sem ganga upp í 5 og eru stærri en 350:",fimmlist)

    elif val == 7:
        print("-------------------BIL--------------------")
        randomlisti = []
        for x in range(200):
            randomlisti.append(random.randint(100, 900))
        print("Listinn:",randomlisti)
        minuslisti = list(map(lambda x: x-2, randomlisti))
        print("Sami listi nema mínusað 2 við tölurnar:",minuslisti)

    elif val == 8:
        print("-------------------BIL--------------------")
        randomlisti = []
        for x in range(200):
            randomlisti.append(random.randint(1, 90))
        print("Upprunalegi listi:",randomlisti)
        undirsex = list(filter(lambda x:(x<6), randomlisti))
        print("Allar tölur undir 6:",undirsex)
        þridjaveldi = list(map(lambda x: x**3, undirsex))
        print("Allar tölur undir 6 í þriðjaveldi:",þridjaveldi)

    elif val == 9:
        print("-------------------BIL--------------------")
        randomlisti = []
        for x in range(100):
            randomlisti.append(random.randint(1,20))
        print("Upprunalegi listi:",randomlisti)
        tiutolur = list(filter(lambda x: (x%10==0), randomlisti))
        tiutolur.sort()
        tiutolur.reverse()
        print("Allar tölur sem enda á 0 í röð:",tiutolur)

    elif val == 10:
        print("-------------------BIL--------------------")
        listi = []
        for x in range(10):
            listi.append(random.randint(1,100))
        print("Listinn:",listi)
        print("Margfeldi allra talna í listanum:",afturkvaemt())

    elif val == 11:
        print("-------------------BIL--------------------")
        randomlisti = []
        for x in range(100):
            randomlisti.append(random.randint(1,100))
        for x in randomlisti:
            y = generator(x)
            next(y)
    elif val == 12:
        print("-------------------BIL--------------------")
        print("Vertu bless")
        afram=1
    else:
        print("-------------------BIL--------------------")
        print("Vitlaust val")