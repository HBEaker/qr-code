import qrcode
import sys

def generate_qr_code(url, filename):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)
    print(f"QR code saved as {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python qr_code_generator.py <URL> <output_filename.png>")
        sys.exit(1)
    
    url = sys.argv[1]
    filename = sys.argv[2]
    
    generate_qr_code(url, filename)
