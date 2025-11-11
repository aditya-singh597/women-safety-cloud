from PIL import Image
import matplotlib.pyplot as plt

img = Image.open("D:\logo.png")

# Rotate the image
rotated = img.rotate(45, expand=True)

# Show both
plt.subplot(1, 2, 1)
plt.title("Original Logo")
plt.imshow(img)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Rotated Logo")
plt.imshow(rotated)
plt.axis('off')

plt.show()
