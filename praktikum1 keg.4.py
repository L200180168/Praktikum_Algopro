Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> nama = 'helmi asyam nuruddin'
>>> nim = 168
>>> tinggi = 1.66
>>> berat = 63
>>> tahunlahir = 1999
>>> aku = (tahunlahir, berat, tinggi, nim, nama)
>>> data = [tahunlahir, berat, tinggi, nim, nama]
>>> type(aku)
<type 'tuple'>
>>> #artinya aku adalah tuple atau deretan objek
>>> aku[0]
1999
>>> #data ke-0 dalam tuple aku adalah 1999
>>> a = nim % 4; aku[a]
1999
>>> #hasil pembagian Nim dibagi 4 tersisa 0, jadi yang ditampilkan adalah tahun lahir
>>> type(aku[a])
<type 'int'>
>>> #data yang ditampilkan adalah integer atau bilangan bulat
>>> aku[a:4]
(1999, 63, 1.66, 168)
>>> #data dari a adalah 1999, 63, 1.66, 168
>>> type(aku[4])
<type 'str'>
>>> #data ke-4 dalam aku merupakan string
>>> aku[0] = 'ok'

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    aku[0] = 'ok'
TypeError: 'tuple' object does not support item assignment
>>> type(data)
<type 'list'>
>>> #jenis data merupakan list
>>> type(data[4])
<type 'str'>
>>> #data ke-4 adalah string
>>> data[4][5]
' '
>>> #karena pada elemen list data, indeks 5 tidak ada dan hanya sampai indeks 4
>>> data[4][a:6]
'helmi '
>>> #dalam data ke 4 slicing ke a-6 adalah helmi
>>> data [0] = 'ok';data
['ok', 63, 1.66, 168, 'helmi asyam nuruddin']
>>> #data ke-0 diganti string ok
>>> data[-a]
'ok'
>>> #hasil data[-a] adalah ok
>>> range(a)
[]
>>> #karena pembagian Nim dibagi 4 tersisa 0, maka hasil range dari data a tidak ada
