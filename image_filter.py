from PIL import Image, ImageFilter

# Open an image
filename = input("Enter image file name (e.g., photo.jpg): ")

try:
    image = Image.open(filename).convert("RGB")
    print("Image opened successfully.")

    print("\n--- Digital Image Filter Utility ---")
    print("1. Grayscale Conversion")
    print("2. Black and White Threshold")
    print("3. Blur Filter")
    print("4. RGB Color Adjustment")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        # Convert image to grayscale
        pixels = image.load()

        for x in range(image.width):
            for y in range(image.height):
                r, g, b = pixels[x, y]
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)
                pixels[x, y] = (gray, gray, gray)

        output = "grayscale.png"
        image.save(output)
        print("Grayscale image saved.")

    elif choice == 2:
        # Convert image to black and white
        threshold = int(input("Enter threshold (0-255): "))
        pixels = image.load()

        for x in range(image.width):
            for y in range(image.height):
                r, g, b = pixels[x, y]
                gray = int(0.299 * r + 0.587 * g + 0.114 * b)

                if gray >= threshold:
                    pixels[x, y] = (255, 255, 255)
                else:
                    pixels[x, y] = (0, 0, 0)

        output = "black_white.png"
        image.save(output)
        print("Black and white image saved.")

    elif choice == 3:
        # Apply blur filter
        radius = float(input("Enter blur radius (e.g., 2): "))

        if radius < 0:
            print("Blur radius cannot be negative.")
        else:
            image = image.filter(ImageFilter.GaussianBlur(radius))
            output = "blurred.png"
            image.save(output)
            print("Blurred image saved.")

    elif choice == 4:
        # Adjust RGB color channels
        red = int(input("Enter red adjustment (-255 to 255): "))
        green = int(input("Enter green adjustment (-255 to 255): "))
        blue = int(input("Enter blue adjustment (-255 to 255): "))

        pixels = image.load()

        for x in range(image.width):
            for y in range(image.height):
                r, g, b = pixels[x, y]

                r = max(0, min(255, r + red))
                g = max(0, min(255, g + green))
                b = max(0, min(255, b + blue))

                pixels[x, y] = (r, g, b)

        output = "color_adjusted.png"
        image.save(output)
        print("Color-adjusted image saved.")

    else:
        print("Invalid choice.")

    if choice in (1, 2, 3, 4) and (choice != 3 or radius >= 0):
        print("Output file:", output)
        image.show()

except FileNotFoundError:
    print("Error: Image file not found.")

except Exception as e:
    print("Error:", e)
    