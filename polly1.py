class America:
    def capital(self):
        print("capita of americ is wasington dc")

    def curency(self):
        print("curency of amrica id dollar")

    def language(self):
        print("language of america is English")


class India:
    def capital(self):
        print("capital of india is Delhi")

    def curency(self):
        print("curency of india is rupees")

    def language(self):
        print("language of india is Hindi")

def func(obj):
    obj.capital()
    obj.curency()
    obj.language()

a=America()
i=India()

func(a)
func(i)