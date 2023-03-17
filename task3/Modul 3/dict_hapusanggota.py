# membuat dictionary baru
dict_saya= {1:1, 2:4, 3:9, 4:16, 5:25}

print(dict_saya.pop(3))

print(dict_saya.popitem())

print(dict_saya)

del dict_saya[2]

dict_saya.clear()

del dict_saya

#error karena dict_saya  sudah dihapus
#print dict_saya