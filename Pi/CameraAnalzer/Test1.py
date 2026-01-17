import cv2
import numpy as np

# Učitaj sliku
image = cv2.imread("JacaSlika.jpg")

# Proveri da li je slika učitana
if image is None:
    raise ValueError("Slika nije pronađena")

# Konvertuj u grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Izaberi ArUco dictionary (najčešći)
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

# Parametri detekcije
aruco_params = cv2.aruco.DetectorParameters()

# Detektor
detector = cv2.aruco.ArucoDetector(aruco_dict, aruco_params)

# Detekcija
corners, ids, rejected = detector.detectMarkers(gray)

# Ako su nađeni ArUco kodovi
if ids is not None:
    for i in range(len(ids)):
        marker_id = ids[i][0]
        marker_corners = corners[i][0]  # shape (4,2)

        # Uglovi
        top_left     = marker_corners[0]
        top_right    = marker_corners[1]
        bottom_right = marker_corners[2]
        bottom_left  = marker_corners[3]

        # Centar markera
        center_x = int(np.mean(marker_corners[:, 0]))
        center_y = int(np.mean(marker_corners[:, 1]))
        center = (center_x, center_y)

        print(f"ArUco ID: {marker_id}")
        print(f"  Top Left:     {top_left}")
        print(f"  Top Right:    {top_right}")
        print(f"  Bottom Right: {bottom_right}")
        print(f"  Bottom Left:  {bottom_left}")
        print(f"  Center:       {center}")
        print("-" * 40)

        # Iscrtavanje (opciono)
        cv2.polylines(
            image,
            [marker_corners.astype(np.int32)],
            True,
            (0, 255, 0),
            2
        )
        cv2.circle(image, center, 5, (0, 0, 255), -1)
        cv2.putText(
            image,
            f"ID {marker_id}",
            (center_x - 20, center_y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (255, 0, 0),
            2
        )

else:
    print("Nijedan ArUco kod nije pronađen.")

# Prikaz slike
cv2.imshow("ArUco Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
