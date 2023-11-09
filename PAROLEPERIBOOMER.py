meme_dict = {"CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            }
for i in range(10):
    parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")            

    if parola in meme_dict.keys():
        print (meme_dict[parola])
    
    else:
        print("prova a riscrivere la parola")
