import random
import time

def time_print(text, delay=0.001):
    for harf in text:
        print(harf, end='', flush=True)
        time.sleep(delay)

a1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
a2 = '0123456789'
PUNCTUATION = str('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~')

ZOR = a1 + a2 + PUNCTUATION + "ğüşıçöĞÜŞİÇÖ"
ORTA = a1 + a2 + "ğüşıçöĞÜŞİÇÖ"
KOLAY = a1 + a2
ÇOK_KOLAY = a1
TAVSİYE_EDİLMEYEN = "1234567890qwertyuıopğüasdfghjklşizxcvbnmöç"
İMKANSIZ = ZOR + "π∞Σ√∛∜∫∬∭∮∯∰∱∲∳∀∁∂∃∄∅∆∇∈∉∊∋∌∍∎∏∐∑∓≅≆≇≈≉≊≋≌≍≎≏≐≑≒≓≔≕≖≗≘≙≚≛≜≝≞≟≠≡≢≣≤≥≦≧≨≩≪≫≬≭≮≯≰≱≲≳≴≵≶≷≸≹≺≻≼≽≾≿⊀⊁⊂⊃⊄⊅⊆⊇⊈⊉⊊⊋⊌⊍⊎⊏⊐⊑⊒⊓⊔⊕⊖⊗⊘⊙⊚⊛⊜⊝⊞⊟⊠⊡⊢⊣⊤⊥⊦⊧⊨⊩⊪⊫⊬⊭⊮⊯⊰⊱⊲⊳⊴⊵⊶⊷⊸⊹⊺⊻⊼⊽⊾⊿⋀⋁⋂⋃⋄⋅⋆⋇⋈⋉⋊⋋⋌⋍⋎⋏⋐⋑⋒⋓⋔⋕⋖⋗⋘⋙⋚⋛⋜⋝⋞⋟⋠⋡⋢⋣⋤⋥⋦⋧⋨⋩⋪⋫⋬⋭⋮⋯⋰⋱⁺⁻⁼⁽⁾ⁿ₊₋₌₍₎♪♫♩♬♭♮♯¢$€£¥₮৲৳௹฿៛₠₡₢₣₤₥₦₧s₨₩₪₫₭₯₰₱₲₳₴₵￥﷼¤ƒ₺♙♖♘♗♔♕♟♜♞♝♚♛♡♥♢♦♤♠♧♣¹²³⁴⁵⁶⁷⁸⁹⁰Æ"

def guvenli_sifre_olustur(zorluk_seti, uzunluk):
    sifre = ""
    
    for _ in range(uzunluk):
        karakter_index = random.randint(0, len(zorluk_seti) - 1)
        yeni_karakter = zorluk_seti[karakter_index]
        
        sifre = sifre + yeni_karakter

def ana_program():
    time_print("Welcome to the Password Generator Program!\n")
    
    while True:
        try:
            time_print("How many digits should the password have? (8-256): ")
            uzunluk = int(input())
            
            if uzunluk < 8 or uzunluk > 256:
                time_print("Please enter a number between 8 and 256!\n")
                continue
                
            time_print("Choose difficulty level:\n")
            time_print("1. Very Strong (Impossible)\n")
            time_print("2. Strong (Hard)\n")
            time_print("3. Medium\n")
            time_print("4. Easy\n")
            time_print("5. Very Easy\n")
            time_print("6. Not Recommended\n")
            time_print("Your choice (1-6): ")
            zorluk = input()
            
            zorluk_setleri = {
                '1': İMKANSIZ,
                '2': ZOR,
                '3': ORTA,
                '4': KOLAY,
                '5': ÇOK_KOLAY,
                '6': TAVSİYE_EDİLMEYEN
            }
            
            if zorluk not in ['1', '2', '3', '4', '5', '6']:
                time_print("\nInvalid selection! Please enter a number between 1 and 6.\n")
                continue
                
            secilen_set = zorluk_setleri[zorluk]
            
            time_print("\nYour password is being created")
            for _ in range(3):
                print('.', end='', flush=True)
                time.sleep(0.3)
            print()
            
            # Güvenli şifre oluşturma
            sifre = guvenli_sifre_olustur(secilen_set, uzunluk)
            
            time_print("\n╔═══════════════════════════════════════════════════════════════════════════╗")
            time_print("\n║   CREATED PASSWORD:                                                       ║")
            time_print(f"\n║   {sifre}   ║")
            time_print("\n╚═══════════════════════════════════════════════════════════════════════════╝\n")
            
            time_print("\nDon't forget to copy this password!\n")
            
            time_print("To create a new password, press 'E', to exit press 'H': ")
            tekrar = input().strip().lower()
            
            if tekrar != 'e':
                time_print("\nThe program is ending. Have a nice day!")
                time.sleep(1)
                break
                
            print("\n" + "="*50 + "\n")
                
        except ValueError:
            time_print("\nError: Please enter a valid number!\n")
        except Exception as e:
            time_print(f"\nAn unexpected error occurred: {str(e)}\n")

if __name__ == "__main__":
    ana_program()
