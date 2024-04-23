utilisateurs = {'yacine': "1234",'u2':"4321",'u3':"0000"}
mdp_verif=True
etoile="**********************************"

print("",etoile)

while (mdp_verif):
    
    #print(utilisateurs.items()) #c'est pour vérifier si le dic est bien def
    
    u1=input("* Saisir votre nom d'utilisateur: ")
    
    if(u1 in utilisateurs.keys()):
        existe=True
        print("* L'utilisateur existe.\n",etoile)
        
    elif(u1.upper() in utilisateurs.keys()):
        existe=True
        u1=u1.upper()
        print("* L'utilisateur existe.\n",etoile)
        
    elif(u1.lower() in utilisateurs.keys()):
        existe=True
        u1=u1.lower()
        print("* L'utilisateur existe.\n",etoile)    
    
    else:
        existe=False

    
    if (existe): #pour éviter la casse
        
        for i in range(3):
            a=True #condition pour  renvoyer le "trop de tentatives"
            m=False #condition pour  renvoyer le "l'utilisateur n'existe pas"
            
            m1=input("* Saisir votre mot de passe: ")
            
            if(m1==utilisateurs[u1]):
                
                print("* /Access Granted/ *\n\n",etoile)
                #pour mettre fin à la boucle while:
                mdp_verif=False
                a=False #pour ne pas afficher le "trop de tentatives" alors qu'on a le bon mdp  
                break 
            
            else:
                print("* Mauvais mot de passe !\n\n* Il ne ous reste que",2-i,"tentatives.\n",etoile)
                #le 2-i sert à afficher le nombre de tentatives restant avant que l'access se bloque 
        
            if(2-i==0):
                print("* Trop de tentatives !\n\n",etoile,"\n")
                mdp_verif=False
    
    else:
        print("* L'utilisateur", u1 ,"n'existe pas !\n\n",etoile)
        