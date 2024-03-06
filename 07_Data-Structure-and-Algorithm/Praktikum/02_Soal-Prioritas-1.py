
#NO 2 Soal Prioritas 1

def get_breads(breads, flour_stock):
    breads_stock = []
    total_flour = flour_stock
    breads.sort(key=lambda x: x["flour"])

    for bread in breads:
        if bread["flour"] <= total_flour:
            breads_stock.append(bread["name"])
            total_flour -= bread["flour"]

    return breads_stock

bread1 = [
    {"name": "donut", "flour": 25},
    {"name": "mini puff", "flour": 15},
    {"name": "baguette", "flour": 75},
    {"name": "cupcake", "flour": 15},
]

bread2 = [
    {"name": "pancake", "flour": 15},
    {"name": "waffle", "flour": 25},
    {"name": "bagel", "flour": 15},
    {"name": "cupcake", "flour": 15},
    {"name": "choco chips", "flour": 10},
    {"name": "mini puff", "flour": 5},
    {"name": "bread", "flour": 30},
]

print(get_breads(bread1, 100))
# ['mini puff', 'cupcake', 'donut']

print(get_breads(bread2, 75))
#['mini puff', 'choco chips', 'pancake', 'bagel', 'cupcake']