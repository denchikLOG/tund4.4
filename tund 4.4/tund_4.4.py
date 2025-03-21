#Ü4

post_index=input("Sisesta postiindeks: ")
if len(post_index)!=5 or not post_index.isdigit():
    print("Vigane sisend! Postiindeks peab olema 5 numbrit pikk.")
else:
    maakond_number=int(post_index[0])
    if maakond_number==1:
        print("Maakond: Tallinn")
        print("Jää kodus!")
    elif maakond_number==2:
        print("Maakond: Narva, Narva-Jõesuu")
        print("Jää kodus!")
    elif maakond_number==3:
        print("Maakond: Kohtla-Järve")
        print("Jää kodus!")
    elif maakond_number==4:
        print("Maakond: Ida-Virumaa, Lääne-Virumaa, Jõgevamaa")
        print("Naiske maski!")
    elif maakond_number==5:
        print("Maakond: Tartu linn")
        print("Kanda maski!")
    elif maakond_number==6:
        print("Maakond: Tartumaa, Põlvamaa, Võrumaa, Valgamaa")
        print("Kanda maski!")
    elif maakond_number==7:
        print("Maakond: Viljandimaa, Järvamaa, Harjumaa, Raplamaa")
        print("Kanda maski!")
    elif maakond_number==8:
        print("Maakond: Pärnumaa")
        print("Kanda maski!")
    elif maakond_number==9:
        print("Maakond: Läänemaa, Hiiumaa, Saaremaa")
        print("Kanda maski!")
    else:
        print("Vigane postiindeks!")

#Ü9

name=input("Sisesta oma nimi: ")
if name.isalpha():
    name=name.capitalize()
    print(f"Hei,{name}!")
    letter_count=len(name)
    B="aeiouAEIOU"
    Asõnad=0
    Bcount=0
    for char in name:
        if char in B:
            Bcount+=1
        elif char.isalpha():
            Asõnad+=1
    print(f"Kirjadeson,{letter_count},tähte.")
    print(f"Vokaaleon,{Bcount},ja kaashäälikuid,{Asõnad}.")
    unique_sorted_letters=sorted(set(name.lower()))
    print(f"Unikaalsed tähde tähestikus:{''.join(unique_sorted_letters)}")
else:
    print("Viganenimi! Nimis võivad olla ainult tähed.")

#Ü7
numbers=[]
for i in range(10):
    number=int(input("Sisesta numbrid, eraldatud komadega: "))
    numbers.append(number)
sort_type=input("Kas soovite sorteerida kasvavalt (asc) või kahanevalt (desc)? ")
if sort_type=="asc":
    sort_number=sorted(numbers,key=abs)
    print("Kasvav sorteerimine absoluutväärtuse järgi:",sort_number)
elif sort_type=="desc":
    sort_number=sorted(numbers,key=abs,reverse=True)
    print("Kahanev sorteerimine absoluutväärtuse järgi:",sort_number)
else:
    print("Vigane sisend! Palun sisestage 'asc' või 'desc'.")

#Ü5
numbers=[]
for i in range(5):
    number=float(input("Sisesta numbrid, eraldatud komadega: "))
    numbers.append(number)
swap_count=int(input("Kui palju elemente soovite vahetada? "))
if swap_count>len(numbers)//2:
    print("Sa ei saa vahetada rohkem elemente kui listis on pool.")
else:
    for i in range(swap_count):
        numbers[i],numbers[-(i+1)]=numbers[-(i+1)],numbers[i]
    print("Uus nimekiri pärast vahetamist:",numbers)
