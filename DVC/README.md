[![DVC logo](https://dvc.org/img/logo-github-readme.png)](https://dvc.org)

[Website](https://dvc.org)
• [Docs](https://dvc.org/doc)
• [Blog](http://blog.dataversioncontrol.com)
• [Tutorial](https://dvc.org/doc/get-started)
• [Related Technologies](https://dvc.org/doc/user-guide/related-technologies)
• [How DVC works](#how-dvc-works)
• [VS Code Extension](#visual-studio-code-extension)
• [Installation](#installation)
• [Contributing](#contributing)
• [Community and Support](#community-and-support)

![CI](https://github.com/iterative/dvc/workflows/Tests/badge.svg?branch=main)
![Python Version](https://img.shields.io/pypi/pyversions/dvc)
![Coverage](https://codecov.io/gh/iterative/dvc/branch/main/graph/badge.svg)
[![VS Code](https://img.shields.io/visual-studio-marketplace/v/Iterative.dvc?color=blue&label=VSCode&logo=visualstudiocode&logoColor=blue)](https://marketplace.visualstudio.com/items?itemName=Iterative.dvc)
[![DOI](https://img.shields.io/badge/DOI-10.5281/zenodo.3677553-blue.svg)](https://doi.org/10.5281/zenodo.3677553)

---

**Data Version Control** or **DVC** is a command line tool and [VS Code Extension](https://marketplace.visualstudio.com/items?itemName=Iterative.dvc) to help you develop reproducible machine learning projects:

1. **Version** your data and models.
   Store them in your cloud storage but keep their version info in your Git repo.

2. **Iterate** fast with lightweight pipelines.
   When you make changes, only run the steps impacted by those changes.

3. **Track** experiments in your local Git repo (no servers needed).

4. **Compare** any data, code, parameters, model, or performance plots.

5. **Share** experiments and automatically reproduce anyone's experiment.

## Quick start

Please read our [Command Reference](https://dvc.org/doc/command-reference) for a complete list.

A common CLI workflow includes:

**Track data**
- `$ git add train.py params.yaml`
- `$ dvc add images/`

**Connect code and data**
- `$ dvc stage add -n featurize -d images/ -o features/ python featurize.py`
- `$ dvc stage add -n train -d features/ -d train.py -o model.p -M metrics.json python train.py`

**Make changes and experiment**
- `$ dvc exp run -n exp-baseline`
- `$ vi train.py`
- `$ dvc exp run -n exp-code-change`

**Compare and select experiments**
- `$ dvc exp show`
- `$ dvc exp apply exp-baseline`

**Share code**
- `$ git add .`
- `$ git commit -m 'The baseline model'`
- `$ git push`

**Share data and ML models**
- `$ dvc remote add myremote -d s3://mybucket/image_cnn`
- `$ dvc push`

## How DVC works

We encourage you to read our [Get Started](https://dvc.org/doc/get-started) docs to better understand what DVC does and how it can fit your scenarios.

The closest *analogies* to describe the main DVC features are these:

- **Git for data**: Store and share data artifacts (like Git-LFS but without a server) and models, connecting them with a Git repository. Data management meets GitOps!
- **Makefiles** for ML: Describes how data or model artifacts are built from other data and code in a standard format. Now you can version your data pipelines with Git.
- Local **experiment tracking**: Turn your machine into an ML experiment management platform, and collaborate with others using existing Git hosting (Github, Gitlab, etc.).

Git is employed as usual to store and version code (including DVC meta-files as placeholders for data). DVC [stores data and model files](https://dvc.org/doc/start/data-management) seamlessly in a cache outside of Git, while preserving almost the same user experience as if they were in the repo. To share and back up the *data cache*, DVC supports multiple remote storage platforms - any cloud (S3, Azure, Google Cloud, etc.) or on-premise network storage (via SSH, for example).

![Flowchart](https://dvc.org/img/flow.gif)

[DVC pipelines](https://dvc.org/doc/start/data-management/data-pipelines) (computational graphs) connect code and data together. They specify all steps required to produce a model: input dependencies including code, data, commands to run; and output information to be saved.

Last but not least, [DVC Experiment Versioning](https://dvc.org/doc/start/experiments) lets you prepare and run a large number of experiments. Their results can be filtered and compared based on hyperparameters and metrics, and visualized with multiple plots.

## Visual Studio Code Extension

![VS Code Extension Overview](https://raw.githubusercontent.com/iterative/vscode-dvc/main/extension/docs/overview.gif)

Note: You'll have to install core DVC on your system separately (as detailed below). The Extension will guide you if needed.

## Installation

There are several ways to install DVC: in VS Code; using `snap`, `choco`, `brew`, `conda`, `pip`; or with an OS-specific package. Full instructions are [available here](https://dvc.org/doc/get-started/install).

### Snapcraft (Linux)

```bash
snap install dvc --classic
