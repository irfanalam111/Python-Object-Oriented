count_ = {'IN': "india", 'US': "united state", 'AU': "austrliya", 'CA': "canada"}


def show_menu():
    print("select an option")
    print("view:view country")
    print("add:Add a country")
    print("del:delete a country")
    print("exit:Exit the program")
    print()

    def show_code(country):
        print(count_)

    def add_country(countries):
        count_ = {'IN': "india", 'US': "united state", 'AU': "austrliya", 'CA': "canada"}
        i = 1
        while i <= 2:
            name = input("enter country key")
            key_ = input("enter country name")
            count_[key_] = name
            i = i + 1
            print(count_)
