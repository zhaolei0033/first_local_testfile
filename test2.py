print("type which file you want open :" )

filename = input(">>>")

txt = open(filename)

print(txt.read())

txt.close()
