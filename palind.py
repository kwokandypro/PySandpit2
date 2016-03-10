# -*- coding: utf-8 -*-


def palindrome_verif():
	Mot = raw_input("Tapez votre mot \n")
	
	Comptage = len(Mot)
	Lett_Sep = list(Mot)
	Decompte = 0
	Der_Lett = Comptage	
	
	if ((Comptage % 2) == 1):
		ImmPair = (Comptage / 2)+1
		#print(str(Decompte)," et ",str(Der_Lett))
		#print(str(Decompte)," et ",str(ImmPair))
		while Decompte < ImmPair:
			print(str(Decompte)," et ",str(Der_Lett))
			if Lett_Sep[Decompte] == Lett_Sep[Der_Lett-1]:
				print("Même lettre")
				Decompte += 1
				Der_Lett -= 1
			else:
				print("Ceci n'est pas un palindrome")
				return 0000
				#break
	elif ((Comptage % 2) == 0):
		Pair = Comptage / 2
		while Decompte < Pair:
			print(str(Decompte)," et ",str(Der_Lett))
			if Lett_Sep[Decompte] == Lett_Sep[Der_Lett-1]:
				print("Même lettre")
				Decompte += 1
				Der_Lett -= 1
			else:
				print("Ceci n'est pas un palindrome")
				return 0000
				#break
	
palindrome_verif()
