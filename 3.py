class Entry:
    def login(self):
        form = input("Введіть пароль: ")
        if form == 'Aquatika': print("Привіт :D")
        elif form == 'підказка': print("Прив")
        else: 
            print("Пароль невірний")  
            Entry.login(self)
E = Entry()
E.login()

class Work:
    def create(self):
        f = open('text.txt', 'w')
        f.close()
    def wrt(self):
        f = open('text.txt', 'w+')
        f.write(input("Запишіть в файл щось: "))
        f.close()
    def rd(self):
        f = open('text.txt', 'r')
        print(f.read())
        f.close()
W = Work()
W.create()
W.wrt()
W.rd()

#Василь Васильович Гриньків, група КІПЗс-2017
