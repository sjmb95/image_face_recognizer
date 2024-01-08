import cv2
import dlib
import face_recognition




imgPath = input('image path:')
img = cv2.imread(imgPath)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_encoded = face_recognition.face_encodings(img_rgb)[0]

imgPath2 = input('comparing image path :')
img2 = cv2.imread(imgPath2)

img2_rgb = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
img2_encoding = face_recognition.face_encodings(img2_rgb)[0]

result = face_recognition.compare_faces([img_encoded], img2_encoding)


print(result)





















