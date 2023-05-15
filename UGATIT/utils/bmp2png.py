import os
import cv2
def bmp2png(read_path,save_path):
    list_r = os.listdir(read_path)
    for i in list_r:
        read_root=os.path.join(read_path,i)
        mask=cv2.imread(read_root,0)
        save_filename=os.path.splitext(i)[0]+'.png'
        save_p=os.path.join(save_path,save_filename)
        print(save_p)
        cv2.imwrite(save_p,mask)


if __name__=='__main__':
    read_path=r'E:\jiangshan\U-net\UGATIT\dataset\masksTokq6\trainA'
    save_path=r"E:\jiangshan\U-net\UGATIT\dataset\masksTokq6\t"
    bmp2png(read_path,save_path)


