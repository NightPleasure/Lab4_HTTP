import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

while True:
    try:
        print("Alege o optiune:")
        print("1 - Enumera lista de categorii")
        print("2 - Arata detalii despre o categorie")
        print("3 - Creaza o categorie noua")
        print("4 - Sterge o categorie")
        print("5 - Modifica titul unei categorii")
        print("6 - Creaza produse noi intr-o categorie")
        print("7 - Arata lista produselor dintr-o categorie")
        print("8 - Exit.")

        choice = input()
        option = int(choice[0])
    except ValueError:
        print("Introdu o varianta de la 1 la 8")
        continue
    except Exception as ex:
        print("Error!")
        print(ex)
        continue

    if option == 1:
        response = requests.get("https://localhost:44370/api/Category/categories", verify=False)
        print(response.json())

    elif option == 2:
        id = input("Introduceti ID-ul produsului: ")
        response = requests.get(f"https://localhost:44370/api/Category/categories/{id}", verify=False)
        print(response.json())

    elif option == 3:
        URL = "https://localhost:44370/api/Category/categories"
        id = input("Introduceti ID-ul produsului: ")
        title = input("Introduceti Titlul produsului: ")
        counter = input("Introduceti numarul de produse: ")
        obj = {
            "id": id,
            "title": title,
            "itemsCount": counter
        }
        post = requests.post(URL, json=obj, verify=False)
        response = requests.get("https://localhost:44370/api/Category/categories", verify=False)
        print(response.json())
        input("Apasa orice :)")

    elif option == 4:
        id = input("Introduceti ID-ul produsului: ")
        deletedObj = requests.delete(f"https://localhost:44370/api/Category/categories/{id}", verify=False)
        response = requests.get("https://localhost:44370/api/Category/categories", verify=False)
        print(response.json())
        input("Apasa orice :)")

    elif option == 5:
        id = input("Introduceti ID-ul produsului: ")
        title = input("Alegeti un titlu nou: ")
        obj = {
            "title": title
        }
        modifyObj = requests.put(f"https://localhost:44370/api/Category/categories/{id}", json=obj, verify=False)
        input("Apasa orice :)")

    elif option == 6:
        id = input("Introduceti ID-ul categoriei: ")
        title = input("Alegeti un titlu nou: ")
        obj = {
            "title": title
        }
        modifyObj = requests.post(f"https://localhost:44370/api/Category/categories/{id}", json=obj, verify=False)
        input("Apasa orice :)")

    elif option == 7:
        id = input("Introduceti ID-ul categoriei: ")
        response = requests.get(f"https://localhost:44370/api/Category/categories/{id}/products", verify=False)
        print(response.json())
    elif option == 8:
        break
