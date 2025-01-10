import copy
def printing_adjusted(list):
    for index, price in enumerate(list):
        print(f"{index + 1}: {price['nome']} = \033[92m{price['preco']:.2f}\033[m")   

    return "-"*30
    
def increase_prices_by_10_percent(list_product):
    deep_copy_with_news_products = copy.deepcopy(list_product)

    for index, price in enumerate(deep_copy_with_news_products):

        increase_10_porcentage = (price['preco'] * 0.1) + price['preco']
        deep_copy_with_news_products[index]['preco'] = increase_10_porcentage
    
    return printing_adjusted(deep_copy_with_news_products)



def sort_products_by_name(list_product):
    deep_copy_products_ordenation_by_name = copy.deepcopy(list_product)
    ordenation_name = sorted(
    deep_copy_products_ordenation_by_name, key=lambda item: item['nome'], reverse=True)


    return printing_adjusted(ordenation_name)


def sort_products_by_price(list_product):
    deep_copy_products_ordenation_by_price = copy.deepcopy(list_product)

    deep_copy_products_ordenation_by_price.sort(key=lambda item: item['preco'], reverse=False)
    
    return printing_adjusted(deep_copy_products_ordenation_by_price)

