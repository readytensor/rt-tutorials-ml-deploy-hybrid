## Introduction

This repository is part of a tutorial series on Ready Tensor, a web platform for AI developers and users. It is specifically referenced in the tutorial **ML deployment with Docker: The hybrid pattern**. The repo contains a containerized random forest binary classifier model built using SciKit-Learn. This repo provides training service and an inference service.

## Repository Contents

The `app/` folder in the repository contains the following key folders/sub-folders:

- `data_management/` will all files related to handling and preprocessing data.
- `inputs/` contains the input files related to the _titanic_ dataset.
- `outputs/` is a folder to save model artifacts and other result files. Within this folder:
  - `artifacts/` is location to save model artifacts (i.e. the saved model including the trained preprocessing pipeline)
  - `outputs/` is used to contain the predictions or other results files (functionality not included in this repo)

## Usage to run the scripts

- Create your virtual environment and install dependencies listed in `requirements.txt`.
- Place the following 3 input files in the path `./app/inputs/`:
  - Train data, which must be a CSV file.
  - Test data, which must be a CSV file.
  - The schema file in JSON format. The schema conforms to Ready Tensor specification for the **Binary Classification-Base** category.
- Update the file paths in the `paths.py` file in `./app/`.
- Run the script `train.py` to train the random forest classifier model. This will save the model artifacts, including the preprocessing pipeline and label encoder, in the path `./app/outputs/artifacts/`.
- Run the script `test.py` to run test predictions using the trained model. This script will load the artifacts and create and save the predictions in a file called `predictions.csv` in the path `./app/outputs/predictions/`.
- Run the script `serve.py` to start the inference service, which can be queried using the `/ping` and `/infer` endpoints. The web service runs on port 8080.

## Usage with Docker

- Build the image. You can use the following command:

`docker build -t classifier_img .`

Here `classifier_img` is the name given to the container.

- Run the container and start the sevice. Use the `-p` flag to map a port on local host to the port 8080 in the container. You can use the following command:

`docker run -it -p 8080:8080 --name classifier classifier_img`

- You can do a health check on the GET endpoint `/ping` as follows:

```bash
curl http://localhost:8080/ping
```

A response code of 200 indicates the service is healthy.

- To get inference, hit the POST endpoint `/infer` as follows:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
  "instances": [
    {
      "PassengerId": "879",
      "Pclass": 3,
      "Name": "Laleff, Mr. Kristo",
      "Sex": "male",
      "Age": null,
      "SibSp": 0,
      "Parch": 0,
      "Ticket": "349217",
      "Fare": 7.8958,
      "Cabin": null,
      "Embarked": "S"
    }
  ]
}' http://localhost:8080/infer
```

You will receive a response as follows:

```json
{
  "status": "success",
  "message": null,
  "predictions": [
    {
      "id": "879",
      "label": "0",
      "probabilities": {
        "0": 0.9913,
        "1": 0.0087
      }
    }
  ]
}
```

## Requirements

The code requires Python 3 and the following libraries:

```makefile
fastapi==0.70.0
uvicorn==0.15.0
pydantic==1.8.2
pandas==1.5.5
numpy==1.19.5
scikit-learn==1.0
feature-engine==1.1.1
```

These packages can be installed by running the following command:

```python
pip install -r requirements.txt
```
