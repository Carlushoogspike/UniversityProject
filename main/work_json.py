import json
import os
from tabulate import tabulate

brands_map = []
brands_file = 'brands.json'

products_map = []
products_file = 'products.json'

categories_map = []
categories_file = 'categories.json'

not_number_in_place = "Não pode conter numeros"


def contains_digit(s):
    return any(char.isdigit() for char in s)


def verify_file(file_name):
    if not os.path.exists(file_name):
        print(f'Não possível encontrar o arquivo {file_name}. Criando...')
        try:
            with open(file_name, 'w') as f:
                print(f"Arquivo {file_name} criado com sucesso.")
            return False
        except IOError:
            print(f'Erro ao criar o arquivo {file_name}')
            return False
    else:
        print(f'Arquivo {file_name} encontrado.')
        return True


def load_brand():
    if not verify_file(brands_file):
        return

    with open(brands_file, 'r', encoding='utf-8') as file:
        file_content = file.read()
        if len(file_content) == 0:
            print('Não há marcas para serem carregadas.')
            return

        data = json.loads(file_content)
        for b in data:
            brands_map.append(b)


def load_categories():
    if not verify_file(categories_file):
        return

    with open(categories_file, 'r', encoding='utf-8') as file:
        file_content = file.read()
        if len(file_content) == 0:
            print('Não há categorias para serem carregadas.')
            return

        data = json.loads(file_content)
        for c in data:
            categories_map.append(c)


load_brand()
load_categories()


def verify_brand(name):
    return name in brands_map


def verify_categories(name):
    return name in categories_map


def create_brand():
    while True:
        try:
            name_brand = input("Digite uma marca: ")

            if contains_digit(name_brand):
                raise ValueError(not_number_in_place)

            if verify_brand(name_brand):
                print("Essa marca já está cadastrada.")
                continue

            print(f"Você cadastrou a marca {name_brand} com sucesso")
            brands_map.append(name_brand)

            with open("brands.json", "w", encoding='utf-8') as file:
                print("Salvando arquivo...")
                json.dump(brands_map, file, ensure_ascii=False)

            option = input("Deseja continuar criando (s/n): ")
            if option == "n":
                break
        except ValueError as e:
            print(f"{e}")


def remove_brand():
    while True:
        print("Marcas Registradas")
        for brand in brands_map:
            print(f'- {brand}')

        print("")
        search_brand = input("Digite o noma da marca que deseja remover: ")

        if not verify_brand(search_brand):
            print("Não foi possivel encontrar essa marca.")
            continue

        print(f"Você removeu com sucesso a marca {search_brand}")

        brands_map.remove(search_brand)
        with open("brands.json", "w", encoding='utf-8') as file:
            print("Salvando arquivo...")
            json.dump(brands_map, file, ensure_ascii=False)

        option = input("Deseja continuar removendo (s/n): ")
        if option == "n":
            break


def request_brand():
    while True:
        try:
            print("Marcas Registradas")
            for brand in brands_map:
                print(f'- {brand}')

            brand = input("Digite uma marca: ")

            if contains_digit(brand):
                raise ValueError(not_number_in_place)

            if not verify_brand(brand):
                print("Você digitou uma marca invalida.")
                continue

            return brand
        except ValueError as e:
            print(f"{e}")


def create_category():
    while True:
        try:
            name = input("Digite o nome da categoria: ")

            if contains_digit(name):
                raise ValueError(not_number_in_place)

            if verify_categories(name):
                print("Essa categoria já está cadastrada")
                continue

            print(f"Você registrou a categoria {name}")
            categories_map.append(name)

            with open(categories_file, 'w', encoding='utf-8') as file:
                print("Salvando categorias")
                json.dump(categories_map, file, ensure_ascii=False)

            option = input("Deseja continuar criando (s/n): ")
            if option == "n":
                break
        except ValueError as e:
            print(f"{e}")


def remove_category():
    while True:
        print("Categorias Registradas")
        for cat in categories_map:
            print(f'- {cat}')

        search_cat = input("Digite o nome da categoria: ")
        if not verify_categories(search_cat):
            print("Não foi possivel encontrar essa categoria.")
            continue

        print(f'Você removeu categoria {search_cat}')
        categories_map.remove(search_cat)
        with open("categories.json", "w", encoding='utf=8') as file:
            print("Salvando categorias")
            json.dump(categories_map, file, ensure_ascii=False)

        option = input("Deseja continuar removendo (s/n): ")
        if option == "n":
            break


def request_category():
    while True:
        try:
            print("Categorias Registradas")
            for cat in categories_map:
                print(f'- {cat}')

            search_cat = input("Digite o nome da categoria: ")

            if contains_digit(search_cat):
                raise ValueError(not_number_in_place)

            if not verify_categories(search_cat):
                print("Não foi possivel encontrar essa categoria.")
                continue

            return search_cat
        except ValueError as e:
            print(f"{e}")


def create_product():
    brand = request_brand()
    categories = request_category()
    while True:
        try:

            product_name = input("Digite o nome do produto: ")

            color = input("Digite o cor do produto: ")
            if contains_digit(color):
                raise ValueError(not_number_in_place)

            price = int(input("Digite o valor do produto: "))

            product = {
                "brand": brand,
                "category": categories,
                "name": product_name,
                "color": color,
                "price": price
            }

            print(f'Você criou o produto com as seguintes infomações:',
                  "\n"
                  f"\nMarca: {brand}",
                  f"\nCategoria: {categories}",
                  f"\nNome: {product_name}",
                  f"\nCor: {color}",
                  f"\nValor: {price} \n")

            products_map.append(product)

            with open(products_file, 'w', encoding='utf-8') as file:
                json.dump(products_map, file, ensure_ascii=False)

            option = input("Deseja continuar removendo (s/n): ")
            if option == "n":
                break
        except ValueError as e:
            print(f"{e}")


def search_product():
    if len(brands_map) == 0:
        print("Falha na leitura: Não há marcas")
        return False

    if len(categories_map) == 0:
        print("Falha na leitura: Não há categorias")
        return False

    brand = request_brand()
    category = request_category()

    if len(products_map) == 0:
        print("Falha na leitura: Não há produtos")
        return False

    filter_list = []

    for product in products_map:
        if product['category'] == category and product['brand'] == brand:
            filter_list.append(product)

    size = len(filter_list)
    if size == 0:
        print("Não há produtos registrados com essa marca e categoria")
        return False

    print(f'Há {size} de produtos registrados com essa marca e categoria, Confira: \n')
    headers = ["Marca", "Categoria", "Nome", "Cor", "Preço"]
    rows = [[p["brand"], p["category"], p["name"], p["color"], p["price"]] for p in filter_list]
    print(tabulate(rows, headers=headers, tablefmt="pretty"))


def get_message():
    return str("|-| Menu de Operações |-|"
               "\n"
               "\n1 - Marca"
               "\n2 - Categoria"
               "\n3 - Produto"
               "\n\nSelecione sua opção: ")


def get_choice(message, valid_option):
    while True:
        put_choice = input(message)
        if put_choice in valid_option:
            return put_choice
        else:
            print("Opção inválida. Por favor, selecione novamente.")


while True:
    choice = get_choice(get_message(), ['0', '1', '2', '3'])
    if choice == '1':
        second_choice = get_choice("|-| Menu de Operações -> Marca |-|"
                                   "\n\n1 -> Registrar Marca"
                                   "\n2 -> Remover Marca"
                                   "\n3 -> Marcas Registradas"
                                   "\n\n0 -> Sair"
                                   "\n\nSelecione sua opção: "
                                   , ['0', '1', '2', '3'])

        if second_choice == '0':
            break
        elif second_choice == '1':
            create_brand()
        elif second_choice == '2':
            remove_brand()
        elif second_choice == '3':
            for brand in brands_map:
                print(f'- {brand}')
    elif choice == '2':
        second_choice = get_choice("|-| Menu de Operações -> Categorias |-|"
                                   "\n\n1 -> Registrar Categoria"
                                   "\n2 -> Remover Categoria"
                                   "\n3 -> Categoria Registradas"
                                   "\n\n0 -> Sair"
                                   "\n\nSelecione sua opção: "
                                   , ['0', '1', '2', '3'])

        if second_choice == '0':
            break
        elif second_choice == '1':
            create_category()
        elif second_choice == '2':
            remove_category()
        elif second_choice == '3':
            for categ in categories_map:
                print(f'- {categ}')
    elif choice == '3':
        second_choice = get_choice("|-| Menu de Operações -> Produto |-|"
                                   "\n\n1 -> Registrar Produto"
                                   "\n2 -> Atualizar Produto"
                                   "\n3 -> Remover Produto"
                                   "\n4 -> Produtos Registradas"
                                   "\n\n0 -> Sair"
                                   "\n\nSelecione sua opção: "
                                   , ['0', '1', '2', '3', '4'])

        if second_choice == '1':
            create_product()
        elif second_choice == "2":
            search_product()
        elif second_choice == '4':
            for product in products_map:
                print(f'- {product}')
