import qrcode

def generate_qr_code(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

if __name__ == "__main__":
    data = "https://google.com"  # QR kodingiz uchun kerakli ma'lumotni joylashtiring
    file_name = "qr_code.png"  # Saqlanadigan QR kodning fayl nomi
    generate_qr_code(data, file_name)
