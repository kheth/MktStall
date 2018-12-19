from parameters import Parameters
import os
from pylab import *
import scipy
import cv2
import matplotlib.image as mpimg
from skimage.filters.rank import otsu
from skimage.filters import gaussian
from skimage.morphology import disk
import skimage as skimg
import parameters
from htmlmaker import HtmlMaker
from seed import seed
from seedimagecollection import seedimagecollection


class MktStall:

    TMP_DIR = "/Users/csy06dmu/Documents/bitbucket_repos/mktstall_repo_seed/tmp"

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
        collection = seedimagecollection()

        collection.analysecollection(collection.getcollection(Parameters.input))

        summary_file = Parameters.results + '/tables/workfile.csv'
        html_summary_file = HtmlMaker(summary_file)


        html_summary_file.summary_table_maker(summary_file)

        #html_summary_file.summary_perimeter_pixel_maker()
        #html_summary_file.summary_area_pixel_maker()
        #html_summary_file.summary_eqd_pixel_maker()
        #html_summary_file.summary_numberofseeds_pixel_maker()

        collection.appendsummaryconfig(Parameters.results)

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
