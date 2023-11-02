from PIL import Image, ImageEnhance
import os

test_dir = "test"
dst_dir = "ll_test"


subject_ids = [d for d in os.listdir(test_dir)]
count = 0
# Move subdirectories to the test directory
for subject in subject_ids:
    subject_path = os.path.join(test_dir, subject)
    img_name = os.listdir(subject_path)[0]
    img_path = os.path.join(subject_path, img_name)

    normal_img = Image.open(img_path)

    # Image brightness enhancer
    bright_enhancer = ImageEnhance.Brightness(normal_img)
    factor = 0.15
    img_bright = bright_enhancer.enhance(factor)

    # Image contrast enhancer
    contrast_enhancer = ImageEnhance.Contrast(img_bright)
    factor = 1.5
    img_output = contrast_enhancer.enhance(factor)

    dst = os.path.join(dst_dir, subject)
    os.makedirs(dst, exist_ok=True)
    img_output.save(os.path.join(dst, 'low_light_{img_name}'.format(img_name=img_name)))
    count = count + 1
    print(count)