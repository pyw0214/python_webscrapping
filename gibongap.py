# def profile(name, age, main_lang):
#    print("name: {0}\t age: {1}\t main_language: {2}"
#         .format(name, age, main_lang))


#profile("Yongwook Park", 20, "Python")
#profile("Jieun Park", 24, "JAVA")


# Same school, Same class, Sale Group

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name : {0}\t age: {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)


def profile(name, age, *language):
    print("name : {0}\t age: {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("Yongwook Park", 20, "Python", "Java", "C", "C++", "C#", "JaveScript")
profile("Jieun Park", 24, "Kotlin", "Swift")
