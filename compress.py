import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('cat.png')

cv2.imwrite('lossless_compressed_image.png', img)

cv2.imwrite('25.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 25])
cv2.imwrite('50.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 50])
cv2.imwrite('75.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 75])

def pixel_count(BGR_image: list)-> int:
    height = len(BGR_image)
    width = len(BGR_image[0])
    return height*width

def histogram_BGR(BGR_image:list)->list:
    blue_list = []
    green_list = []
    red_list = []
    for i in range(0,256):
        blue_list.append(0)
        green_list.append(0)
        red_list.append(0)
    for row in BGR_image:
        for pixel in row:
            blue_list[pixel[0]] += 1
            green_list[pixel[1]] += 1
            red_list[pixel[2]] += 1
    return blue_list, green_list, red_list            

if __name__ == '__main__':
    image_location='cat.png' 
    image1 = '25.jpg'
    image2 = '50.jpg'
    image3 = '75.jpg'

    img = cv2.imread(image_location, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image_location} - original', img) 

    img = cv2.imread(image1, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image1} - original', img) 
    img = cv2.imread(image2, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image2} - original', img) 
    img = cv2.imread(image3, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image3} - original', img) 
   
    print(f'Pixel Count: {pixel_count(img)}')

    blue_hist, green_hist, red_hist = histogram_BGR(img)

    x = range(256)
    ry=(histogram_BGR(img[2]))
    plt.plot(x,ry, label = "red", color='red')

    gy=(histogram_BGR(img[1]))
    plt.plot(x, gy, label = "green", color='green')

    by=(histogram_BGR(img[0]))
    plt.plot(x, by, label = "blue", color='blue')
    
    plt.title("Luminosity -Frequency Analysis", loc='center')
    plt.legend()
    plt.show()  # display
    
    cv2.waitKey() 
    cv2.destroyAllWindows() 
