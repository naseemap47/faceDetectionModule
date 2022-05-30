import cv2


def findObjects(img, cascade, scaleFactor=1.1, minNeighbors=4):
    img_copy = img.copy()
    img_gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    objects = cascade.detectMultiScale(img_gray, scaleFactor=scaleFactor, minNeighbors=minNeighbors)
    for (x, y, w, h) in objects:
        cv2.rectangle(img_copy, (x, y), (x + w, y + h), (255, 0, 255), 2)
    return img_copy, objects


def main():
    img = cv2.imread('Resources/elonMusk.jpg')
    img = cv2.resize(img, (740, 480))
    faceCascade = cv2.CascadeClassifier('Resources/haarcascade_frontalface_default.xml')
    img_obj, objects = findObjects(img, faceCascade)

    cv2.imshow('Img', img_obj)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
