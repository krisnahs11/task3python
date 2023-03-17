tuple1=(2,3,4,[5,6])
# kita tidak bisa mengubah anggota tuple
# bila kita hilangkan tanda komentar #pada baris ke 6
# akan muncul error: # typeError: 'tuple' object does not support item assignment
 
#tuple[1]= 8

# tapi list didalam tuple bisa diubah
# output; (2,3,4,[7,6])
tuple1[3][0]= 7
print(tuple1)

# tuple bisa diganti secara keseluruhan dengan penugasan kembali
tuple1= ('p','y','t','h','o','n')
print(tuple1)

# anggota tuple juga tidak bisa dihapus menggunakan del
# perintah berikut akan menghasilkan error TypeError
# kalau anda menghilangkan tanda komentar #

#del tuple[0]
# kita bisa menghapus tuple keseluruhan
del tuple1