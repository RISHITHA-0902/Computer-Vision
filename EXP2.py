import cv2

# Read the image
img = cv2.imread("image1.jpg")

# Apply Gaussian Blur
blur = cv2.GaussianBlur(img, (5, 5), 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)

# Save output
cv2.imwrite("blurred_image.jpg", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()