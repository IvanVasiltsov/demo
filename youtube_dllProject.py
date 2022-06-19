from openpyxl import workbook
from openpyxl import load_workbook

try:
    with open("out.txt", 'w', encoding="utf-8") as file:
        file.write("test text")

except:
    print("file not found")
finally:
    print("работа с файлом завершена")