import os
import parameters
import warnings
from peaimagecollection import PeaImageCollection
from peautils import PeaUtils


class MktStall:

    INPUT = ""
    RESULTS = ""
    TMP_DIR = ""

    def __init__(self):
        print "Welcome to MktStall v1.01."
        self.DEBUG = False
        self.VERBOSE = False
        self.raw_collection = ""
        self.acceptable_label_collection = ""
        self.unacceptable_label_collection = ""
        self.tmp_working_directory = ""
        self.config_file = ""

    def start(self):
        """
        Main Logic for the entry of MktStall
        :return:
        """
        #########################
        # WARNINGS BEING SUPRESSED
        #########################
        warnings.filterwarnings("ignore", message="Possible precision loss when converting from float64 to uint8")
        print "Starting MktStall.\n"
        self.tmp_working_directory = PeaUtils.copy_directory_structure(self.VERBOSE, self.INPUT, self.TMP_DIR)
        self.raw_collection = PeaImageCollection(self.tmp_working_directory, self.DEBUG, self.VERBOSE, self.config_file)
        print "Number of pdfs:\t", self.raw_collection.count_files()
        print "\nExtracting images from pdfs."
        self.raw_collection.convert_pdf_to_jpg()
        ################

        ################
        # print "\nExtracting labels from images."
        self.raw_collection.affirm_image_collection_is_portrait()
        self.raw_collection.process_image_labels()
        print "\nExtracting rulers from images."
        self.raw_collection.process_image_rulers()
        print "\nAnalysing images."
        self.raw_collection.analyse_images()
        self.raw_collection.make_csv(self.RESULTS + '/tables')
        self.raw_collection.make_html(self.RESULTS + '/html', self.config_file)
        self.raw_collection.make_pca(self.RESULTS + "/tables/workfile.tsv",
                                     self.RESULTS + "/tables/testforpca.tsv",
                                     self.RESULTS + "/html/pca.html")

    def main(self):
        """
        Usage: python ./MktStall.py arg1 [input] arg2 [results] arg3 [tmpdir] arg4 [debug] arg5 [verbose]
        :return:
        """
        ###############################################
        # KEEP ME FOR CMD LINE STAGE
        # for arg in sys.argv[1:]:
        # this is to take argvs from cmdline
        ###############################################
        p = parameters.Parameters()
        self.INPUT = p.input
        self.RESULTS = p.results
        self.TMP_DIR = p.tmp_dir
        #self.config_file = ConfigMaker(self.TMP_DIR)

        print self.INPUT
        print self.RESULTS
        print self.TMP_DIR

        if not os.path.exists(self.RESULTS):
            os.makedirs(self.RESULTS)
        if not os.path.exists(self.RESULTS + '/images'):
            os.makedirs(self.RESULTS + '/images')
        if not os.path.exists(self.RESULTS + '/html'):
            os.makedirs(self.RESULTS + '/html')
        if not os.path.exists(self.RESULTS + '/tables'):
            os.makedirs(self.RESULTS + '/tables')
        if not os.path.exists(self.RESULTS + '/worddoc'):
            os.makedirs(self.RESULTS + '/worddoc')

        self.start()


if __name__ == '__main__':
    mkt = MktStall()
    mkt.main()
