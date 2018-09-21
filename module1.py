#!/usr/bin/python3.6
# -*-coding:utf-8 -*


def replay():
	other = input("Tu veux savoir autre chose ? oui ou non ?  ")
	return other

def la_date_des_prochaines_vacances():
	print("""
***Programme mis à jour pour l'année scolaire 2018 et 2019 uniquement***

J'ai besoin de la date d'aujourd'hui pour te dire quand seront les prochaines 
vacances :)
""")
	mois = input("Indique le mois en chiffre : ")
	mois = int(mois)
	jour = input("Indique le jour en chiffre : ")
	jour = int(jour)

	if (mois == 5) or (mois == 6 and jour < 8):
		print("Les grandes vacances débutent le 8 juin")
	elif (mois == 6 and jour > 8) or (mois == 7 or mois == 8 or mois == 9) or (mois == 10 and jour < 20):
		print("Les vacances de la toussaint débutent le 20 octobre")
	elif (mois == 10 and jour > 20) or (mois == 11 and jour > 5) or (mois == 12 and jour < 22):
		print("Les vacances de noel débutent le 22 décembre")
	elif (mois == 12 and jour > 22) or mois == 1 or (mois == 2 and jour < 9):
		print("Les vacances d'hiver débutent le 9 février")
	elif (mois == 2 and jour > 9) or mois == 3 or (mois == 4 and jour < 6):
		print("Les vacances de printemps débutent le 6 arvil")
	else:
		print("Relance le programme et écris correctement s'il te plaît :)")


def les_dates_de_vacances_de_l_annee():
	print("""
***Programme mis à jour pour l'année scolaire 2018 et 2019 uniquement***

			Vacances de printemps

- Fin des cours : mercredi 25 avril 2018 - Jour de reprise : lundi 14 mai 2018
	
			Vacances d'été

- Fin des cours : vendredi 8 juin 2018 - Jour de reprise : lundi 3 septembre 2018

			Vacances de la Toussaint

- Fin des cours : vendredi 20 octobre 2018 - Jour de reprise : lundi 5 novembre 2018

			Vacances de Noel

- Fin des cours : vendredi 22 décembre 2018 - Jour de reprise : lundi 7 janvier 2019

			Vacances d'hiver

- Fin des cours : vendredi 9 février 2019 - Jour de reprise : lundi 25 février 2019

			Vacances de printemps

- Fin des cours : vendredi 6 avril 2019 - Jour de reprise : lundi 22 avril 2019

			Vacances d'été

- Fin des cours : vendredi 7 juillet 2019 - Jour de reprise : lundi 31 août 2019

""")


def les_jours_feries():
	print("""
Jour de l'an -- > 1 Janvier 
Lundi de Pâques -- > 2 Avril 	
Fête du Travail -- > 1 Mai 
8 Mai 1945 -- > 8 Mai 
Jeudi de l'Ascension -- > 10 Mai 	
Lundi de Pentecôte -- >	21 Mai 	
Fête Nationale -- > 14 Juillet
Assomption -- >	15 Août 	
La Toussaint -- > 1 Novembre 	
Armistice -- > 11 Novembre 	
Noël -- > 25 Décembre 	

""")

def les_jours_importants():
	print("""
Epiphanie -- > 6 Janvier 
La Chandeleur -- > 2 Février 
Saint Valentin -- > 14 Février 
Mardi Gras -- >	13 Février 	
Fête des Grands Mères -- > 4 Mars 
Saint Patrick -- > 17 Mars 
Fête des Mères -- > 27 Mai 
Fête des Pères -- > 17 Juin 
Fête de la Musique -- >	21 Juin
""")