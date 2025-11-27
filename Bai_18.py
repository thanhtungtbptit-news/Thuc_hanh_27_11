data = [
    ("A", 5),
    ("B", 3),
    ("A", 2),
    ("C", 7),
    ("B", 4)
]
tong_sku = {}
for sku, quantity in data:
    if sku in tong_sku:
        tong_sku[sku] += quantity
    else:
        tong_sku[sku] = quantity
result = list(tong_sku.items())
print(result)
