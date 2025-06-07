# QR Template Generator

This repository contains a simple script for generating QR codes from a URL and placing them on a custom template image.

## Requirements

- Python 3.8+
- [`qrcode`](https://pypi.org/project/qrcode/) with Pillow support
- [`Pillow`](https://pypi.org/project/Pillow/)

Install dependencies with:

```bash
pip install qrcode[pil] Pillow
```

## Usage

```
python qr_template_generator.py URL -t TEMPLATE_PATH [options]
```

Options:

- `-o`, `--output`: Name of the generated image file (default: `output.png`).
- `--x`: X coordinate of the QR code's top-left corner on the template (default: `0`).
- `--y`: Y coordinate of the QR code's top-left corner on the template (default: `0`).
- `--size`: Size of the generated QR code in pixels (default: `300`).

The template image should be any standard image format (PNG, JPEG, etc.). The script will place the generated QR code onto the template at the specified coordinates and save the result as the output image. You can then print the resulting file with any image viewer.

## Example

```
python qr_template_generator.py "https://example.com" -t my_template.png --x 50 --y 100 -o qr_output.png
```

This will create `qr_output.png` with a QR code for `https://example.com` pasted onto `my_template.png` at position `(50, 100)`.

