from azureml.core import Experiment, ScriptRunConfig, Environment

# Custom
from azure_ml_workspace.workspace import (
    workspace, maybe_create_compute_instances)

compute_instance, cpu_cluster = maybe_create_compute_instances()


def hello_world_experiment():
    experiment = Experiment(workspace=workspace, name='test-experiment-01')

    config = ScriptRunConfig(
        source_directory='./azure_ml_experiment/src',
        script='train.py',
        compute_target=cpu_cluster.name
    )

    run = experiment.submit(config)
    aml_url = run.get_portal_url()
    print(aml_url)


def pytorch_model_experiment():
    experiment = Experiment(
        workspace=workspace,
        name='test-experiment-02-pytorch'
    )
    config = ScriptRunConfig(
        source_directory='./azure_ml_experiment/src',
        script='pytorch_train.py',
        compute_target=cpu_cluster.name)

    # set up pytorch environment
    env = Environment.from_conda_specification(
        name='pytorch-env',
        file_path='./azure_ml_experiment/src/pytorch-env.yml'
    )
    config.run_config.environment = env

    run = experiment.submit(config)

    aml_url = run.get_portal_url()
    print(aml_url)


if __name__ == "__main__":
    pytorch_model_experiment()