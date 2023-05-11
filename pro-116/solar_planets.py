import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun",
            (100,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.8,
            (255,215,7)
            )

cv2.putText(img,
            "Mercury",
            (120,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (7,255,28)
            )

cv2.putText(img,
            "Venus",
            (190,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (7,255,28)
            )

cv2.putText(img,
            "Earth",
            (295,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (7,255,28)
            )

cv2.putText(img,
            "Mars",
            (385,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (7,255,28)
            )

cv2.putText(img,
            "Jupiter",
            (435,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (7,255,28)
            )

cv2.putText(img,
            "Saturn",
            (700,125),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (7,255,28)
            )

cv2.putText(img,
            "Uranus",
            (950,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (7,255,28)
            )

cv2.putText(img,
            "Neptune",
            (1115,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.4,
            (7,255,28)
            )

cv2.imshow("solar-system",img)
cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg",img)











