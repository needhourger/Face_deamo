#-*- coding=utf-8 -*-
import requests
import cv2
import json
import os

api_key="4sLjHdOfyyawO4ldcy-2ZdKn1g8rX2zJ"
api_secret="BZ-mqmWJ_YrqLYXKSiX4lhDPdilVcx21"
compare_url="https://api-cn.faceplusplus.com/facepp/v3/compare"
payload={"api_key":api_key,"api_secret":api_secret}

def print_dict(dictionary):
    for key,value in dictionary.items():
        if isinstance(value,dict):
            print_dict(value)
        elif isinstance(value,list):
            for i in value:
                print(key+":")
                print_dict(i)
            print("\n")
        else:
            print("{key}:{value}".format(key=key,value=value))


def cap_image():
    print("[INFO] Opening camera...")
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        if ret:
            #print("[INFO] Opening camera...")
            img=cv2.flip(frame,1,dst=None)
            cv2.imshow("Camera",img)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                cv2.imwrite("./temp.jpg",img)
                cap.release()
                cv2.destroyAllWindows()
                return True
        else:
            print("[ERRO] Error capture...")
    cap.release()
    cv2.destroyAllWindows()
    return False

def recognize():
    if not(os.path.exists("./base.jpg")):
        input("[WARN] Please register first...")
        register()

    if cap_image():
        print("[INFO] Image capture...")
    else:
        print("[WARN] No image capture")
        input("press any key to continue...")
        return

    files={ "image_file1":open("./base.jpg","rb"),
            "image_file2":open("./temp.jpg","rb")}

    r=requests.post(compare_url,data=payload,files=files)

    temp=json.loads(r.text)

    print_dict(temp)
    input("Enter any key to continue...")

    files["image_file1"].close()
    files["image_file2"].close()
    os.remove("./temp.jpg")
    
    


def register():
    print("[INFO] Opening camera...")
    cap=cv2.VideoCapture(0)
    while True:
        ret,frame=cap.read()
        if ret:
            #print("[INFO] Opening camera...")
            img=cv2.flip(frame,1,dst=None)
            cv2.imshow("Camera",img)
            if cv2.waitKey(1) & 0xFF == ord('c'):
                cv2.imwrite("./base.jpg",img)
                cap.release()
                cv2.destroyAllWindows()
                print("[INFO] Register successed")
                input("Enter any key to continue...")
                return True
        else:
            print("[ERRO] Error capture...")
    cap.release()
    cv2.destroyAllWindows()
    return False


def print_menu():
    os.system("cls")
    print(" Face Recognition demo  ")
    print("             --Code by cc")
    print("=========================")
    print("     1.register          ")
    print("     2.recognize         ")
    print("     0.exit              ")
    print("=========================")

if __name__=="__main__":
    x=""
    while True:
        print_menu()
        x=input("Enter your Choice:")
        if x[0]=='1':
            os.system("cls")
            register()
        elif x[0]=='2':
            os.system("cls")
            recognize()
        elif x[0]=='0':
            exit(0)
        else:
            continue

    

        
            
