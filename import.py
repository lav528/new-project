from sys import argv

script, filename = argv

txt = open(filename)

print(f"Содержание файла {filename}:")
print(txt.read())

print("Снова введите имя файла: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
