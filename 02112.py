#6
store = {"молоко": 20, "сыр": 15}
store2 = {"мороженое": 40, "сыр": 20, "яблоко": 40}
out = {}

for i in store.keys() | store2.keys():
    out[i] = store.get(i, 0) + store2.get(i, 0)

print(out)