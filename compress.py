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

def histogram_BGR(BGR_image):
    blue_list = []
    green_list = []
    red_list = []
    gray_list = []

    for i in range(256):
        blue_list.append(0)
        green_list.append(0)
        red_list.append(0)
        gray_list.append(0)

    for row in BGR_image:
        for pixel in row:
            
            blue_list[int(pixel[0])] += 1
            green_list[int(pixel[1])] += 1
            red_list[int(pixel[2])] += 1
            gray_list[int((int(pixel[0]) + int(pixel[1]) + int(pixel[2]))/3)] += 1

    return blue_list, green_list, red_list, gray_list   

def unique_values(BGR_image):
    blue = []
    green = []
    red = []
    gray = []

    for row in BGR_image:
        for pixel in row:
            if pixel[0] not in blue:
                blue.append(pixel[0])
            if pixel[1] not in green:
                green.append(pixel[1])
            if pixel[2] not in red:
                red.append(pixel[2])
            if int( (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3) not in gray:
                gray.append(int( (int(pixel[0]) + int(pixel[1]) + int(pixel[2])) / 3))
    return blue, green, red, gray

if __name__ == '__main__':
    image_location='cat.png' 
    image1 = '25.jpg'
    image2 = '50.jpg'
    image3 = '75.jpg'

    img = cv2.imread(image_location, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image_location} - original', img) 

    img1 = cv2.imread(image1, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image1} - original', img) 

    img2 = cv2.imread(image2, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image2} - original', img) 

    img3 = cv2.imread(image3, cv2.IMREAD_COLOR) #Blue, Green, Red
    cv2.imshow(f'{image3} - original', img) 

    images = [img, img1, img2, img3]
   
    print(f'Pixel Count: {pixel_count(img)}')

    x = []
    for i in range(256):
        x.append(i)

    gray_histos = []

    for i in range(4):
        blue_hist  = histogram_BGR(images[i])[0]
        green_hist  = histogram_BGR(images[i])[1]
        red_hist = histogram_BGR(images[i])[2]
        gray_hist = histogram_BGR(images[i])[3]

        gray_histos.append(gray_hist)

        plt.plot(x, red_hist, label = "red", color='red')
        plt.plot(x, green_hist, label = "green", color='green')
        plt.plot(x, blue_hist, label = "blue", color='blue')
        plt.plot(x, gray_hist, label = "gray", color='gray')

        plt.title(f'{i} - Color Histogram Line Chart', loc='center')
        plt.legend()
        plt.show()  # display

    for i in range(len(gray_histos)):
        plt.plot(x, gray_histos[i], color=(1/((i+1) * 3), 1/((i+1) * 3), 1/((i+1) * 3)))
        plt.legend()
    plt.title("Luminosity Histogram Line Chart", loc='center')
    plt.show()

    for image in images:
        blue = unique_values(image)[0]
        green = unique_values(image)[1]
        red = unique_values(image)[2]
        gray = unique_values(image)[3]

        plt.bar(x, blue,  color="blue")
        plt.bar(x, green, color="blue")
        plt.bar(x, red, color="blue")
        plt.bar(x, gray, color="blue")
    plt.title("Unique Values Bar Chart", loc='center')
    plt.show()
    
    cv2.waitKey() 
    cv2.destroyAllWindows() 
