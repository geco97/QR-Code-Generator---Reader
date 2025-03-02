# QR Code Generator & Scanner

This project provides a **QR Code Generator** and a **QR Code Scanner** with AI-powered content optimization and an integrated logging system. It allows users to generate and scan QR codes directly from their screen.

## 📌 Features

### ✅ QR Code Generator
- Extracts metadata (title & description) from URLs.
- Uses **AI summarization** to optimize the content.
- Generates **QR codes** from text or URLs.
- Saves QR codes as an image (`qr_code.png`).
- **Logs all generated QR codes** for tracking.

### ✅ QR Code Scanner
- Automatically scans QR codes **visible on the screen**.
- Uses **OpenCV and Pyzbar** to decode QR codes.
- Displays the scanned QR code content.
- Supports auto-wrapping of text to fit the screen.
- **Logs all scanned QR codes** for future reference.

### ✅ Logging System
- Tracks **all QR generation & scanning**.
- Stores logs in the `logs/qr_scanner.log` file.
- **Error handling** logs any issues occurring in the program.

---

## 🚀 Installation

### **Step 1: Clone the Repository**
```bash
git clone https://github.com/your-repo/QR_Code_Project.git
cd QR_Code_Project
```

### **Step 2: Install Dependencies**
```bash
pip install -r requirements.txt
```

---

## 🛠 How to Use

### **1️⃣ Generate a QR Code**
Run the QR code generator and enter the text or URL:
```bash
python run_qr_generator.py
```
📌 **The QR code will be saved as** `qr_code.png`

### **2️⃣ Scan a QR Code from the Screen**
Run the QR code scanner:
```bash
python run_qr_reader.py
```
📌 **Ensure a QR code is visible on the screen** before running the scanner.

---

## 📚 Libraries Used

| Library        | Purpose                         |
|---------------|---------------------------------|
| `qrcode`      | Generates QR codes              |
| `requests`    | Fetches metadata from URLs      |
| `beautifulsoup4` | Parses website data          |
| `sumy`        | AI-powered text summarization  |
| `PIL (pillow)` | Image processing               |
| `pygame`      | Displays scanned QR content    |
| `opencv-python` | Converts images for scanning  |
| `pyzbar`      | Decodes QR codes from images   |
| `numpy`       | Image array processing         |
| `logging`     | Tracks QR generation & scans   |

---

## 📌 Logging System
- **Log File Location:** `logs/qr_scanner.log`
- **Tracks:**
  - ✅ Generated QR codes
  - ✅ Scanned QR codes
  - ✅ Errors encountered

---

## 📌 Future Improvements
- ✅ **Real-time QR code scanning** using webcam.
- ✅ **Dynamic QR codes** that update based on user interaction.
- ✅ **Save scanned QR results to a database.**
- ✅ **Clipboard support** to copy scanned QR text automatically.

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 📝 Author
Developed by **GECO97** 🚀
