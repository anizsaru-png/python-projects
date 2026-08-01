import qrcode
import os

def generate_qr(data, filename="qr_code.png", folder="qr_codes"):
    """Generate a QR code from given data and save it as an image."""
    
    # Create folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Create QR code object
    qr = qrcode.QRCode(
        version=1,                  # controls size (1 = smallest, 40 = largest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,                 # size of each box in pixels
        border=4,                    # thickness of border
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    filepath = os.path.join(folder, filename)
    img.save(filepath)
    print(f"✅ QR code saved at: {filepath}")

def main():
    print("=== QR Code Generator ===")
    data = input("Enter the text or URL to encode: ")
    filename = input("Enter filename to save as (e.g. mycode.png): ")

    if not filename.endswith(".png"):
        filename += ".png"

    generate_qr(data, filename)

if __name__ == "__main__":
    main()