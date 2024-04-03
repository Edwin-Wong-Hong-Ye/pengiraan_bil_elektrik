#ATUR CARA MENGIRA JUMLAH BIL ELEKTRIK

#proses input
penggunaan_elektrik=int(input('Sila masukkan elektirik yang anda gunakan bulan ini(kWj):'))

#proses menentukan kadar tarif
if penggunaan_elektrik<=200:
    kadar_tarif=0.218
elif penggunaan_elektrik<=300:
    kadar_tarif=0.334
elif penggunaan_elektrik<=600:
    kadar_tarif=0.516
elif penggunaan_elektrik<=900:
    kadar_tarif=0.546
else:
    print('Tidak mdapat kira.')

#proses mengira bil elektrik
bil_elektrik=penggunaan_elektrik*kadar_tarif

#proses output
print('Bil elektrik anda ialah RM',bil_elektrik,'.')
