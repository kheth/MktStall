import os
from seed import seed
from parameters import Parameters
import pandas as pd
class seedimagecollection:
    def __init__(self):
        self.collection = []
        self.summarycsv = []

    def getcollection(self, input_directory):
        for root, dir, files in os.walk(input_directory):
            for f in files:
                if "DS_Store" not in f:
                    self.collection.append((os.path.join(root, f)))
        return self.collection

    def analysecollection(self, collection):
        summaryfile = open(Parameters.results + "/tables/workfile.csv", "w")
        workfile_summary_header = "image_name" + "," + \
                          "numberofseeds" + "," + \
                          "area_mean_pix" + "," + \
                          "eqd_mean_pix" + "," + \
                          "perimeter_mean_pix" + "," + \
                          "mean_max_mins" + "," + \
                          "pix_per_cm" + "," + \
                          "area_mean_cm" + "," + \
                          "eqd_mean_cm" + "," + \
                          "perimeter_mean_cm" + "," \
                          "ecc_mean" + "\n"
        summaryfile.write(workfile_summary_header)
        for i in collection:
            test = seed(i)  # get an instance of the class
            accession_csv = test.seed_analyse()
            summaryfile.write(accession_csv)
        summaryfile.close()

    def appendsummaryconfig(self, results_directory):
        accession_config_list = []
        for root, dir, files in os.walk(results_directory):

            for f in files:
                if f != "workfile.csv.config":
                    if f.endswith("config"):
                        accession_config_list.append(root + "/" + f)

        for accession_config in accession_config_list:
            print accession_config
            accession_config_to_append = open(accession_config, "a")
            summary_file = open(results_directory + "/" + "workfile.csv.config","r")
            accession_config_to_append.write(summary_file.read())
            summary_file.close()
            accession_config_to_append.close()



