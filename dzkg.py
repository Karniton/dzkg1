from colorthief import ColorThief
from PIL import Image
import os 


def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))


def sorted_by_red(path,path1):
        string_of_filenames = os.listdir(f"{path}")

        for i in string_of_filenames:

            pil_image = Image.open(f"{path}\\{i}")
            im_crop = crop_center(pil_image,200,200)
            im_crop.save(f"{path}\\(crop){i}")
            ct = ColorThief(f"{path}\\(crop){i}")
            dominant_color = ct.get_color(quality = 1)
            print(dominant_color,i)

            if dominant_color[0]>=50 and dominant_color[1] <= (dominant_color[0] // 2) and dominant_color[2] <= (dominant_color[0] // 2):
                print("the picture propably red")
                os.replace(f"{path}\\{i}", f"{path1}\\{i}")

            os.remove(f"{path}\\(crop){i}")
            
#"C:\\Users\\vipyu\\OneDrive\\Desktop\\folder1"
#"C:\\Users\\vipyu\\OneDrive\\Desktop\\folder2"
path_before = input("Введите путь к папке,которую нужно отсортировать:").replace("\\","\\\\")
path_after = input("Введите путь к папке,куда поместить отсортированные картинки:c").replace("\\","\\\\")

sorted_by_red(path_before,path_after)
    

