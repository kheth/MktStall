import os
from htmlmaker import HtmlMaker
from csvmaker import CsvMaker
from pdfreader import PdfReader
from peaimage import PeaImage
from pcamaker import PcaMaker


class PeaImageCollection:

    def __init__(self, directory_path, debug, verbose, config):
        self.debug = debug
        self.verbose = verbose
        self.dir_path = directory_path
        self.dir_size = self.get_directory_size(self.dir_path)
        self.image_count = ""
        # List the images objects that comprise the collection
        self.images = []
        self.config_file = config

    def analyse_images(self):
        for PeaImage in self.images:
            print ""
            print "#################################"
            PeaImage.analyse_image()
            # PeaImage.getStaticRegionConvexHulls()

    def convert_pdf_to_jpg(self):
        """
        Function: Convert all pdfs to jpgs
        :param: inputDirectoryContainingPdf
        """
        # list of my image objects
        reader = PdfReader(self.dir_path, self.dir_path, self.debug, self.verbose)
        temp_list = reader.pdf_reader_pdf_to_image()
        print "Number of images held in temp list that have been converted: ", len(temp_list)
        ret_list = []
        for e in temp_list:
            ret_list.append(PeaImage(os.path.basename(e), e, self.config_file))
        if self.verbose:
            print "Number of images held in collection: ", len(ret_list)
        self.images = ret_list
        return ret_list

    def affirm_image_collection_is_portrait(self):
        """
        Function: make sure that all images within the collection are of the portrait orientation.
        """
        print "Affirming image collection is portrait."
        for img in self.images:
            img.affirm_image_is_portrait()

    def make_csv(self, out_dir):
        mktstall_csv = CsvMaker()
        mktstall_csv.make_csv(out_dir, self.images)


    def make_html(self, out_dir, config):
        mktstall_html = HtmlMaker(config)
        mktstall_html.make_html(out_dir, self.images)

    def make_pca(self, input_tsv_file, output_tsv_file, output_html):
        mktstall_html = PcaMaker()
        mktstall_html.convert_table(input_tsv_file, output_tsv_file)
        #mktstall_html.create_pca(output_tsv_file, output_html)

    def process_image_labels(self):
        """
        Function: Process each image and extracts and assigns its label.
        """
        for img in self.images:
            img.extract_image_label()

    def process_image_rulers(self):
        """
        Function: Process each image and extracts the ruler and finds pixels/cm
        """
        for PeaImage in self.images:
            PeaImage.extract_image_ruler()

    @staticmethod
    def get_directory_size(directory_path):
        """
        Function: Finds the size of the directory by walking through the directory structure
        :param directory_path:
        :return: total_size
        """
        total_size = 0
        for dir_path, dir_names, file_names in os.walk(directory_path):
            for f in file_names:
                fp = os.path.join(dir_path, f)
                total_size += os.path.getsize(fp)
        return total_size

    def count_files(self):
        """
        Function: Count number of files
        :return: total count of files
        """
        total_count = 0
        for dir_path, dir_names, file_names in os.walk(self.dir_path):
            for f in file_names:
                if not f.startswith("."):
                    total_count += 1
        return total_count

    def set_image_count(self, num_image_files):
        """
        Function: Sets the number of image files
        :param: num_image_files
        """
        self.image_count = num_image_files

    def get_image_count(self):
        """
        Function: Gets the number of image files
        :return: self.image_count
        """
        if self.image_count == "":
            total_count = 0
            for dir_path, dir_names, file_names in os.walk(self.dir_path):
                for f in file_names:
                    if not f.startswith("."):
                        if f.endswith(".jpg") or f.endswith(".jpeg"):
                            total_count += 1
            self.image_count = total_count
        return self.image_count

    def load_images(self):
        """
        Function: Commence image processing for all images in the collection
        :return:
        """
        self. images = self.convert_pdf_to_jpg(self.dir_path)
        # self.image_count =self.countjpgimagefromdir(self.dir_path)
        self.image_count = self.count_files(self.dir_path)
        # self.processlabels(self.images)
        self.process_image_labels(self.images)

