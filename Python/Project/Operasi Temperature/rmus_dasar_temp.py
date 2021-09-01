# Lat. Operasi Temperatur Suhu

print("\nPENGUBAH TEMPERTURE SUHU\n")

# Konversi Celcius ke Suhu lain
C = float(input("Masukkan Jumlah Celcius Anda :"))
print("Hasil ke Celcius =",C,"C")

# Pada Suhu Lain

R = (4/5)*C
print("Hasil ke Reamur =",R,"R")

F = ((9/5)*C)+32
print("Hasil ke Fahrenheit =",F,"F")

K = C+273
print("Hasil ke Kelvin =",K,"K")

# Konversi Reamur

R = float(input("Masukkan Jumlah Reamur Anda :"))
C = (5/4)*R
print("Hasil ke Celcius =",C,"C")

R = R
print("Hasil ke Reamur =",R,"R")

F = ((9/4)*R)+32
print("Hasil ke Fahrenheit =",F,"F")

K = ((5/4)*R)+273
print("Hasil ke Kelvin =",K,"K")

# Konversi Fahrenheit

F = float(input("Masukkan Jumlah Fahrenheit Anda :"))
C = (5/9)*(F-32)
print("Hasil ke Celcius =",C,"C")

R = (4/9)*(F-32)
print("Hasil ke Reamur =",R,"R")

F = F
print("Hasil ke Fahrenheit =",F,"F")

# Konversi Kelvin

K = float(input("Masukkan Jumlah Kelvin Anda :"))
C = K-273
print("Hasil ke Celcius =",C,"C")

R = (4/5)*(K-273)
print("Hasil ke Reamur =",R,"R")

K = K
print("Hasil ke Kelvin =",K,"K")