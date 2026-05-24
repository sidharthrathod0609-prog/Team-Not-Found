import shutil
import os

dest_dir = r"c:\Users\Sidharth Rathod\Downloads\Team-Not-Found-main\Team-Not-Found-main\frontend\public\assets\images\thumbs"

# Source files (already high-quality premium images)
high_quality_imgs = [
    "product-img1.png",   # broccoli
    "product-img2.png",   # bananas
    "product-img3.png",   # strawberries
    "product-img5.png",   # apples
    "product-img6.png",   # oranges
    "product-img7.png",   # c-500
    "product-img8.png",   # almond milk
    "product-img9.png",   # organic milk
    "product-img10.png",  # bread
    "product-img11.png",  # yogurt
    "product-img12.png",  # protein bar
    "product-img16.png",  # salmon
    "flash-sale-img1.png",
    "flash-sale-img2.png"
]

# We want to replace product-two-img1.png to product-two-img15.png
for i in range(1, 16):
    src_file = high_quality_imgs[(i - 1) % len(high_quality_imgs)]
    src_path = os.path.join(dest_dir, src_file)
    dest_path = os.path.join(dest_dir, f"product-two-img{i}.png")
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_file} to product-two-img{i}.png")

# We want to replace trending-three-img1.png to trending-three-img10.png
for i in range(1, 11):
    src_file = high_quality_imgs[(i + 2) % len(high_quality_imgs)]
    src_path = os.path.join(dest_dir, src_file)
    dest_path = os.path.join(dest_dir, f"trending-three-img{i}.png")
    if os.path.exists(src_path):
        shutil.copy2(src_path, dest_path)
        print(f"Copied {src_file} to trending-three-img{i}.png")

print("Asset copying complete!")
