import cv2


def video():
    cap = cv2.VideoCapture(0+cv2.CAP_DSHOW)
    while (True):
        ret, frame = cap.read()
        cv2.imshow('image',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(ret)
    if ret==True:
        cv2.imshow('image',frame)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
    return print('taken a picture')
