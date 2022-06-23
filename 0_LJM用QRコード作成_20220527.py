import openpyxl
import qrcode
import os
from openpyxl.drawing.image import Image
import glob

base_f = "base.xlsx"
save_f = "to.xlsx"


book = openpyxl.load_workbook(base_f)
sheet = book.active

rows = sheet["A1:B999"]

i = 1
for row in rows:
          values = [cell.value for cell in row]
          if values[0] is None: break
          img_base = qrcode.make(row[0].value)
          aa ="aa"+str(i)+".png"
          
          img_base.save(aa)
          img = openpyxl.drawing.image.Image(aa)

          img.width = 100
          img.height =100
          print(row[0].value)
          print(img)
          print(aa)
          zz = "B" + str(i)
          i = i + 5
          sheet.add_image(img, zz)
book.save(save_f)

for file in glob.glob("aa*.png"):
    os.remove(file)

print("QRｺｰﾄﾞ作成完了しました。")

