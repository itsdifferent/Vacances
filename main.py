#!/usr/bin/python3.6
# -*-coding:utf-8 -*

d = 1

while d == 1:
	choice = input("""
	Que veux-tu connaître ?

- la date des prochaines vacances
- les dates de vacances de l'année
- (prochainement le compteur avant les vacances)
- les jours fériés
- les jours importants 

--> """)


	if choice == "la date des prochaines vacances":
		from fonctionne import la_date_des_prochaines_vacances
		la_date_des_prochaines_vacances()
		from fonctionne import replay
		replay()
		if replay() == "non":
			break
	elif choice == "les dates de vacances de l'année":
		from fonctionne import les_dates_de_vacances_de_l_annee
		les_dates_de_vacances_de_l_annee()
		from fonctionne import replay
		replay()
		if replay() == "non":
			break
	elif choice == "les jours fériés":
		from fonctionne import les_jours_feries
		les_jours_feries()
		from fonctionne import replay
		replay()
		if replay() == "non":
			break
	elif choice == "les jours importants":
		from fonctionne import les_jours_importants
		les_jours_importants()
		from fonctionne import replay	
		replay()
		if replay() == "non":
			break
	else: 
		print("Ecris ta réponse correctement s'il te plaît :)")



