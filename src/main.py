import cv2

WINDOW_NAME = "HandTrack - Webcam"

def main():
    # Initialize the default webcam
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        camera.release()
        raise RuntimeError("Unable to open the webcam.")

    print("HandTrack started.")
    print("Press Q to quit.")

    try:
        while True:
            # Capture a video frame
            success, frame = camera.read()

            if not success or frame is None:
                print("Error: unable to read webcam frame.")
                break

            # Mirror the image
            frame = cv2.flip(frame, 1)

            # Display instructions
            cv2.putText(
                frame,
                "HandTrack | Press Q to quit",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

            # Display the video
            cv2.imshow(WINDOW_NAME, frame)

            # Exit when Q is pressed
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

    finally:
        # Release resources
        camera.release()
        cv2.destroyAllWindows()
        print("HandTrack stopped.")


if __name__ == "__main__":
    main()
