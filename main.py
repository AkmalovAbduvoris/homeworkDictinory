from googletrans import Translator
translator = Translator()
import json

class Dictionary:
    def __init__(self) -> None:
        self.file = "translate.json"

    def viewOldWords(self):
        try:
            with open(self.file, "r") as file:
                return json.load(file)
        except:
            return []

    def writeWord(self, data):
        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    def addText(self, uz,en):
        data = self.viewOldWords()
        newId = len(data) + 1
        newText = {"id": newId, "uz" : uz , "en" : en}
        data.append(newText)
        self.writeWord(data)

    def viewText(self):
        ok = self.viewOldWords()
        for item in ok:
            print(f"{item['id']}) {item['uz']} - {item['en']}")

    def sozOyini(self, num):
        if len(self.viewOldWords()) < num:
            print("So'z yetarli emas")
            return
        tori = 0
        xato = []
        
        for i in range(num):
            ok = self.viewOldWords()
            print(f"Uzbekchasini top: {ok[i]['en']}")
            ans = input("Javob: ")
            if ans.lower() == ok[i]['uz'].lower():
                print("To'ri")
                tori += 1
            else:
                print(f"Noto'ri. To'ri javob: {ok[i]['uz']}")
                xato.append(ok[i])
        print(f"Natija: {tori}/ {num}dan {(tori / num) * 100}% topilgan")

        if xato:
            print("Topomagan so'zlar")
            for i in xato:
                print(f"{i['uz']} - {i['en']}")

while True:
    print("1.So'z qo'shish\n2.So'zlarni ko'rish\n3.So'z o'yini\n4.Dasturni tugatish");
    num = int(input("Son kiriting: "))
    dct = Dictionary()
    if num == 1:
        word_count = int(input("Nechta so'z qoshmoqchisiz: "))
        for i in range(word_count):
            uzb = input("Uzbekcha so'z kiriting: ")
            eng = input("Ingilizcha so'z kiriting: ")
            if not eng:
                eng = translator.translate(uzb, src='uz', dest='en').text
            dct.addText(uzb, eng)
    elif num == 2:
        dct.viewText()
    elif num == 3:
        dct.sozOyini(int(input("Nechta so'zni topmoqchsiz: ")))
    elif num == 4:
        print("Dastur tugadi")
        break
    else:
        print("Bunday raqam mavjud emas")