from PIL import Image
import glob, os
import tkinter.filedialog as fd

"""Изменяем размеры рисунков в выбранной папке и вставляем лейбл"""

size = 300, 300
count = 0
file_ext_images = ['.jpg', '.jpeg', '.png', '.ppm', '.gif', 'tif', '.bmp']

label_nf = fd.askopenfilename(initialdir = "./", title = "Открыть рисунок для лейбла",
                           filetypes = (("png files","*.png"), ("all files","*.*")))
if not label_nf:
    exit()

directory = fd.askdirectory(title="Открыть папку с картинками", initialdir="./")
if not directory:
    exit()

label = Image.open(label_nf)

for infile in glob.glob(directory + "/*.*"):
    file, ext = os.path.splitext(infile)
    if ext not in file_ext_images:
        continue

    with Image.open(infile) as im:
        im.thumbnail(size)
        im.paste(label, (5, 5))
        im.save(file + "_sm" + ".jpeg", "JPEG")
        count += 1

label.close()
print(f"Обработано {count} рисунка/ов.")

