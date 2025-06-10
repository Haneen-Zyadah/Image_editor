from PIL import Image, ImageFilter, ImageEnhance


def load_image(path):
    try:
        image = Image.open(path)
        print(f"Image loaded: {image.format}, {image.size}, {image.mode}")
        return image
    except Exception as e:
        print(print(f"Error loading image: {e}"))
        return None


def resize_image(image, width, height):
    return image.resize((width, height))


def convert_to_grayscale(image):
    return image.convert("L")


def apply_blur(image, radius=2):
    return image.filter(ImageFilter.GaussianBlur(radius))


def rotate_image(image, angle):
    return image.rotate(angle)


def adjust_brightness(image, factor):
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)


def adjust_contrast(image, factor):
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(factor)


def save_image(image, path):
    image.save(path)
    print(f"Image saved to {path}")
