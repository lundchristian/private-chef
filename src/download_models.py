"""
This script downloads the model from the GPT4All API and saves it to the models
directory.

The docker image should be built with the phi-3-mini-4k-instruct.Q4_0.gguf model,
meaning that it shouldn't be necessary to run this script.

However, if you want to build the docker image from scratch, or with a different
model, you can run this script to download the model.
"""

from gpt4all import GPT4All

PATH = "models/"
MODEL_NAME = "Phi-3-mini-4k-instruct.Q4_0.gguf"

_ = GPT4All(
    model_name=MODEL_NAME,  # full model name with .gguf extension
    model_path=PATH,  # path to model directory
    device="cpu",  # device to run model on, only "cpu" is supported
    allow_download=True,  # allow initial download
)
