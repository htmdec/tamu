import sys

gemd_tools_path = "/srv/hemi01-j01/gemd_tools"
sys.path.append(gemd_tools_path)
from workflow.Folder import Folder
from workflow.TAMUWorkflow import TAMUWorkflow
from workflow.Workflow import Workflow
from utilities.tools import plot_graph
import os
import pathlib
from pathlib import Path


def main():
    _file_path = pathlib.Path(__file__)
    iteration_count = 2
    iteration = "AAB"
    source_folder = _file_path.parent.parent / "data/"
    output_folder = _file_path.parent / "data/{}".format(iteration)
    sample_data_folder = _file_path.parent.parent / "Sample Data/Iteration{}_{}".format(
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
    # print(w_aab.displayable())
    w_aab.thin_dumps()

    plot_graph("/srv/hemi01-j01/htmdec/birdshot/gemd/data/AAB/AAB01/VAM/A/thin_jsons")
    plot_graph(
        "/srv/hemi01-j01/htmdec/birdshot/gemd/data/AAB/AAB01/VAM/A/thin_jsons",
        obj_state="spec",
    )


if __name__ == "__main__":
    main()
