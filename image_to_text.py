import cv2
import pytesseract
from time import sleep
from PIL import ImageGrab, Image
import numpy

pytesseract.pytesseract.tesseract_cmd = (
    "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
)
# sleep(5)
# pil_image = ImageGrab.grab()  # .convert('L')# this to convert color to black and white
# data = pil_image.load()


img = cv2.imread("image_to_text.png")
# pil_image = Image.open(‘Image.jpg’).convert(‘RGB')
# opencv_image = numpy.array(pil_image)
opencv_image = numpy.array(img)
img = opencv_image

# img = cv2.imread("D:\hello_world.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_boxes(img))

# detecting character
h_img, w_img, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    # print(b)
    b = b.split(" ")
    print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, h_img - y), (w, h_img - h), (0, 0, 255), 1)
    cv2.putText(
        img, b[0], (x, h_img - y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.7, (50, 255, 0), 1
    )

cv2.imshow("result", img)
cv2.imwrite("image_to_text.jpg", img)
cv2.waitKey(0)

