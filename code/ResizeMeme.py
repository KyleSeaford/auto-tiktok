from PIL import Image, ImageDraw
import logging
import os

# Set logging
logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='./ZZ_logs/resize.log', filemode='w')

def resize_and_center(input_folder, output_folder):
    target_size = (1080, 1920)
    dot_size = 5

    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            with Image.open(input_path) as img:
                # Resize the original image to be 1080 wide
                resized_img = img.resize((1080, int(img.height * (1080 / img.width))))

                # Skip images with height greater than 1920
                if resized_img.height > 1920:
                    logging.warning(f"Skipped: {filename} - Height greater than 1920")
                    continue

                # black bars to make it 1080x1920
                new_img = Image.new("RGB", target_size, (0, 0, 0))
                new_img.paste(resized_img, ((target_size[0] - resized_img.width) // 2, (target_size[1] - resized_img.height) // 2))

                # dots at bottom
                draw = ImageDraw.Draw(new_img)
                center_x = target_size[0] // 2
                center_y = target_size[1] - 70  # dot hight 
                dot_spacing = 25  # dots spacing

                for _ in range(5):
                    dot_x = center_x - dot_spacing + (_ * dot_spacing)
                    dot_y = center_y
                    draw.ellipse((dot_x - dot_size, dot_y - dot_size, dot_x + dot_size, dot_y + dot_size), fill=(255, 255, 255))

                # Save the resized and centered image
                new_img.save(output_path)
                logging.info(f"Resized and centered: {filename}")

if __name__ == "__main__":
    input_folder = "meme"
    output_folder = "new_memes"

    logging.critical("Starting image resize and center")
    resize_and_center(input_folder, output_folder)

    logging.critical("Images resized and centered successfully.")
    print("done")
