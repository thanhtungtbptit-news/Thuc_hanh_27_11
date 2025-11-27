data = [
    ("A01", 5),
    ("B02", 3),
    ("A01", 2),
    ("C03", 7),
    ("B02", 4)
]
tong_sku = {}
for sku, quantity in data:
    if sku in tong_sku:
        tong_sku[sku] += quantity
    else:
        tong_sku[sku] = quantity
result = list(tong_sku.items())
print(result)
