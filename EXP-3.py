import cv2

# Read the image
img = cv2.imread("image1.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect edges
edges = cv2.Canny(gray, 100, 200)

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edges", edges)

# Save output
cv2.imwrite("canny_edges.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()