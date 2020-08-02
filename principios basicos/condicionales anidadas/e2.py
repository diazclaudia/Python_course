nota1=int(input("Ingrese primer nota:"))
nota2=int(input("Ingrese segunda nota:"))
nota3=int(input("Ingrese tercer nota:"))
media=(nota1+nota2+nota3)/3

if media <= 60:
	print ("insuficiente") 
elif media >= 60 and media < 70:
    print ("regular/bien") 	
elif media >= 70 and media < 80:
    print ("bien")
elif media >= 80 and media < 90:
	print ("suficiente")
else:
	print ("sobresaliente")

       


print ("media "+ str(media))    	
	             

	            