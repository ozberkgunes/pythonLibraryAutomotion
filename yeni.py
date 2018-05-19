kitaplar = list()

def bookAdd(author,bookName):

    kitaplar.append((author,bookName))
    print("kitap eklendi")
def bookRemove(book):
    kitaplar.remove(kitap)
    print("kitap Çıkarıldı")

    def listele():
        for i in kitaplar:
            print(i)

while  True:
    print("""
1- kitap ekler
2- kitap cıkartır
3- kitap listele
4-exit
        """)
    secim = input("Secim")
    if secim =="1":
        k_adi=input("Kitap Adi ")
        y_adi=input("yazar Adi")
        bookAdd(y_adi,k_adi)
    if secim=="2":
        k_adi= input ("Kitap Adi")
        y_adi= input ("yazar adi")
        bookRemove((k_adi,y_adi))
    if secim=="3":
        for i in kitaplar:
            print("yazar: ", i[0],"      Kitap : " , i[1])
