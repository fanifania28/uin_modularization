nama = 'Fani Rohmiasih'
program = 'Perhitungan Periode dan Frekuensi Getaran'

print(f'Program {program} oleh {nama}')

def hitung_periode(getaran,waktu):
    periode = getaran / waktu
    print(f'Getaran = {getaran} kali dalam waktu = {waktu} sekon')
    print(f'sehingga periode = {periode} sekon')
    return periode
def hitung_frekuensi(satu,periode):
    frekuensi = satu / periode
    print(f'Pada periode = {periode} sekon maka frekuensinya = {frekuensi} Hz')
    return frekuensi

# getaran = 60
# waktu = 15
periode = hitung_periode(60, 15)
periode = hitung_periode(75, 20)
frekuensi = hitung_frekuensi(1, 4)
frekuensi = hitung_frekuensi(1, 3.75)