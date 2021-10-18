"""
    Global configuration.
"""

#----------------------------------------------------------------------------
# Images

IMAGE_DIR = 'images' # Dir to store fake or real face
MAX_FAKE_IMAGE_ID = 12 # random id would generated from 1 to max_image_id
IMAGE_FORMAT = '.jpg'

#----------------------------------------------------------------------------

#----------------------------------------------------------------------------
# Recognition Model

MODEL_PATH = './model/grayscale_densenet.h5' # path to load model
INPUT_SIZE = (224, 224, 1)
#----------------------------------------------------------------------------
