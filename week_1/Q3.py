import time

def printLyrics():
	songLyrics = "Meri kismat ke har ek panne pe Mere jeete ji baad marne ke#Mere har ik kal har ik lamhe me#Tu likh de mera usey#Har kahaani me saare qisson me#Dil ki duniya ke sacche rishton me#Zindagani ke saare hisso mein#Tu likh de mera usey#Aye Khuda aye Khuda jab bana uska hi bana#Aye Khuda aye Khuda jab bana uska hi bana#Uska hoon uss me hoon uss se hoon#Usi ka rehne de#Main toh pyaasa hoon hai#Dariya woh zariya woh jeene ka mere#Mujhe ghar de gali de shehar de#Usi ke naam ke"
	songSplit  = songLyrics.split("#")

	for i in songSplit:
		print(i)
		time.sleep(1)

printLyrics()