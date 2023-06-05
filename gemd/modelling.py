import sys

gemd_tools_path = "/srv/hemi01-j01/gemd_tools"
sys.path.append(gemd_tools_path)
from workflow.Folder import Folder
from workflow.TAMUWorkflow import TAMUWorkflow
from workflow.Workflow import Workflow
from utilities.tools import plot_graph
import os
from pathlib import Path


def main():
    iteration_count = 2
    iteration = "AAB"
    source_folder = "../data/"
    output_folder = "data/{}".format(iteration)
    sample_data_folder = "../Sample Data/Iteration{}_{}".format(
        iteration_count, iteration
    )
    path = os.path.join(source_folder, iteration)
    w_aab = TAMUWorkflow(
        path,
        output_folder=output_folder,
        iteration=iteration,
        sample_data_folder=sample_data_folder,
    )
    w_aab.testing_mode = True
    w_aab.build_model()


if __name__ == "__main__":
    main()
