import cv2

# Read the image
img = cv2.imread("image1.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display original and grayscale images
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)

# Save grayscale image
cv2.imwrite("gray_image.jpg", gray)

# Wait until a key is pressed
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()