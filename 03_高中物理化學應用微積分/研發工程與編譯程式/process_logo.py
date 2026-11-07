import fitz
import numpy as np
from PIL import Image

svg_path = r'C:\Users\user\Documents\woieyufan-logo_downward.svg'
svg_doc = fitz.open(svg_path)
page = svg_doc[0]
pix = page.get_pixmap(dpi=300)

img = np.frombuffer(pix.samples, dtype=np.uint8).reshape((pix.height, pix.width, pix.n))
# Crop to content bbox scaled to dpi 300 (which is 2x dpi 150)
scale = 300 / 150
x_min, x_max = int(260 * scale), int(1014 * scale)
y_min, y_max = int(472 * scale), int(1209 * scale)

cropped = img[y_min:y_max, x_min:x_max]
print("Cropped shape:", cropped.shape)

# Create PIL Image with transparency
pil_img = Image.fromarray(cropped).convert("RGBA")
datas = pil_img.getdata()

# Replace white background with transparent
new_data = []
for item in datas:
    # If pixel is near pure white, make it transparent
    if item[0] > 245 and item[1] > 245 and item[2] > 245:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

pil_img.putdata(new_data)
badge_path = r'C:\Users\user\Documents\logo_badge.png'
pil_img.save(badge_path, "PNG")
print("Saved transparent logo badge:", badge_path)
