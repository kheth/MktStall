import os
import subprocess
from typing import Union


class PdfReader:

    def __init__(self, input_directory, output_directory, debug, verbose):
        self.DEBUG = debug
        self.VERBOSE = verbose
        self.input_directory = input_directory
        self.output_directory = output_directory
        self.DPI = "300"

    def set_dpi(self, dpi_to_be_set):
        """
        Function: set dpi of image
        """
        self.DPI = dpi_to_be_set

    @staticmethod
    def get_list_of_pdf_s_in_directory(directory):
        """
        Gets a list of the pdf s in the provided directory.
        :param directory:
        :return: a list of pdf file names.
        """
        tmp_list = os.listdir(directory)
        ret_list = []
        for f in tmp_list:  # type: Union[str, unicode]
            if f.endswith(".pdf"):
                ret_list.append(directory + "/" + f)
                print "Adding pdf to be converted: " + directory + "/" + f

        return ret_list

    def delete_pdf_s(self, list_of_pdf_s):
        for f in list_of_pdf_s:
            if self.DEBUG:
                print "Deleting pdf: " + f
            os.remove(f)

    def get_list_of_jpeg_s_in_directory(self, directory):
        tmp_list = os.listdir(directory)
        ret_list = []
        for f in tmp_list:
            if f.endswith(".jpg") or f.endswith(".jpeg"):
                ret_list.append(directory + "/" + f)
                if self.DEBUG:
                    print "Adding image to list in [get_list_of_jpeg_s_in_directory()]: " + directory + "/" + f
        return ret_list

    def pdf_reader_pdf_to_image(self):
        """"
        Function: Execute the Java command for PDF box pdfToImage
        """
        pdf_s = self.get_list_of_pdf_s_in_directory(self.input_directory)
        for f in pdf_s:
            prefix = f+".toJpg."
            # pdf = self.input_directory + "/" + f
            subprocess.check_output(['java',
                                     '-jar',
                                     '../resources/pdfbox/pdfbox-app-2.0.7.jar',
                                     'PDFToImage',
                                     '-outputPrefix',
                                     prefix,
                                     '-dpi',
                                     self.DPI,
                                     f])
        self.delete_pdf_s(pdf_s)
        return self.get_list_of_jpeg_s_in_directory(self.input_directory)
