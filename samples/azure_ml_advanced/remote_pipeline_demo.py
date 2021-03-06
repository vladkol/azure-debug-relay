# a file to test pipeline debugging things
import argparse
from publish_pipeline import create_and_publish_pipeline


def main():
    """
    CLI entry point
    """
    published_pipeline, aml_workspace = create_and_publish_pipeline()

    experiment_name = "debug_experiment"

    parser = argparse.ArgumentParser()
    parser.add_argument("--is-debug", type=bool, required=False, default=False)
    parser.add_argument("--debug-relay-connection-name",
                        type=str, required=False, default="")
    options, _ = parser.parse_known_args()

    pipeline_parameters = {
        "is_debug": options.is_debug
        }
    if options.is_debug:
        if options.debug_relay_connection_name == "":
            raise ValueError("Hybrid connection name cannot be empty!")

        pipeline_parameters.update({
            "debug_relay_connection_name": options.debug_relay_connection_name
            })

    published_pipeline.submit(workspace=aml_workspace, experiment_name=experiment_name,
                              pipeline_parameters=pipeline_parameters,
                              continue_on_step_failure=True)


if __name__ == '__main__':
    main()
