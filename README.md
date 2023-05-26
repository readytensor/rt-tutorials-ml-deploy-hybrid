## Introduction

This repository is a dockerized implementation of the random forest binary classifier. It is implemented in flexible way that it can be used with any binary classification dataset with with use of a data schema. The model includes a flexible preprocessing pipeline, the main random forest algorithm, hyperparameter-tuning using scikit-optimize, a SHAP explainer, and a FASTAPI inference service which provides endpoints for predictions and local explanations. Pydantic data validation is used for the schema, training and test files, as well as the inference request data. The repo also includes comprehensive set of unit and integration tests.

This repository is part of a tutorial series on Ready Tensor, a web platform for AI developers and users. The purpose of the tutorial series is to help AI developers create adaptable algorithm implementations that avoid hard-coding your logic to a specific dataset. This makes it easier to re-use your algorithms with new datasets in the future without requiring any code change.

## Repository Contents

```bash
binary_class_project/
├── examples/
│   ├── titanic_schema.json
│   ├── titanic_train.csv
│   └── titanic_test.csv
├── inputs/
│   ├── data/
│   │   ├── testing/
│   │   └── training/
│   └── schema/
├── model/
│   └── artifacts/
├── outputs/
│   ├── hpt_outputs/
│   ├── logs/
│   └── predictions/
├── src/
│   ├── config/
│   │   ├── default_hyperparameters.json
│   │   ├── hpt.json
│   │   ├── model_config.json
│   │   ├── paths.py
│   │   └── preprocessing.json
│   ├── data_models/
│   │   ├── data_validator.py
│   │   ├── infer_request_model.py
│   │   └── schema_validator.py
│   ├── hyperparameter_tuning/
│   │   ├── __init__.json
│   │   └── tuner.py
│   ├── prediction/
│   │   ├── __init__.json
│   │   └── predictor_model.py
│   ├── preprocessing/
│   │   ├── custom_transformers.py
│   │   ├── pipeline.py
│   │   ├── preprocess.py
│   │   └── target_encoder.py
│   ├── schema/
│   │   └── data_schema.py
│   ├── xai/
│   │   ├── __init__.json
│   │   └── explainer.py
│   ├── logger.py
│   ├── predict.py
│   ├── serve.py
│   ├── serve_utils.py
│   ├── train.py
│   └── utils.py
├── tests/
│   ├── <mirrors `/src` structure ...>
│   ...
│   ...
│   └── test_utils.py
├── tmp/
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

- **`/examples`**: This directory contains example files for the titanic dataset. Three files are included: `titanic_schema.json`, `titanic_train.csv` and `titanic_test.csv`. You can place these files in the `inputs/schema`, `inputs/data/training` and `inputs/data/testing` folders, respectively.
- **`/inputs`**: This directory contains all the input files for your project, including the data and schema files. The data is further divided into testing and training subsets.
- **`/model/artifacts`**: This directory is used to store the model artifacts, such as trained models and their parameters.
- **`/outputs`**: The outputs directory contains all output files, including the prediction results, logs, and hyperparameter tuning outputs.
- **`/src`**: This directory holds the source code for the project. It is further divided into various subdirectories such as `config` for configuration files, `data_models` for data models for input validation, `hyperparameter_tuning` for hyperparameter-tuning (HPT) related files, `prediction` for prediction model scripts, `preprocessing` for data preprocessing scripts, `schema` for schema scripts, and `xai` for explainable AI scripts.
- **`/src/data_models`**: This directory contains the data models for input validation. It is further divided into `data_validator.py` for data validation, `infer_request_model.py` for inference request validation, and `schema_validator.py` for schema validation.
- Within **`/src`** folder: We have the following main scripts:
  - **`logger.py`**: This script contains the centralized logger setup for the project. It is used the `train.py`, `predict.py` and `serve.py` scripts. Logging is stored in the path `./app/outputs/logs/`.
  - **`predict.py`**: This script is used to run batch predictions using the trained model. It loads the artifacts and creates and saves the predictions in a file called `predictions.csv` in the path `./app/outputs/predictions/`.
  - **`serve.py`**: This script is used to serve the model as a REST API. It loads the artifacts and creates a FastAPI server to serve the model.
  - **`serve_utils.py`**: This script contains utility functions used by the `serve.py` script.
  - **`train.py`**: This script is used to train the model. It loads the data, preprocesses it, trains the model, and saves the artifacts in the path `./app/outputs/artifacts/`. It also saves a SHAP explainer object in the path `./app/outputs/artifacts/`.
  - **`utils.py`**: This script contains utility functions used by the other scripts.
- **`/tests`**: This directory contains all the tests for the project. It mirrors the `src` directory structure for consistency. There is also a `test_resources` folder inside `/tests` which can contain any resources needed for the tests (e.g. sample data files).
- **`/tmp`**: This directory is used for storing temporary files which are not necessary to commit to the repository.
- **`.gitignore`**: This file specifies the files and folders that should be ignored by Git.
- **`LICENSE`**: This file contains the license for the project.
- **`README.md`**: This file contains the documentation for the project, explaining how to set it up and use it.
- **`requirements.txt`**: This file lists the dependencies for the project, making it easier to install all necessary packages.

## Usage (to run locally)

- Create your virtual environment and install dependencies listed in `requirements.txt`.
- Place the following 3 input files in the sub-directories in `./app/inputs/`:
  - Train data, which must be a CSV file, to be placed in `./app/inputs/data/training/`. File name can be any; extension must be ".csv".
  - Test data, which must be a CSV file, to be placed in `./app/inputs/data/testing/`. File name can be any; extension must be ".csv".
  - The schema file in JSON format , to be placed in `./app/inputs/data_config/`. The schema conforms to Ready Tensor specification for the **Binary Classification-Base** category. File name can be any; extension must be ".json".
- Run the script `train.py` to train the random forest classifier model. This will save the model artifacts, including the preprocessing pipeline and label encoder, in the path `./app/outputs/artifacts/`.
- Run the script `predict.py` to run batch predictions using the trained model. This script will load the artifacts and create and save the predictions in a file called `predictions.csv` in the path `./app/outputs/predictions/`.
- Run the script `serve.py` to start the inference service, which can be queried using the `/ping` and `/infer` endpoints. The service also provides local explanations for the predictions using the `/explain` endpoint.

## Usage with Docker

- Set up a bind mount
- Build the image. You can use the following command:

`docker build -t classifier_img .`

Here `classifier_img` is the name given to the container (you can choose any name).

- Run the container and start the sevice. Use the `-p` flag to map a port on local host to the port 8080 in the container. You can use the following command:

`docker run -it -p 8080:8080 --name classifier classifier_img`

## Requirements

The code requires Python 3 and the following libraries:

```makefile
fastapi==0.70.0
uvicorn==0.15.0
pydantic==1.8.2
pandas==1.5.2
numpy==1.20.3
scikit-learn==1.0
feature-engine==1.2.0
imbalanced-learn==0.8.1
scikit-optimize==0.9.0
httpx==0.24.0
shap==0.41.0
```

These packages can be installed by running the following command:

```python
pip install -r requirements.txt
```
