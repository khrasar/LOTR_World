races = [ "İnsan", "Elf", "Cüce", "Hobbit", "Balrog", "Büyücü", "Ork", "Ejderha", "Troll"]
characters = []

# Karakterlerin tanımlandığı ve özelliklerinin eklendiği sınıf
class character():
    def __init__(self,isim,sınıf,cinsiyet,yas,irk):
        self.isim = isim
        self.sınıf = sınıf
        self.cinsiyet = cinsiyet
        self.yas = yas
        self.irk = irk
        
    def addNewChar(self,newChar):
        characters.append(newChar)
        print("Yeni karakter eklendi.")
        
    def showAllChars(self):
        for i in characters:
          print(i.isim)
##########################################################
class insan(character):
    def __init__(self,isim,sınıf,cinsiyet,yas):
        super().__init__(isim,sınıf,cinsiyet,yas,"İnsan")
class elf(character):
    def __init__(self,isim,sınıf,cinsiyet,yas):
        super().__init__(isim,sınıf,cinsiyet,yas,"Elf")
class cüce(character):
    def __init__(self,isim,sınıf,cinsiyet,yas):
        super().__init__(isim,sınıf,cinsiyet,yas,"Cüce")
class hobbit(character):
    def __init__(self,isim,sınıf,cinsiyet,yas):
        super().__init__(isim,sınıf,cinsiyet,yas,"Hobbit")
        
class balrog(character):
    def __init__(self,isim,sınıf,cinsiyet,yas):
        super().__init__(isim,sınıf,cinsiyet,yas,"Balrog")
    def SelfGucEkle(self, yeni_guc):
        self.guc = yeni_guc
    def SelfGuc(self):
        return self.guc
    
class büyücü(character):
    def __init__(self,isim,sınıf,cinsiyet,yas):
        super().__init__(isim,sınıf,cinsiyet,yas,"Büyücü")
    def SelfGucEkle(self, yeni_guc):
        self.guc = yeni_guc
    def SelfGuc(self):
        return self.guc
    
class ork(character):
    def __init__(self,isim,sınıf,cinsiyet,yas):
        super().__init__(isim,sınıf,cinsiyet,yas,"Ork")
class ejderha(character):
    def __init__(self,isim,sınıf,cinsiyet,yas):
        super().__init__(isim,sınıf,cinsiyet,yas,"Ejderha")
class troll(character):
    def __init__(self,isim,sınıf,cinsiyet,yas):
        super().__init__(isim,sınıf,cinsiyet,yas,"Troll")
############################################################

def showCharacterAttributes(character):
        print(vars(character))

aragorn = insan("Aragorn,son of Arathorn", "Savaşçı", "Erkek", 87)
aragorn.addNewChar(aragorn)


print("Merhabalar, Yüzüklerin Efendisi tabanlı karakter oluşturma uygulamasına girdiniz\n")
print()
print("Karakter yaratmak için girmeniz gerekenler: isim, ırk, sınıf, cinsiyet, yaş\n")
print("Karakterlerinize temel özellikler yanında yeni özellik eklemek isterseniz göstergeleri takip edin.")

print("Örnek olarak oluşturduğumuz karakterin özelliklerini aşağıda görebilirsiniz\n")
showCharacterAttributes(aragorn)
while True:
    isim1 = str(input("Karekter ismi:"))
    sınıf1 = str(input("Karakter sınıfı:"))
    cinsiyet1 = str(input("Karakter cinsiyeti:"))
    print("Girdiğiniz değer tam sayı olmalıdır, lütfen harf veya küsüratlı sayı kullanmayınız\n")
    yas1 = int(input("Karakter yaşı:"))
    print("İstediğiniz ırkı seçebelir veya karakterinize LOTR dünyasından yeni bir ırk verebilirsiniz\n")
    print(races)
    irk1 = input("Karakter ırkı:(lütfen seçiminizde bütün harfleri küçük yazınız.)\n")
    if irk1 == "insan":
        newChar = insan(isim1,sınıf1,cinsiyet1,yas1)
    elif irk1 == "elf":
        newChar = elf(isim1,sınıf1,cinsiyet1,yas1)
    elif irk1 == "cüce":
        newChar = cüce(isim1,sınıf1,cinsiyet1,yas1)
    elif irk1 == "hobbit":
        newChar = hobbit(isim1,sınıf1,cinsiyet1,yas1)
    elif irk1 == "balrog":
        newChar = balrog(isim1,sınıf1,cinsiyet1,yas1)
        print("Doğaları gereği Barloglar ve Büyücüler değişimle yeni güçler kazanabilir")
        print("Eklemek istediğiniz gücü yazabilirsiniz ya da güç vermeden devam etmek için ok yazabilirsiniz\n")
        guc1 = input()
        newChar.SelfGucEkle(guc1)
        newChar.SelfGuc
            
    elif irk1 == "büyücü":
        newChar = büyücü(isim1,sınıf1,cinsiyet1,yas1)
        print("Doğaları gereği Barloglar ve Büyücüler değişimle yeni güçler kazanabilir")
        print("Eklemek istediğiniz gücü yazabilirsiniz ya da güç vermeden devam etmek için ok yazabilirsiniz\n")
        guc1 = input()
        newChar.SelfGucEkle(guc1)
        newChar.SelfGuc
        
    elif irk1 == "ork":
        newChar = ork(isim1,sınıf1,cinsiyet1,yas1)
    elif irk1 == "ejderha":
        newChar = ejderha(isim1,sınıf1,cinsiyet1,yas1)
    elif irk1 == "troll":
        newChar = troll(isim1,sınıf1,cinsiyet1,yas1)
    print("Yeni eklenen karakterin özellikleri\n")
    showCharacterAttributes(newChar)
    print()
    newChar.addNewChar(newChar)
    print("Bütün kayıtlı karakterler:\n")
    newChar.showAllChars()
    print()
    print("Daha fazla karakter eklemek istiyorsanız y istemiyorsanız n yazabilirsiniz")
    ans = input("Cevap:")
    if ans == "n":
        break
