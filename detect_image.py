import cv2

# Load the pre-trained face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

def detect_faces(image_path):
    # Read the image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image '{image_path}'")
        return

    # Convert to grayscale (required for detection)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    # scaleFactor: how much the image size is reduced at each scale
    # minNeighbors: how many neighbors each rectangle should retain
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=8,
        minSize=(60, 60)
    )

    print(f"Found {len(faces)} face(s)")

    # Draw rectangles around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, "Face", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    # Show and save the result
    cv2.imshow("Face Detection", img)
    cv2.imwrite("output.jpg", img)
    print("Saved result to output.jpg")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# --- Run it ---
detect_faces("your_image.jpg")   # Replace with your image path