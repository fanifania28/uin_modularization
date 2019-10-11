nama = 'Fani Rohmiasih'
program = 'Gerak Lurus'

print(f'Program {program} oleh {nama}')

def hitung_kecepatan(jarak,waktu):
    kecepatan = jarak / waktu
    print(f'Jarak = {jarak / 1000}km ditempuh dalam waktu = {waktu / 60}menit')
    print(f'sehingga kecepatan = {kecepatan} m/s')
    return kecepatan

# jarak = 10000
# waktu = 50 * 60
kecepatan = hitung_kecepatan(1000, 5 * 60)
kecepatan = hitung_kecepatan(3000, 70 * 60)

