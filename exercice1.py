import random  # Import random module to generate random numbers from gc import is_finalized

print ("######################################")
print ("          *Course name* Airlines")
print ("######################################")
print ("The best airline in the world!")
print ("")
cout_billet = 0
montant_reservation = 0
montant_total = 0
i = 1
choix = 1

while choix == 1 :
    nb_passagers = int(input("How many tickets would you like to book? "))
    print("")

    while i <= nb_passagers :
        print ("============")
        print (F"Passenger {i}/{nb_passagers}")
        print ("============")
        nom_passager = input (F"Passenger name {i} : ")
        age_passager = int(input (F"Passenger age {i} : "))

        if age_passager < 0 :
            print ("Invalid entry. Please enter a valid age")
            i = i - 1

        else :
            if age_passager <= 3 :
                cout_billet = 0

            else :
                if age_passager < 65 :
                    cout_billet = 150

                else :
                    rabais_aleatoire = ((random.randint(15, 55)) / 100)
                    cout_billet = (150 * (1 - rabais_aleatoire))

        if cout_billet > 0 and cout_billet < 150 :
            print (F"Discount applied for {nom_passager} : {int (rabais_aleatoire * 100)}%")

        if age_passager >= 0:
            print (F"Ticket price reserved for {nom_passager} : {cout_billet:.2f}$")
            print ("")
            montant_reservation = (montant_reservation + cout_billet)

        i = i + 1

    if nb_passagers > 0 :
        print (F"Total amount to collect for this booking : {montant_reservation:.2f}$")
        print ("")

    montant_total = (montant_total + montant_reservation)
    choix = 0

    while choix < 1 or choix > 2 :
        print ("1. Register another customer")
        print ("2. Quit")
        choix = int (input ("Enter your choice : "))

        if choix < 1 or choix > 2 :
            print ("Invalid choice. Please enter 1 or 2.")
            print ("")
        i = 1
        montant_reservation = 0

print(F"Total cumulative amount for all registered customers : {montant_total:.2f}$")
print("Bye bye!")