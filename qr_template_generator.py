import argparse
from pathlib import Path

try:
    import qrcode
    from PIL import Image
except ImportError as e:
    raise SystemExit("Required packages not found. Please install 'qrcode[pil]' and 'Pillow'.")


def generate_qr(url: str, qr_size: int = 300) -> Image.Image:
    """Generate a QR code image from a URL."""
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img.resize((qr_size, qr_size), Image.LANCZOS)


def apply_template(template_path: Path, qr_img: Image.Image, x: int, y: int) -> Image.Image:
    """Paste the QR code onto the template at the given coordinates."""
    template = Image.open(template_path).convert("RGB")
    template.paste(qr_img, (x, y))
    return template


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a QR code on a template image")
    parser.add_argument("url", help="URL to encode in the QR code")
    parser.add_argument("-t", "--template", required=True, help="Path to background template image")
    parser.add_argument("-o", "--output", default="output.png", help="Output image filename")
    parser.add_argument("--x", type=int, default=0, help="X coordinate for QR code placement")
    parser.add_argument("--y", type=int, default=0, help="Y coordinate for QR code placement")
    parser.add_argument("--size", type=int, default=300, help="Width/height of generated QR code in pixels")
    args = parser.parse_args()

    qr_img = generate_qr(args.url, args.size)
    result = apply_template(Path(args.template), qr_img, args.x, args.y)
    result.save(args.output)
    print(f"Saved QR template to {args.output}")


if __name__ == "__main__":
    main()
