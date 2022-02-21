from product import product
from company import company
from pathlib import Path

# Loading products info
products = []
products_list_file = open(str(Path(__file__).resolve().parent) + "/products_list.txt", "r")

for p in products_list_file:
    p = p.replace("\n", "")
    p = p.split(",")

    products.append(product(p[0], float(p[1]), float(p[2])))

# Loading companies info
companies = []
companies_list_file = open(str(Path(__file__).resolve().parent) + "/companies_list.txt", "r")

for c in companies_list_file:
    c = c.replace("\n", "")
    c = c.split(",")

    if len(c) == 6:
        companies.append(company(c[0], float(c[1]), float(c[2]), float(c[3]), float(c[4]), float(c[5])))
    else:
        companies.append(company(c[0], float(c[1]), float(c[2])))

# Showing results
for p in products:
    print("Product info:")
    print("Name: {}".format(p.get_name()))
    print("Distance: {:.2f}".format(p.get_distance()))
    print("Weight: {:.2f}".format(p.get_weight()))
    print()
    print("Budgets:")
    
    for c in companies:
        print("{}: R$ {:.2f}".format(c.get_name(), c.calculate_budget(p)))
    
    print("---")