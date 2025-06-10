from editor import (
    load_image,
    resize_image,
    convert_to_grayscale,
    apply_blur,
    rotate_image,
    adjust_brightness,
    adjust_contrast,
    save_image,
)


def main():
    image_path = input("Enter Image Path: (e.g. assets/OIP.jpg) ")
    image = load_image(image_path)

    if not image:
        return
    
    history = [image]
    while True:
        print("\nWhat would you like to do?")
        print("1. Resize image")
        print("2. Convert to grayscale")
        print("3. Apply blur")
        print("4. Rotate image")
        print("5. Adjust brightness")
        print("6. Adjust contrast")
        print("7. Undo last edit")
        print("8. Save and exit")
        print("9. Exit without saving")
        choice = input("Enter your choice (1-9): ")

        if choice == "1":
            width = int(input("Enter new width: "))
            height = int(input("Enter new height: "))
            image = resize_image(image, width, height)
            image.show()
        elif choice == "2":
            image = convert_to_grayscale(image)
            print("Image converted to grayscale.")
            image.show()
        elif choice == "3":
            radius = float(input("Enter blur radius: "))
            image = apply_blur(image, radius)
            print(f"Image blurred with radius {radius}.")
            image.show() 
        elif choice == "4":
            angle = float(input("Enter rotation angle (in degrees): "))
            image = rotate_image(image, angle)
            print(f"Image rotated by {angle} degrees.")
            image.show()

        elif choice == "5":
            factor = float(input("Brightness factor (e.g., 1.2 for brighter, 0.8 for darker): "))
            image = adjust_brightness(image, factor)
            print(f"Adjusted brightness by factor {factor}.")
            image.show()

        elif choice == "6":
            factor = float(input("Contrast factor (e.g., 1.2 for more contrast, 0.8 for less): "))
            image = adjust_contrast(image, factor)
            print(f"Adjusted contrast by factor {factor}.")
            image.show()
            
        elif choice == "7":
            if len(history) > 1:
                history.pop()
                image = history[-1]
                print("Undo successful.")
                image.show()  # Show the image after undoing
            else:
                print("Nothing to undo.")

        elif choice == "8":
            save_path = input("Enter save path (e.g., output/edited.jpg): ")
            if not (save_path.endswith(".jpg") or save_path.endswith(".jpeg") or save_path.endswith(".png")):
                save_path += ".jpeg"
            save_image(image, save_path)
            break
        elif choice == "9":
            print("Exiting without saving.")
            break
        else:
            print("Invalid choice. Please try again.")
            
        history.append(image)


if __name__ == "__main__":
    main()
