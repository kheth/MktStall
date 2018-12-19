import re
from peautils import PeaUtils


class ImageLabel:

    def __init__(self, image_label_list):
        self.DEBUG = False
        self.imageLabelList = image_label_list
        self.accession_label = ""
        self.imageAcceptable = False
        self.acceptable_list_of_labels = []
        self.unacceptable_list_of_labels = []

    def process_image_label(self):
        clean_label_list = self.make_clean_ocr_label_list()
        self.imageAcceptable = self.is_image_label_acceptable(clean_label_list)
        if self.imageAcceptable:
            self.imageLabelList = clean_label_list
        return self.imageAcceptable

    def make_clean_ocr_label_list(self):
        """
        Function: Clean the imageLabelList
        """
        clean_label_list = []
        if self.DEBUG:
            print "Generate Lable - IN: ", self.imageLabelList
        for dirty_label in self.imageLabelList:
            cleaned_label = self.generate_label(dirty_label)
            if cleaned_label:
                clean_label_list.append(cleaned_label)
        if self.DEBUG:
            print "Generate Lable - OUT: ", clean_label_list
        return clean_label_list

    def print_image_label_list(self, prefix):
        for label in self.imageLabelList:
            print prefix, label

    def generate_label(self, label_string):
        """

        :param label_string:
        :return:
        """
        if "_" in label_string:
            if self.DEBUG:
                print "Before re: ", label_string
            s = re.sub('[^0-9a-zA-Z]+', '*', label_string)  # replace nonalphas with star
            if self.DEBUG:
                print "After re: ", s
            stringlist = s.split("*")  # split by star
            if self.DEBUG:
                print "String list after re: ", stringlist
            for i, e in reversed(list(enumerate(stringlist))):  # in reverse order, enumerate split list
                # use a sliding window to test for a pattern within a substring
                if i >= 2:  # check there are a minimum of 3 elements
                    if PeaUtils.is_number(stringlist[i]):  # is last element in the trio a number
                        if PeaUtils.is_number(stringlist[i - 1]):  # is penultimate in trio a number
                            if PeaUtils.is_number(stringlist[i - 2]):  # is ultimate in trio a number
                                string2 = stringlist[i - 2] + "_" + stringlist[i - 1] + "_" + stringlist[i]  # build
                                if self.DEBUG:
                                    print "Printing raw stringList: ", stringlist
                                if len(string2) > 5:  # if string is longer than short id
                                    return "tg_" + string2  # firstline
                                else:
                                    return string2  # secondline

    def get_image_label_list(self):
        pass

    def test_image_label_quality(self):
        pass

    def is_image_label_acceptable(self, clean_label_list):
        if len(clean_label_list) < 2:
            if self.DEBUG:
                print "A full label was not generated! Begin further thresholding."
            self.imageAcceptable = False
        else:
            self.imageAcceptable = True
        return self.imageAcceptable

    def append_acceptable_labels_somewhere(self, in_clean_label_list):
        if self.is_image_label_acceptable(in_clean_label_list):
            self.acceptable_list_of_labels.append(self.imageLabelList)
            if self.DEBUG:
                print "acceptable list of labels"
                print self.acceptable_list_of_labels
        else:
            self.unacceptable_list_of_labels.append(self.imageLabelList)
            if self.DEBUG:
                print "unacceptable list of labels"
                print self.unacceptable_list_of_labels
