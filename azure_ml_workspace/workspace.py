from azureml.core import Workspace
from azureml.core.compute import ComputeInstance
from azureml.core.compute_target import ComputeTargetException
from azureml.core.compute import ComputeTarget, AmlCompute

from config import AzureMLConfig

az = AzureMLConfig()

# Set up Workspace
workspace = Workspace.get(
    name=az.workspace,
    subscription_id=az.subscription_id,
    resource_group=az.resource_group
)

compute_name = "ci{}".format(workspace._workspace_id)[:10]

# Get Compute Instance
try:
    instance = ComputeInstance(
        workspace=workspace,
        name=compute_name
    )
    print('Found existing instance, use it.')
except ComputeTargetException:
    compute_config = ComputeInstance.provisioning_configuration(
        vm_size='STANDARD_D1_V2',
        ssh_public_access=False,
    )
    instance = ComputeInstance.create(
        workspace,
        compute_name,
        compute_config
    )
    instance.wait_for_completion(show_output=True)

# Choose a name for your CPU cluster
cpu_cluster_name = "cpucluster"

# Verify that cluster does not exist already
try:
    cpu_cluster = ComputeTarget(
        workspace=workspace,
        name=cpu_cluster_name
    )
    print('Found existing cluster, use it.')
except ComputeTargetException:
    compute_config = AmlCompute.provisioning_configuration(
        vm_size='STANDARD_D1_V2',
        min_nodes=1,
        max_nodes=4)
    cpu_cluster = ComputeTarget.create(
        workspace,
        cpu_cluster_name,
        compute_config
    )

cpu_cluster.wait_for_completion(show_output=True)
