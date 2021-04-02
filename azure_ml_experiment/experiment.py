from azureml.core import Experiment, ScriptRunConfig

# Custom
from azure_ml_workspace.workspace import (
    workspace, maybe_create_compute_instances)


compute_instance, cpu_cluster = maybe_create_compute_instances()
experiment = Experiment(workspace=workspace, name='test-experiment-01')

config = ScriptRunConfig(
    source_directory='./azure_ml_experiment/src',
    script='train.py',
    compute_target=cpu_cluster.name
)

run = experiment.submit(config)
aml_url = run.get_portal_url()
print(aml_url)