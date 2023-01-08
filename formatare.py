import csv

# dict={'1.500': 'Bucureşti, Sector 3, zona Basarabia (Titan)\n310 m (4 minute)',
#       '290': 'Bucuresti, Sector 1, zona Cismigiu (Ultracentral)',
#       '420': 'Bucureşti, Sector 4 zona Drumul Taberei',
#       '330': 'Bucuresti, zona Dorobanti\n760 m (10 minute)',
#       '335': 'Bucureşti, zona Tineretului\n430 m (5 minute)',
#       '299': 'Bucureşti, zona Iancului',
#       '410': 'Bucureşti, Sector 2, zona Muncii',
#       '300': 'Bucureşti, zona Cotroceni',
#       '329': 'Bucureşti, Sector 3, zona Timpuri Noi (Tineretului)\n400 m (5 minute)',
#       '350': 'Bucureşti, Sector 6, zona Gorjului (Militari)',
#       '400': 'Bucuresti, Sector 1, zona Baneasa',
#       '375': 'Bucureşti, zona Virtuţii (Militari)\n110 m (1 minut)',
#       '370': 'Bucureşti, zona Drumul Taberei',
#       '900': 'Bucureşti, Sector 1 zona Viilor (Rahova)',
#       '220': 'Bucureşti, zona Militari',
#       '365': 'Bucureşti, Sector 2 zona Obor (Colentina)',
#       '270': 'Bucureşti, Sector 5 zona Drumul Taberei\n650 m (8 minute)'}
# sector_1={}
# sector_2={}
# sector_3={}
# sector_4={}
# sector_5={}
# sector_6={}
#
# for key in dict:
#       if 'Sector' in dict[key]:
#             if 'Sector 1' in dict[key]:
#                   sector_1[key]=dict[key]
#
#
#
# print(sector_1)


#### Bucata asta e pt calculul mediei

dict={'360': 'Bucureşti, Sector 1, zona Romană (Ultracentral)\\n200 m (3 minute)', '450': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '340': 'Bucureşti, Sector 1, zona Banu Manta (1 Mai)\\n480 m (6 minute)', '500': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n660 m (8 minute)', '339': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)\\n480 m (6 minute)', '349': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n270 m (3 minute)', '300': 'Bucureşti, Sector 1, zona 1 Mai', '420': 'Bucureşti, Sector 1, zona Jiului (Bucurestii Noi)\\n300 m (4 minute)', '290': 'Bucuresti, Sector 1, zona Cismigiu (Ultracentral)', '270': 'Bucureşti, Sector 1, zona P-ţa Romană (Ultracentral)\\n100 m (1 minut)', '1.095': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '350': 'Bucureşti, Sector 1, zona Titulescu (1 Mai)\\n480 m (6 minute)', '230': 'Bucureşti, Sector 1, zona 1 Mai\\n660 m (8 minute)', '480': 'Bucuresti, Sector 1, zona Calea Victoriei (Ultracentral)\\n320 m (4 minute)', '370': 'Bucuresti, Sector 1, zona Baneasa', '320': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n540 m (7 minute)', '379': 'Bucureşti, Sector 1, zona Romană (Ultracentral)', '600': 'Bucureşti, Sector 1, zona Domenii (1 Mai)\\n420 m (5 minute)', '390': 'Bucuresti, Sector 1, zona Magheru (Ultracentral)\\n360 m (5 minute)', '280': 'Bucureşti, Sector 1, zona Turda (1 Mai)', '400': 'Bucureşti, Sector 1, zona Iancu Nicolae (Pipera)', '530': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '499': 'Bucureşti, Sector 1, zona Domenii (1 Mai)', '490': 'Bucuresti, Sector 1, zona P-ta Victoriei (Ultracentral)\\n210 m (3 minute)', '440': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n40 m (1 minut)', '200': 'Bucuresti, Sector 1, zona P-ta Universitatii (Ultracentral)\\n110 m (1 minut)', '630': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '550': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '700': 'Bucureşti, Sector 1, zona Herăstrău (Herastrau)\\n530 m (7 minute)', '460': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)', '750': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '1.300': 'Bucureşti, Sector 1, zona Floreasca\\n680 m (9 minute)', '244': 'Bucureşti, Sector 1, zona 1 Mai', '185': 'Bucuresti, Sector 1, zona Antiaeriana (Rahova)', '1.000': 'Bucuresti, Sector 1, zona Romana (Ultracentral)\\n530 m (7 minute)'}
#
# print(len(dict))
# sum=0
# for key in dict:
#     if len(key)>=4:
#         sum+=float(key)/5*1000
#         # print(key)
#         # print(float(key)/5*100)
#     else:
#         sum+=float(key)
#     print(key)
#
# ### acum calculeaza bine
# print(sum/len(dict))

######
import pandas as pd


# with open ('test.csv','w', encoding="utf-8") as file:
#     file.write('Rent,Address\n')
#     writer=csv.writer(file)
#     for key,value in dict.items():
#
#         if len(key)>=4:
#             new_key=round(float(key)/4.90*1000)
#             new_key=int(new_key)
#             writer.writerow([new_key, value])
#         else:
#             key=int(key)
#             writer.writerow([key, value])
#
# df=pd.read_csv('test.csv')
# print(df)

### pana aici formatez datele si le trec intr-un csv.. tot ce e de tipul 1200 e in lei si fac si conversie


#
#
sectorul_1={'360': 'Bucureşti, Sector 1, zona Romană (Ultracentral)\\n200 m (3 minute)', '450': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '340': 'Bucureşti, Sector 1, zona Banu Manta (1 Mai)\\n480 m (6 minute)', '500': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n660 m (8 minute)', '339': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)\\n480 m (6 minute)', '349': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n270 m (3 minute)', '300': 'Bucureşti, Sector 1, zona 1 Mai', '420': 'Bucureşti, Sector 1, zona Jiului (Bucurestii Noi)\\n300 m (4 minute)', '290': 'Bucuresti, Sector 1, zona Cismigiu (Ultracentral)', '270': 'Bucureşti, Sector 1, zona P-ţa Romană (Ultracentral)\\n100 m (1 minut)', '1.095': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '350': 'Bucureşti, Sector 1, zona Titulescu (1 Mai)\\n480 m (6 minute)', '230': 'Bucureşti, Sector 1, zona 1 Mai\\n660 m (8 minute)', '480': 'Bucuresti, Sector 1, zona Calea Victoriei (Ultracentral)\\n320 m (4 minute)', '370': 'Bucuresti, Sector 1, zona Baneasa', '320': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n540 m (7 minute)', '379': 'Bucureşti, Sector 1, zona Romană (Ultracentral)', '600': 'Bucureşti, Sector 1, zona Domenii (1 Mai)\\n420 m (5 minute)', '390': 'Bucuresti, Sector 1, zona Magheru (Ultracentral)\\n360 m (5 minute)', '280': 'Bucureşti, Sector 1, zona Turda (1 Mai)', '400': 'Bucureşti, Sector 1, zona Iancu Nicolae (Pipera)', '530': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '499': 'Bucureşti, Sector 1, zona Domenii (1 Mai)', '490': 'Bucuresti, Sector 1, zona P-ta Victoriei (Ultracentral)\\n210 m (3 minute)', '440': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n40 m (1 minut)', '200': 'Bucuresti, Sector 1, zona P-ta Universitatii (Ultracentral)\\n110 m (1 minut)', '630': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '550': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '700': 'Bucureşti, Sector 1, zona Herăstrău (Herastrau)\\n530 m (7 minute)', '460': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)', '750': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '1.300': 'Bucureşti, Sector 1, zona Floreasca\\n680 m (9 minute)', '244': 'Bucureşti, Sector 1, zona 1 Mai', '185': 'Bucuresti, Sector 1, zona Antiaeriana (Rahova)', '1.000': 'Bucuresti, Sector 1, zona Romana (Ultracentral)\\n530 m (7 minute)'}
# sectorul_2={'360': 'Bucureşti, Sector 1, zona Romană (Ultracentral)\\n200 m (3 minute)', '450': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '340': 'Bucureşti, Sector 1, zona Banu Manta (1 Mai)\\n480 m (6 minute)', '500': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n660 m (8 minute)', '339': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)\\n480 m (6 minute)', '349': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n270 m (3 minute)', '300': 'Bucureşti, Sector 1, zona 1 Mai', '420': 'Bucureşti, Sector 1, zona Jiului (Bucurestii Noi)\\n300 m (4 minute)', '290': 'Bucuresti, Sector 1, zona Cismigiu (Ultracentral)', '270': 'Bucureşti, Sector 1, zona P-ţa Romană (Ultracentral)\\n100 m (1 minut)', '1.095': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '350': 'Bucureşti, Sector 1, zona Titulescu (1 Mai)\\n480 m (6 minute)', '230': 'Bucureşti, Sector 1, zona 1 Mai\\n660 m (8 minute)', '480': 'Bucuresti, Sector 1, zona Calea Victoriei (Ultracentral)\\n320 m (4 minute)', '370': 'Bucuresti, Sector 1, zona Baneasa', '320': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n540 m (7 minute)', '379': 'Bucureşti, Sector 1, zona Romană (Ultracentral)', '600': 'Bucureşti, Sector 1, zona Domenii (1 Mai)\\n420 m (5 minute)', '390': 'Bucuresti, Sector 1, zona Magheru (Ultracentral)\\n360 m (5 minute)', '280': 'Bucureşti, Sector 1, zona Turda (1 Mai)', '400': 'Bucureşti, Sector 1, zona Iancu Nicolae (Pipera)', '530': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '499': 'Bucureşti, Sector 1, zona Domenii (1 Mai)', '490': 'Bucuresti, Sector 1, zona P-ta Victoriei (Ultracentral)\\n210 m (3 minute)', '440': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n40 m (1 minut)', '200': 'Bucuresti, Sector 1, zona P-ta Universitatii (Ultracentral)\\n110 m (1 minut)', '630': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '550': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '700': 'Bucureşti, Sector 1, zona Herăstrău (Herastrau)\\n530 m (7 minute)', '460': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)', '750': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '1.300': 'Bucureşti, Sector 1, zona Floreasca\\n680 m (9 minute)', '244': 'Bucureşti, Sector 1, zona 1 Mai', '185': 'Bucuresti, Sector 1, zona Antiaeriana (Rahova)', '1.000': 'Bucuresti, Sector 1, zona Romana (Ultracentral)\\n530 m (7 minute)'}
# sectorul_3={'360': 'Bucureşti, Sector 1, zona Romană (Ultracentral)\\n200 m (3 minute)', '450': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '340': 'Bucureşti, Sector 1, zona Banu Manta (1 Mai)\\n480 m (6 minute)', '500': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n660 m (8 minute)', '339': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)\\n480 m (6 minute)', '349': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n270 m (3 minute)', '300': 'Bucureşti, Sector 1, zona 1 Mai', '420': 'Bucureşti, Sector 1, zona Jiului (Bucurestii Noi)\\n300 m (4 minute)', '290': 'Bucuresti, Sector 1, zona Cismigiu (Ultracentral)', '270': 'Bucureşti, Sector 1, zona P-ţa Romană (Ultracentral)\\n100 m (1 minut)', '1.095': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '350': 'Bucureşti, Sector 1, zona Titulescu (1 Mai)\\n480 m (6 minute)', '230': 'Bucureşti, Sector 1, zona 1 Mai\\n660 m (8 minute)', '480': 'Bucuresti, Sector 1, zona Calea Victoriei (Ultracentral)\\n320 m (4 minute)', '370': 'Bucuresti, Sector 1, zona Baneasa', '320': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n540 m (7 minute)', '379': 'Bucureşti, Sector 1, zona Romană (Ultracentral)', '600': 'Bucureşti, Sector 1, zona Domenii (1 Mai)\\n420 m (5 minute)', '390': 'Bucuresti, Sector 1, zona Magheru (Ultracentral)\\n360 m (5 minute)', '280': 'Bucureşti, Sector 1, zona Turda (1 Mai)', '400': 'Bucureşti, Sector 1, zona Iancu Nicolae (Pipera)', '530': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '499': 'Bucureşti, Sector 1, zona Domenii (1 Mai)', '490': 'Bucuresti, Sector 1, zona P-ta Victoriei (Ultracentral)\\n210 m (3 minute)', '440': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n40 m (1 minut)', '200': 'Bucuresti, Sector 1, zona P-ta Universitatii (Ultracentral)\\n110 m (1 minut)', '630': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '550': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '700': 'Bucureşti, Sector 1, zona Herăstrău (Herastrau)\\n530 m (7 minute)', '460': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)', '750': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '1.300': 'Bucureşti, Sector 1, zona Floreasca\\n680 m (9 minute)', '244': 'Bucureşti, Sector 1, zona 1 Mai', '185': 'Bucuresti, Sector 1, zona Antiaeriana (Rahova)', '1.000': 'Bucuresti, Sector 1, zona Romana (Ultracentral)\\n530 m (7 minute)'}
# sectorul_4={'360': 'Bucureşti, Sector 1, zona Romană (Ultracentral)\\n200 m (3 minute)', '450': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '340': 'Bucureşti, Sector 1, zona Banu Manta (1 Mai)\\n480 m (6 minute)', '500': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n660 m (8 minute)', '339': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)\\n480 m (6 minute)', '349': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n270 m (3 minute)', '300': 'Bucureşti, Sector 1, zona 1 Mai', '420': 'Bucureşti, Sector 1, zona Jiului (Bucurestii Noi)\\n300 m (4 minute)', '290': 'Bucuresti, Sector 1, zona Cismigiu (Ultracentral)', '270': 'Bucureşti, Sector 1, zona P-ţa Romană (Ultracentral)\\n100 m (1 minut)', '1.095': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '350': 'Bucureşti, Sector 1, zona Titulescu (1 Mai)\\n480 m (6 minute)', '230': 'Bucureşti, Sector 1, zona 1 Mai\\n660 m (8 minute)', '480': 'Bucuresti, Sector 1, zona Calea Victoriei (Ultracentral)\\n320 m (4 minute)', '370': 'Bucuresti, Sector 1, zona Baneasa', '320': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n540 m (7 minute)', '379': 'Bucureşti, Sector 1, zona Romană (Ultracentral)', '600': 'Bucureşti, Sector 1, zona Domenii (1 Mai)\\n420 m (5 minute)', '390': 'Bucuresti, Sector 1, zona Magheru (Ultracentral)\\n360 m (5 minute)', '280': 'Bucureşti, Sector 1, zona Turda (1 Mai)', '400': 'Bucureşti, Sector 1, zona Iancu Nicolae (Pipera)', '530': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '499': 'Bucureşti, Sector 1, zona Domenii (1 Mai)', '490': 'Bucuresti, Sector 1, zona P-ta Victoriei (Ultracentral)\\n210 m (3 minute)', '440': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n40 m (1 minut)', '200': 'Bucuresti, Sector 1, zona P-ta Universitatii (Ultracentral)\\n110 m (1 minut)', '630': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '550': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '700': 'Bucureşti, Sector 1, zona Herăstrău (Herastrau)\\n530 m (7 minute)', '460': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)', '750': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '1.300': 'Bucureşti, Sector 1, zona Floreasca\\n680 m (9 minute)', '244': 'Bucureşti, Sector 1, zona 1 Mai', '185': 'Bucuresti, Sector 1, zona Antiaeriana (Rahova)', '1.000': 'Bucuresti, Sector 1, zona Romana (Ultracentral)\\n530 m (7 minute)'}
# sectorul_5={'360': 'Bucureşti, Sector 1, zona Romană (Ultracentral)\\n200 m (3 minute)', '450': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '340': 'Bucureşti, Sector 1, zona Banu Manta (1 Mai)\\n480 m (6 minute)', '500': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n660 m (8 minute)', '339': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)\\n480 m (6 minute)', '349': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n270 m (3 minute)', '300': 'Bucureşti, Sector 1, zona 1 Mai', '420': 'Bucureşti, Sector 1, zona Jiului (Bucurestii Noi)\\n300 m (4 minute)', '290': 'Bucuresti, Sector 1, zona Cismigiu (Ultracentral)', '270': 'Bucureşti, Sector 1, zona P-ţa Romană (Ultracentral)\\n100 m (1 minut)', '1.095': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '350': 'Bucureşti, Sector 1, zona Titulescu (1 Mai)\\n480 m (6 minute)', '230': 'Bucureşti, Sector 1, zona 1 Mai\\n660 m (8 minute)', '480': 'Bucuresti, Sector 1, zona Calea Victoriei (Ultracentral)\\n320 m (4 minute)', '370': 'Bucuresti, Sector 1, zona Baneasa', '320': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n540 m (7 minute)', '379': 'Bucureşti, Sector 1, zona Romană (Ultracentral)', '600': 'Bucureşti, Sector 1, zona Domenii (1 Mai)\\n420 m (5 minute)', '390': 'Bucuresti, Sector 1, zona Magheru (Ultracentral)\\n360 m (5 minute)', '280': 'Bucureşti, Sector 1, zona Turda (1 Mai)', '400': 'Bucureşti, Sector 1, zona Iancu Nicolae (Pipera)', '530': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '499': 'Bucureşti, Sector 1, zona Domenii (1 Mai)', '490': 'Bucuresti, Sector 1, zona P-ta Victoriei (Ultracentral)\\n210 m (3 minute)', '440': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n40 m (1 minut)', '200': 'Bucuresti, Sector 1, zona P-ta Universitatii (Ultracentral)\\n110 m (1 minut)', '630': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '550': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '700': 'Bucureşti, Sector 1, zona Herăstrău (Herastrau)\\n530 m (7 minute)', '460': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)', '750': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '1.300': 'Bucureşti, Sector 1, zona Floreasca\\n680 m (9 minute)', '244': 'Bucureşti, Sector 1, zona 1 Mai', '185': 'Bucuresti, Sector 1, zona Antiaeriana (Rahova)', '1.000': 'Bucuresti, Sector 1, zona Romana (Ultracentral)\\n530 m (7 minute)'}
# sectorul_6={'360': 'Bucureşti, Sector 1, zona Romană (Ultracentral)\\n200 m (3 minute)', '450': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '340': 'Bucureşti, Sector 1, zona Banu Manta (1 Mai)\\n480 m (6 minute)', '500': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n660 m (8 minute)', '339': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)\\n480 m (6 minute)', '349': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n270 m (3 minute)', '300': 'Bucureşti, Sector 1, zona 1 Mai', '420': 'Bucureşti, Sector 1, zona Jiului (Bucurestii Noi)\\n300 m (4 minute)', '290': 'Bucuresti, Sector 1, zona Cismigiu (Ultracentral)', '270': 'Bucureşti, Sector 1, zona P-ţa Romană (Ultracentral)\\n100 m (1 minut)', '1.095': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '350': 'Bucureşti, Sector 1, zona Titulescu (1 Mai)\\n480 m (6 minute)', '230': 'Bucureşti, Sector 1, zona 1 Mai\\n660 m (8 minute)', '480': 'Bucuresti, Sector 1, zona Calea Victoriei (Ultracentral)\\n320 m (4 minute)', '370': 'Bucuresti, Sector 1, zona Baneasa', '320': 'Bucureşti, Sector 1, zona Calea Victoriei (Ultracentral)\\n540 m (7 minute)', '379': 'Bucureşti, Sector 1, zona Romană (Ultracentral)', '600': 'Bucureşti, Sector 1, zona Domenii (1 Mai)\\n420 m (5 minute)', '390': 'Bucuresti, Sector 1, zona Magheru (Ultracentral)\\n360 m (5 minute)', '280': 'Bucureşti, Sector 1, zona Turda (1 Mai)', '400': 'Bucureşti, Sector 1, zona Iancu Nicolae (Pipera)', '530': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '499': 'Bucureşti, Sector 1, zona Domenii (1 Mai)', '490': 'Bucuresti, Sector 1, zona P-ta Victoriei (Ultracentral)\\n210 m (3 minute)', '440': 'Bucuresti, Sector 1, zona Universitate (Ultracentral)\\n40 m (1 minut)', '200': 'Bucuresti, Sector 1, zona P-ta Universitatii (Ultracentral)\\n110 m (1 minut)', '630': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '550': 'Bucureşti, Sector 1, zona Aviaţiei (Aviatiei)', '700': 'Bucureşti, Sector 1, zona Herăstrău (Herastrau)\\n530 m (7 minute)', '460': 'Bucureşti, Sector 1, zona Victoriei (Ultracentral)', '750': 'Bucureşti, Sector 1, zona Băneasa (Baneasa)', '1.300': 'Bucureşti, Sector 1, zona Floreasca\\n680 m (9 minute)', '244': 'Bucureşti, Sector 1, zona 1 Mai', '185': 'Bucuresti, Sector 1, zona Antiaeriana (Rahova)', '1.000': 'Bucuresti, Sector 1, zona Romana (Ultracentral)\\n530 m (7 minute)'}
# list=[sectorul_1,sectorul_2,sectorul_3,sectorul_4,sectorul_5,sectorul_6]
#
# for item in list:
#     print(item)



from transformation import Transformation

sector_1=Transformation(name='test',dict=sectorul_1)
sector_1.content()


import matplotlib.pyplot as plt
import pandas as pd

df_sector_1=pd.read_csv('sector_1.csv')
df_sector_2=pd.read_csv('sector_2.csv')
df_sector_3=pd.read_csv('sector_3.csv')
df_sector_4=pd.read_csv('sector_4.csv')
df_sector_5=pd.read_csv('sector_5.csv')
df_sector_6=pd.read_csv('sector_6.csv')

print(df_sector_1['Rent'].mean())
print(df_sector_2['Rent'].mean())
print(df_sector_3['Rent'].mean())
print(df_sector_4['Rent'].mean())
print(df_sector_5['Rent'].mean())
print(df_sector_6['Rent'].mean())


courses = ['Sectorul 1','Sectorul 2','Sectorul 3','Sectorul 4','Sectorul 5','Sectorul 6']
values = [df_sector_1['Rent'].mean(),
          df_sector_2['Rent'].mean(),
          df_sector_3['Rent'].mean(),
          df_sector_4['Rent'].mean(),
          df_sector_5['Rent'].mean(),
          df_sector_6['Rent'].mean(),]

fig = plt.figure(figsize=(10, 5))
plt.xlabel('Sectors')
plt.ylabel('Rents € ')
# creating the bar plot
plt.bar(courses, values, color=['maroon','red','pink','green','blue','purple'],
        width=0.4)
plt.show()

print(df_sector_1['Rent'])
print(df_sector_1['Rent'].sum())
### asa fac graf tip coloana


