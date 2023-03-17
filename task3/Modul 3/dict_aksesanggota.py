dict_saya= {'nama':'budi', 'usia':27}

print(dict_saya['nama'])

print(dict_saya.get('usia'))

print(dict_saya.get('alamat'))

# mengakses kunci yang tidak tersedia menyebabkan Key Error
# dict_saya['alamat'] 