import sys

# gemd_tools_path = "/srv/hemi01-j01/gemd_tools"
sys.path.append("/srv/hemi01-j01/gemd_tools")
from workflow.folder_or_file import FolderOrFile
from workflow.TAMUWorkflow import TAMUWorkflow
from workflow.Workflow import Workflow
from utilities.tools import plot_graph
from utilities.gemd_modeller.gemd_modeller import GemdModeller
import os
import pathlib
from pathlib import Path


def main():
    # _file_path = pathlib.Path(__file__)
    # iteration_count = 2
    # iteration = "AAB"
    # source_folder = _file_path.parent.parent / "data/"
    # output_folder = _file_path.parent / "data/{}".format(iteration)
    # sample_data_folder = _file_path.parent.parent / "Sample Data/Iteration{}_{}".format(
    #     iteration_count, iteration
    # )

    # path = os.path.join(source_folder, iteration)
    # w_aab = TAMUWorkflow(
    #     path,
    #     output_folder=output_folder,
    #     iteration=iteration,
    #     sample_data_folder=sample_data_folder,
    # )
    # w_aab.testing_mode = True
    # w_aab.build_model()
    # w_aab.thin_dumps()

    p = "/srv/hemi01-j01/htmdec/birdshot/gemd/data/AAB/AAB01/VAM/A/thin_jsons"

    v = GemdModeller(p)
    assets_to_add = {'parameters': 1, 'conditions': 1, 'properties': 1, 'file_links': 1,'tags': 1 }
    run_graph = v.build_graph(add_separate_node=True, assets_to_add=assets_to_add)

    GemdModeller.save_graph(
        dest="/srv/hemi01-j01/tmp", G=run_graph, name="birdshot_run_graph_tmp"
    )

    spec_graph = v.build_graph(
        obj_state="spec", add_separate_node=True, assets_to_add=assets_to_add
    )
    GemdModeller.save_graph(
        dest="/srv/hemi01-j01/tmp", G=spec_graph, name="birdshot_spec_graph_tmp"
    )


if __name__ == "__main__":
    main()
