import cv2


def main():
    img = cv2.imread('Resources/elonMusk.jpg')
    img = cv2.resize(img, (740, 480))

    cv2.imshow('Img', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
