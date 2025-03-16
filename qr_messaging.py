import qrcode
import cv2
from encryption import encrypt_message, decrypt_message

def generate_qr(message, password, filename='encrypted_qr.png'):
    encrypted_message = encrypt_message(message, password)
    img = qrcode.make(encrypted_message)
    img.save(filename)
    print(f"[QR GENERATED] Saved as {filename}")

def scan_qr(filename, password):
    detector = cv2.QRCodeDetector()
    img = cv2.imread(filename)
    data, _, _ = detector.detectAndDecode(img)
    if data:
        message = decrypt_message(data, password)
        print(f"[MESSAGE FROM QR] {message}")
    else:
        print("[ERROR] QR Code not detected or unreadable.")

if __name__ == "__main__":
    mode = input("Choose mode (generate/scan): ").lower()
    password = input("Enter encryption password: ")

    if mode == 'generate':
        message = input("Enter your message: ")
        generate_qr(message, password)
    elif mode == 'scan':
        filename = input("Enter QR image filename: ")
        scan_qr(filename, password)
