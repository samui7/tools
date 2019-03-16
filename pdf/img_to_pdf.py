# python img_to_pdf.py imgpath1 imgpath2 ... for up to 10 image files

from PIL import Image
import sys

def to_pdf(path_list):
    
    page1 = Image.open(path_list[0])
    img_list = []
    if len(path_list) > 1:
        for path in path_list[1:]:
            img_list.append(Image.open(path))
    
    out_name = path_list[0] + '_converted.pdf'
    
    page1.save(out_name, "PDF", resolution = 100.0, save_all=True, append_images=img_list)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Specify at least 1 image path")
        exit()
    if len(sys.argv) > 11:
    	print("Too many images")
    	exit()
    path_list = sys.argv[1:]
    to_pdf(path_list)