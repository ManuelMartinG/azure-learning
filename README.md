# Azure Learning

Repository that contains Azure learnings, pocs, etc

## Connect to SSH Container

```bash
chmod 400 {}.pem
ssh azureuser@52.167.30.199 -p 50001 -i {}.pem
```


## Set up

1. Configure VS Code Azure and Azure Machine Learning plugins.

2. Install requirements

```bash
pip install requirements.txt
```

## Workspace configuration

**How to create workspace compute instances and cluster**

```bash
python -m azure_ml_workspace.workspace
```

## Experiment

Following tutorial on https://github.com/MicrosoftDocs/azure-docs/blob/master/articles/machine-learning/tutorial-1st-experiment-sdk-setup-local.md

**How to create an experiment**

```bash
python -m azure_ml_experiment.experiment
```
