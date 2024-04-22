def toplama(x, y):
    return x + y

def cikartma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    if y == 0:
        return "Sıfıra bölme hatası!"
    else:
        return x / y

print("İşlem Seçenekleri")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

secim = input("İşlemi seçiniz (1/2/3/4): ") #İşlem seçimi

num1 = float(input("Birinci sayıyı giriniz: "))#1. sayı seçimi
num2 = float(input("İkinci sayıyı giriniz: "))#2. sayı seçimi

if secim == '1':
    print(num1, "+", num2, "=", toplama(num1, num2))#toplama

elif secim == '2':
    print(num1, "-", num2, "=", cikartma(num1, num2))#çıkarma

elif secim == '3':
    print(num1, "*", num2, "=", carpma(num1, num2))#çarpma

elif secim == '4':
    print(num1, "/", num2, "=", bolme(num1, num2))#bölme

else:
    print("Geçersiz işlem seçimi!")#geçersiz işlem