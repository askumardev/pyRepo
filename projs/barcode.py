#!/usr/bin/env python3
"""Generate a barcode image from text using python-barcode."""

import os
import sys

try:
    import barcode
    from barcode.writer import ImageWriter
except ImportError:
    print("Missing dependency: pip install python-barcode pillow")
    sys.exit(1)

DEFAULT_TEXT = "https://example.com"
DEFAULT_FORMAT = "code128"


def generate_barcode(text: str, out_path: str, barcode_format: str = DEFAULT_FORMAT) -> str:
    """Generate barcode image and return saved file path."""
    text = text.strip() or DEFAULT_TEXT
    if not text:
        raise ValueError("Text must be provided for barcode generation")

    barcode_format = barcode_format.lower()
    if barcode_format not in barcode.PROVIDED_BARCODES:
        raise ValueError(
            f"Unsupported barcode format: {barcode_format}. "
            f"Choose from {', '.join(sorted(barcode.PROVIDED_BARCODES))}."
        )

    out_path = os.path.abspath(out_path)
    out_dir = os.path.dirname(out_path)
    if out_dir and not os.path.exists(out_dir):
        os.makedirs(out_dir, exist_ok=True)

    filename, _ = os.path.splitext(out_path)
    my_code = barcode.get(barcode_format, text, writer=ImageWriter())
    saved_file = my_code.save(filename)
    return saved_file


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Generate barcode from text")
    parser.add_argument("text", nargs="?", default=DEFAULT_TEXT, help="Text or number to encode")
    parser.add_argument("--format", default=DEFAULT_FORMAT, help="Barcode symbology (code128, ean13, etc.)")
    parser.add_argument("--out", default="output/barcode.png", help="Output image path")
    args = parser.parse_args()

    try:
        output_path = generate_barcode(args.text, args.out, args.format)
        print(f"Barcode saved to: {output_path}")
    except Exception as err:
        print(f"Error: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
