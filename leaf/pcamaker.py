from matplotlib.pyplot import savefig
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA as sklearnPCA
import pandas as pd
from parameters import Parameters
from configmaker import ConfigMaker


class PcaMaker:

    def __init__(self):
        self.config_file = ConfigMaker(Parameters.results + "/summary_output.config")

    #read in workfile
    def convert_table(self, input_tsv_file, output_tsv_file):
        with open(input_tsv_file) as f:
            workfile_list = f.read().splitlines()
        header = workfile_list[0]
        data = workfile_list[1:]
        f.close()

        # print header, tab, group
        fileforpca = open(output_tsv_file,"w")
        #TODO: remove centroid
        pcaheader = header + "\tGroup"
        each_column = pcaheader.split("\t")
        del each_column[10]
        pcaheader = "\t".join(each_column)
        fileforpca.write(pcaheader)
        fileforpca.write("\n")

        # for not header, get first element, splitby space, then tab, get correct element
        for i in data:
            accession = i.split("\t")[0]
            accession_line2 = accession.split()[1]
            group = accession_line2.split("_")[0]
            line_with_group = i + "\t" + group
            # remove centroid column 10
            each_column = line_with_group.split("\t")
            del each_column[10]
            pca_line = "\t".join(each_column)
            fileforpca.write(pca_line)
            fileforpca.write("\n")

        fileforpca.close()

    def create_pca(self, input_tsv_file_for_pca, output_html):
        df = pd.read_csv(
            filepath_or_buffer=input_tsv_file_for_pca,
            header=0,
            sep='\t')

        X = df.ix[:,1:24].values
        y = df.ix[:,23].values
        #WARNING OCCURANCE
        standardised_X = StandardScaler().fit_transform(X)
        sklearn_pca = sklearnPCA(n_components=2)
        Y_sklearn = sklearn_pca.fit_transform(standardised_X)

        traces = []

        factor_group = df['Group'].unique()
        print "The factors (groups) found: ", factor_group
        for name in factor_group:

            trace = Scatter(
                x=Y_sklearn[y==name,0],
                y=Y_sklearn[y==name,1],
                mode='markers',
                name=name,
                marker=Marker(
                    size=12,
                    line=Line(
                        color='rgba(217, 217, 217, 0.14)',
                        width=0.5),
                    opacity=0.8))
            traces.append(trace)
        data = Data(traces)
        layout = Layout(xaxis=XAxis(title='PC1', showline=False),
                        yaxis=YAxis(title='PC2', showline=False))
        fig = Figure(data=data, layout=layout)
        plot(fig, show_link=False, filename=output_html, auto_open=False)
        # add success for this process to the config
        #TODO: add pca
        #self.config_file.pca_output_config_file(output_html)

