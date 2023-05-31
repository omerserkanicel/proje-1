sozluk = {"kanki": "sevdiğin kişiye sesleniş şekli","denyo": "MALL!!!","manita": "sevgili",
        "bug": "oyun hatası"}
        
        
secim = input("Kanki,Denyo,Manita,Bug bunlardan hangisinin anlamını öğrenmek istersin:")
if secim in sozluk:
    print(sozluk[secim])
else:
    print("sözlükte böyle bir kelime yok")
