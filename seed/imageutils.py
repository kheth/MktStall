#import peaimage
import cv2
import os
from peautils import PeaUtils


class ImageUtils:
    def __init__(self, config):
        print "hello"
        self.config_file = config

    @staticmethod
    def get_grayscale_gaussian_otsus_image_copy(in_path, config_file):
        # Open image this image.
        input_image = cv2.cv.LoadImage(in_path)
        # Make a copy of same dimension.
        grey_image = cv2.cv.CreateImage(cv2.cv.GetSize(input_image), cv2.cv.IPL_DEPTH_8U, 1)
        # Transformation - Greyscale.
        cv2.cv.CvtColor(input_image, grey_image, cv2.cv.CV_BGR2GRAY);  # changed from cv.CV_BGR2GRAY
        # Make the save path with "grey.jpg" suffix.
        out_name, out_path = PeaUtils.get_file_path("B", in_path, ".jpg")
        # Save transformed image.
        cv2.cv.SaveImage(out_path, grey_image)
        img = cv2.imread(out_path, 0)
        # Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        out_name_2, out_path_2 = PeaUtils.get_file_path("H", out_path, ".jpg")
        cv2.imwrite(out_path_2, th3)
        os.remove(out_path)
        print "OUTPATH: ", out_path_2
        return out_path_2
        #return peaimage.PeaImage(out_name_2, out_path_2, config_file)