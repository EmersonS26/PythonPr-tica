carros1 = str(input("Digite seu carro: "))
carros = {
    "Mercedez-Benz" : {"Nome":"Mercedez classic","Ano":2024,"Estado":"Novo"},
    "BMW" : {"Nome":"Bmw Adventure","Ano":2024,"Estado":"Usado"},
    "Lamborghini" : {"Nome":"URUS","Ano":2024,"Estado":"Novo"},
    "Renault" : {"Nome":"Clio","Ano":2023,"Estado":"Semi-Novo"},
    "Volkswagen" : {"Nome":"Golf","Ano":2024,"Estado":"Novo"}
}

if(carros1 == "mercedez"):
    print(carros.get("Mercedez-Benz"))
elif(carros1 == "bmw" or carros1 == "x1"):
    print(carros.get("BMW"))
elif(carros1 == "lamborghini"):
    print(carros.get("Lamborghini"))
elif(carros1 == "gol" or carros1 == "volks"):
    print(carros.get("Volkswagen"))
elif(carros1 == "renault" or carros1 == "clio"):
    print(carros.get("Renault"))
else:
    print("Carro indiponível!")
    


    
