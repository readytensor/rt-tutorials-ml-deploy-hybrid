import os

# Path to the current file's directory
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the parent directory
PARENT_DIR = os.path.dirname(CURRENT_DIR)

# Path to mounted volume called ml_vol
MOUNT_DIR = os.path.join(PARENT_DIR, "ml_vol")

# Path to inputs inside ml_vol
INPUT_DIR = os.path.join(MOUNT_DIR, "inputs")
# File paths for input schema file 
SCHEMA_DIR = os.path.join(INPUT_DIR, "data_config")
# Path to data directory inside inputs directory
DATA_DIR = os.path.join(INPUT_DIR, "data")
# Path to training directory inside data directory
TRAIN_DIR = os.path.join(DATA_DIR, "training")
# Path to test directory inside data directory
TEST_DIR = os.path.join(DATA_DIR, "testing")

# Path to model directory inside ml_vol
MODEL_PATH = os.path.join(MOUNT_DIR, "model")
# Path to artifacts directory inside model directory
MODEL_ARTIFACTS_PATH = os.path.join(MODEL_PATH, "artifacts")

# Path to outputs inside ml_vol
OUTPUT_DIR = os.path.join(MOUNT_DIR, "outputs")
# Path to logs directory inside outputs directory
LOGS_DIR = os.path.join(OUTPUT_DIR, "logs")
# Path to testing outputs directory inside outputs directory
TEST_OUTPUTS_DIR = os.path.join(OUTPUT_DIR, "testing_outputs")
# Name of the file containing the predictions
PREDICTIONS_FILE_NAME = "predictions.csv"
