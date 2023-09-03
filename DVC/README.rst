|Banner|


|CI| |Python Version| |Coverage| |VS Code| |DOI|

|PyPI| |PyPI Downloads| |Packages| |Brew| |Conda| |Choco| |Snap|

|

**Data Version Control** or **DVC** is a command line tool and `VS Code Extension`_ to help you develop reproducible machine learning projects:

#. **Version** your data and models.
   Store them in your cloud storage but keep their version info in your Git repo.

#. **Iterate** fast with lightweight pipelines.
   When you make changes, only run the steps impacted by those changes.

#. **Track** experiments in your local Git repo (no servers needed).

#. **Compare** any data, code, parameters, model, or performance plots.

#. **Share** experiments and automatically reproduce anyone's experiment.

Quick start
===========

    Please read our `Command Reference <https://dvc.org/doc/command-reference>`_ for a complete list.

A common CLI workflow includes:


+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Task                              | Terminal                                                                                           |
+===================================+====================================================================================================+
| Track data                        | | ``$ git add train.py params.yaml``                                                               |
|                                   | | ``$ dvc add images/``                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Connect code and data             | | ``$ dvc stage add -n featurize -d images/ -o features/ python featurize.py``                     |
|                                   | | ``$ dvc stage add -n train -d features/ -d train.py -o model.p -M metrics.json python train.py`` |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Make changes and experiment       | | ``$ dvc exp run -n exp-baseline``                                                                |
|                                   | | ``$ vi train.py``                                                                                |
|                                   | | ``$ dvc exp run -n exp-code-change``                                                             |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Compare and select experiments    | | ``$ dvc exp show``                                                                               |
|                                   | | ``$ dvc exp apply exp-baseline``                                                                 |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Share code                        | | ``$ git add .``                                                                                  |
|                                   | | ``$ git commit -m 'The baseline model'``                                                         |
|                                   | | ``$ git push``                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Share data and ML models          | | ``$ dvc remote add myremote -d s3://mybucket/image_cnn``                                         |
|                                   | | ``$ dvc push``                                                                                   |
+-----------------------------------+----------------------------------------------------------------------------------------------------+

How DVC works
=============

    We encourage you to read our `Get Started
    <https://dvc.org/doc/get-started>`_ docs to better understand what DVC
    does and how it can fit your scenarios.

The closest *analogies* to describe the main DVC features are these:

#. **Git for data**: Store and share data artifacts (like Git-LFS but without a server) and models, connecting them with a Git repository. Data management meets GitOps!
#. **Makefiles** for ML: Describes how data or model artifacts are built from other data and code in a standard format. Now you can version your data pipelines with Git.
#. Local **experiment tracking**: Turn your machine into an ML experiment management platform, and collaborate with others using existing Git hosting (Github, Gitlab, etc.).

Git is employed as usual to store and version code (including DVC meta-files as placeholders for data).
DVC `stores data and model files <https://dvc.org/doc/start/data-management>`_ seamlessly in a cache outside of Git, while preserving almost the same user experience as if they were in the repo.
To share and back up the *data cache*, DVC supports multiple remote storage platforms - any cloud (S3, Azure, Google Cloud, etc.) or on-premise network storage (via SSH, for example).

|Flowchart|

`DVC pipelines <https://dvc.org/doc/start/data-management/data-pipelines>`_ (computational graphs) connect code and data together.
They specify all steps required to produce a model: input dependencies including code, data, commands to run; and output information to be saved.

Last but not least, `DVC Experiment Versioning <https://dvc.org/doc/start/experiments>`_ lets you prepare and run a large number of experiments.
Their results can be filtered and compared based on hyperparameters and metrics, and visualized with multiple plots.


Installation
============

There are several ways to install DVC: in VS Code; using ``snap``, ``choco``, ``brew``, ``conda``, ``pip``; or with an OS-specific package.
Full instructions are `available here <https://dvc.org/doc/get-started/install>`_.

Snapcraft (Linux)
-----------------

|Snap|

.. code-block:: bash

   snap install dvc --classic

This corresponds to the latest tagged release.
Add ``--beta`` for the latest tagged release candidate, or ``--edge`` for the latest ``main`` version.

Chocolatey (Windows)
--------------------

|Choco|

.. code-block:: bash

   choco install dvc

Brew (mac OS)
-------------

|Brew|

.. code-block:: bash

   brew install dvc

PyPI (Python)
-------------

|PyPI|

.. code-block:: bash

   pip install dvc

Depending on the remote storage type you plan to use to keep and share your data, you might need to specify one of the optional dependencies: ``s3``, ``gs``, ``azure``, ``oss``, ``ssh``. Or ``all`` to include them all.
The command should look like this: ``pip install 'dvc[s3]'`` (in this case AWS S3 dependencies such as ``boto3`` will be installed automatically).

To install the development version, run:

.. code-block:: bash

   pip install git+git://github.com/iterative/dvc

Package (Platform-specific)
---------------------------

|Packages|

Self-contained packages for Linux, Windows, and Mac are available.
The latest version of the packages can be found on the GitHub `releases page <https://github.com/iterative/dvc/releases>`_.

Ubuntu / Debian (deb)
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

   sudo wget https://dvc.org/deb/dvc.list -O /etc/apt/sources.list.d/dvc.list
   wget -qO - https://dvc.org/deb/iterative.asc | sudo apt-key add -
   sudo apt update
   sudo apt install dvc

Fedora / CentOS (rpm)
^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

   sudo wget https://dvc.org/rpm/dvc.repo -O /etc/yum.repos.d/dvc.repo
   sudo rpm --import https://dvc.org/rpm/iterative.asc
   sudo yum update
   sudo yum install dvc


DVC with S3 Remote Storage
=========================

Prerequisites
-------------

Before getting started, ensure you have the following prerequisites in place:

1. Install DVC by following the instructions [here](https://dvc.org/doc/get-started/install).
2. Set up an AWS account at [AWS](https://aws.amazon.com/) and configure AWS CLI with your access credentials.

Make sure you are connected to the S3 bucket:

.. code:: python

   import boto3

   AWS_ACCESS_KEY_ID = "Your_AWS_ACCESS_KEY_ID"
   AWS_SECRET_ACCESS_KEY = "Your_AWS_SECRET_ACCESS_KEY"
   S3_BUCKET_NAME = 'Your_S3_Bucket_Name'

   def s3_client():
       return boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

   def test_s3_bucket_exists(s3_client):
       # Check if the S3 bucket exists
       try:
           s3_client.head_bucket(Bucket=S3_BUCKET_NAME)
           print(f"S3 Bucket '{S3_BUCKET_NAME}' exists.")
       except Exception as e:
           print(f"Error: {e}")
           print(f"S3 Bucket '{S3_BUCKET_NAME}' does not exist.")

   def test_s3_bucket_access(s3_client):
       # Check if you can list objects in the S3 bucket
       try:
           response = s3_client.list_objects_v2(Bucket=S3_BUCKET_NAME)
           if 'Contents' in response:
               print(f"Successfully accessed objects in S3 Bucket '{S3_BUCKET_NAME}'.")
           else:
               print(f"No objects found in S3 Bucket '{S3_BUCKET_NAME}'.")
       except Exception as e:
           print(f"Error: {e}")

   if __name__ == "__main__":
       s3 = s3_client()
       test_s3_bucket_exists(s3)
       test_s3_bucket_access(s3)

Getting Started
---------------

### Initialize a DVC Project

To begin using DVC, initialize a new project:

.. code:: shell

   mkdir my-dvc-project
   cd my-dvc-project
   dvc init

### Configure S3 as a Remote Storage

Now, configure S3 as the remote storage for your DVC project:

.. code:: shell

   dvc remote add -d my-s3-remote s3://my-bucket-name/path/to/data

Replace `my-s3-remote` with a suitable name for your remote and `s3://my-bucket-name/path/to/data` with your actual S3 bucket path.

### Add Data to DVC

Add your data files to the DVC project. This doesn't store the data directly in Git but tracks it using DVC:

.. code:: shell

   dvc add data/my_data.csv

### Commit Changes

Commit the changes made by DVC to your Git repository:

.. code:: shell

   git add .dvc .gitignore data/my_data.csv.dvc
   git commit -m "Add data tracking with DVC"

### Push Data to S3

Push your data to the S3 remote storage:

.. code:: shell

   dvc push

Scheduing Data Extraction using Lambda Functions and CloudWatch Events
======================================================================

1 - First, we Create a Lambda function (Handler Function) : 

.. code:: python
    

    def lambda_handler(event, context):
        base_url = event["base_url"]
        query = event["Query"]

        # ... params for file saving and total pages to extract 

        try:
            data_to_store = ""

            for page in range(1, total_pages + 1):
                params = {
                   # ... params to extract the data 
                }

                response = requests.get(base_url, params=params, timeout=10)
                response.raise_for_status()

                doc = BeautifulSoup(response.text, "html.parser")

                links = [a['href'] for a in doc.find_all('a', href=True) if 'https://arxiv.org/abs/' in a['href']]

                for link in links:
                    try:
                        response = requests.get(link, timeout=10)
                        response.raise_for_status()

                        doc = BeautifulSoup(response.text, "html.parser")

                        title = doc.find('h1', class_='title mathjax').text.strip()
                        abstract = doc.find('blockquote', class_='abstract mathjax').text.strip()

                        question = f"Q: Can you give me an abstract for my research paper with the {title}?"
                        answer = f"A: {abstract}"

                        data_to_store += question + "\n" + answer + "\n\n"
                        print(f"Collected data for {title}")

                    except Exception as e:
                        print(f"Error scraping link {link}: {e}")

            if store_data_in_s3(bucket_name, file_name, data_to_store):
                print(f"Stored final data in S3: s3://{bucket_name}/{file_name}")

        except Exception as e:
            print(f"An error occurred: {e}")

for each Lambda run event : 
.. code:: json 

       {
         event: "https://arxiv.org/search/",
         Query: "DATA SCIENCE OR MACHINE LEARNING"
       }

2 - We Schedule the event execution using CloudWatch Events service : 




.. |Banner| image:: https://dvc.org/img/logo-github-readme.png
   :target: https://dvc.org
   :alt: DVC logo

.. |VS Code Extension Overview| image:: https://raw.githubusercontent.com/iterative/vscode-dvc/main/extension/docs/overview.gif
   :alt: DVC Extension for VS Code

.. |CI| image:: https://github.com/iterative/dvc/workflows/Tests/badge.svg?branch=main
   :target: https://github.com/iterative/dvc/actions
   :alt: GHA Tests

.. |Maintainability| image:: https://codeclimate.com/github/iterative/dvc/badges/gpa.svg
   :target: https://codeclimate.com/github/iterative/dvc
   :alt: Code Climate

.. |Python Version| image:: https://img.shields.io/pypi/pyversions/dvc
   :target: https://pypi.org/project/dvc
   :alt: Python Version

.. |Coverage| image:: https://codecov.io/gh/iterative/dvc/branch/main/graph/badge.svg
   :target: https://codecov.io/gh/iterative/dvc
   :alt: Codecov

.. |Snap| image:: https://img.shields.io/badge/snap-install-82BEA0.svg?logo=snapcraft
   :target: https://snapcraft.io/dvc
   :alt: Snapcraft

.. |Choco| image:: https://img.shields.io/chocolatey/v/dvc?label=choco
   :target: https://chocolatey.org/packages/dvc
   :alt: Chocolatey

.. |Brew| image:: https://img.shields.io/homebrew/v/dvc?label=brew
   :target: https://formulae.brew.sh/formula/dvc
   :alt: Homebrew

.. |Conda| image:: https://img.shields.io/conda/v/conda-forge/dvc.svg?label=conda&logo=conda-forge
   :target: https://anaconda.org/conda-forge/dvc
   :alt: Conda-forge

.. |PyPI| image:: https://img.shields.io/pypi/v/dvc.svg?label=pip&logo=PyPI&logoColor=white
   :target: https://pypi.org/project/dvc
   :alt: PyPI

.. |PyPI Downloads| image:: https://img.shields.io/pypi/dm/dvc.svg?color=blue&label=Downloads&logo=pypi&logoColor=gold
   :target: https://pypi.org/project/dvc
   :alt: PyPI Downloads

.. |Packages| image:: https://img.shields.io/badge/deb|pkg|rpm|exe-blue
   :target: https://dvc.org/doc/install
   :alt: deb|pkg|rpm|exe

.. |DOI| image:: https://img.shields.io/badge/DOI-10.5281/zenodo.3677553-blue.svg
   :target: https://doi.org/10.5281/zenodo.3677553
   :alt: DOI

.. |Flowchart| image:: https://dvc.org/img/flow.gif
   :target: https://dvc.org/img/flow.gif
   :alt: how_dvc_works

.. |Contribs| image:: https://contrib.rocks/image?repo=iterative/dvc
   :target: https://github.com/iterative/dvc/graphs/contributors
   :alt: Contributors

.. |VS Code| image:: https://img.shields.io/visual-studio-marketplace/v/Iterative.dvc?color=blue&label=VSCode&logo=visualstudiocode&logoColor=blue
   :target: https://marketplace.visualstudio.com/items?itemName=Iterative.dvc
   :alt: VS Code Extension
