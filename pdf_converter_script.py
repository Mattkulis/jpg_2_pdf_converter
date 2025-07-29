from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import inch
from PIL import Image
import os

# === CONFIG ===
output_pdf = "Final_TRW_KDP_Book.pdf"
num_pages = 45  # update this if your page count changes
image_folder = os.getcwd()  # assumes script is in the same folder

# === KDP Trim size (6.125 x 9.25 inches) in points
PAGE_WIDTH = 6.125 * inch  # 441 pts
PAGE_HEIGHT = 9.25 * inch  # 666.75 pts

# === Create PDF ===
c = canvas.Canvas(output_pdf, pagesize=(PAGE_WIDTH, PAGE_HEIGHT))

for i in range(1, num_pages + 1):
    image_path = os.path.join(image_folder, f"Page{i}.jpg")
    if os.path.exists(image_path):
        c.drawImage(image_path, 0, 0, width=PAGE_WIDTH, height=PAGE_HEIGHT)
        c.showPage()
    else:
        print(f"❌ Missing: {image_path}")

c.save()
print(f"✅ PDF created successfully: {output_pdf}")
