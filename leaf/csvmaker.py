class CsvMaker:

    def __init__(self):
        self.images = []

    def make_csv(self, out_dir, images):

        f_csv = open(out_dir + "/workfile.tsv", "w")
        print "making csv file at " + out_dir + "/workfile.tsv"
        header = "Accession\t" \
                 "pixelsPerCM\t" \
                 "Length\t" \
                 "Length_cm\t" \
                 "Width\t" \
                 "Width_cm\t" \
                 "Area\t" \
                 "Area_cm2\t" \
                 "Perimeter\t" \
                 "Perimeter_cm\t" \
                 "Centroid\t" \
                 "AspectRatio\t" \
                 "Roundness\t" \
                 "Compactness\t" \
                 "Rectangularity\t" \
                 "Perimeter Ratio of Length\t" \
                 "Perimeter Ratio of Length and Width\t" \
                 "Perimeter Convexity\t" \
                 "Area Convexity\t" \
                 "Area Ratio of Convexity\t" \
                 "Equivalent Diameter\t" \
                 "Equivalent Diameter cm\t" \
                 "Serrated\t" \
                 "NumberofTeeth"
        f_csv.write(header)
        f_csv.write("\n")

        for PeaImage in images:
            print "your pea image in self.images"
            print PeaImage.csv_string
            f_csv.write(PeaImage.csv_string)
            f_csv.write("\n")
        f_csv.close()
