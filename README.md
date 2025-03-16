# 📬 Offline Encrypted Messaging System

A spy-inspired, peer-to-peer messaging system that works entirely without an internet connection. It allows secure communication through either local networks or QR codes, ensuring privacy with end-to-end encryption.

---

## ✅ Features

- **Offline Messaging:** Send messages without internet connectivity.
- **Local Network (Sockets)**: Communicate securely over a local network (LAN).
- **QR Code Messaging:** Exchange encrypted messages via generated QR codes.
- **End-to-End Encryption:** All messages secured using AES encryption (via PyCryptodome).

---

## 🛠️ Tech Stack

- **Python**
- **Socket Programming** (Local network communication)
- **PyCryptodome** (Encryption & decryption)
- **qrcode & OpenCV** (QR code generation & scanning)

---

## 🚀 How to Run

### ⚙️ Install Requirements
```bash
pip install -r requirements.txt
```

### 📡 Local Network Messaging

**Step 1: Start Server**
```bash
python messaging.py
```
- Choose `server` mode.
- Provide your encryption password.

**Step 2: Send Message** (in another terminal)
```bash
python messaging.py
```
- Choose `client` mode.
- Enter the same encryption password.
- Provide the IP address of the recipient (for testing locally, use `127.0.0.1`).
- Enter your message.

### 📷 QR Code Messaging

**Generate QR code**
```bash
python qr_messaging.py
```
- Select `generate`.
- Provide your encryption password.
- Enter your message.
- QR code image (`encrypted_qr.png`) is generated.

**Scan QR code**
```bash
python qr_messaging.py
```
- Select `scan`.
- Provide the encryption password.
- Enter QR code image filename (`encrypted_qr.png`).

---

## 📝 Project Structure
```
offline-encrypted-messaging/
├── encryption.py       # Encryption & Decryption
├── messaging.py        # LAN Messaging via sockets
├── qr_messaging.py     # QR Code Messaging
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔑 Security Tips

- Always keep encryption passwords safe and secure.
- Change passwords frequently.

---

## 🚧 Troubleshooting

If OpenCV errors occur, run:
```bash
sudo apt-get update && sudo apt-get install -y libgl1-mesa-glx libglib2.0-0
```

---

## 📖 License

MIT License

---

✨ **Enjoy your secure, offline messaging!**

