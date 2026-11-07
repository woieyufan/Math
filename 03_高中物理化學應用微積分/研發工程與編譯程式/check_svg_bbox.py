import fitz

svg_path = r'C:\Users\user\Documents\woieyufan-logo_downward.svg'
svg_doc = fitz.open(svg_path)
page = svg_doc[0]
pix = page.get_pixmap(dpi=150)
print("Pixmap alpha:", pix.alpha)

# Find bounding box of non-white / non-transparent pixels
import numpy as np
# Convert to numpy array
img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
print("Image shape:", img.shape)

if pix.alpha:
    # check alpha channel > 0
    alpha = img[:, :, -1]
    non_empty = np.where(alpha > 10)
else:
    # check if not pure white (assuming white background)
    non_white = np.where((img[:, :, 0] < 250) | (img[:, :, 1] < 250) | (img[:, :, 2] < 250))
    non_empty = non_white

if len(non_empty[0]) > 0:
    y_min, y_max = non_empty[0].min(), non_empty[0].max()
    x_min, x_max = non_empty[1].min(), non_empty[1].max()
    print(f"Content bbox in pixels: x=[{x_min}, {x_max}], y=[{y_min}, {y_max}]")
    print(f"Content dimensions: width={x_max - x_min}, height={y_max - y_min}")
    aspect_ratio = (x_max - x_min) / (y_max - y_min)
    print(f"Aspect ratio (w/h): {aspect_ratio:.3f}")
else:
    print("No non-empty pixels found!")
