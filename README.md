# Dog VS Cat Image Classification (DL Project 1)

![Status](https://img.shields.io/badge/status-experimental-orange)
![Python](https://img.shields.io/badge/python-3.11-blue)

Short Streamlit demo that classifies uploaded images as either a dog or a cat using a pretrained TensorFlow SavedModel.

**Key features**
- Simple Streamlit web UI for image upload and prediction
- Uses a TensorFlow SavedModel located in the `pretrained model/` folder
- Small, dependency-driven setup (see `requirements.txt`)

## Why this project is useful

- Fast way to demonstrate a binary image classifier in a web UI
- Useful starter template for deploying small ML demos locally or on lightweight cloud services
- Easy to adapt to other binary tasks by replacing the SavedModel

## Getting started

### Prerequisites

- Python 3.11 (see `runtime.txt`)
- Git (to clone the repository)
- Optional: GPU and appropriate CUDA/cuDNN if using a GPU build of TensorFlow

On Linux you may need system packages listed in `packages.txt` (for example, `libgl1` for OpenCV).

### Install (recommended)

1. Create and activate a virtual environment

Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux / macOS

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install Python dependencies

```bash
pip install -r requirements.txt
```

3. Ensure the pretrained model is present

The app expects a TensorFlow SavedModel under the folder `pretrained model/` (this repository includes a `pretrained model/` directory with `saved_model.pb` and `variables/`). Do not rename the folder unless you update the path in `dog_cat_web_app.py`.

### Run the app

```bash
streamlit run dog_cat_web_app.py
```

Open the URL printed by Streamlit (usually `http://localhost:8501`) and upload an image (jpg, png, jpeg). The app will resize the image to 224×224 and run a prediction. Results show the predicted label and a basic confidence check.

## Usage notes and tips

- The model is loaded from `pretrained model` using `tensorflow.keras.models.load_model`. If you replace the model, make sure it accepts 224×224×3 input and that the labels are ordered `["Cat", "Dog"]`.
- The app treats predictions with confidence below 0.6 as unclear and prompts for a different image.
- If you encounter OpenCV or image-display issues on Linux, install system package `libgl1` (listed in `packages.txt`).

## Project structure (important files)

- `dog_cat_web_app.py` — Streamlit app entrypoint
- `pretrained model/` — SavedModel used by the app
- `requirements.txt` — Python dependencies
- `packages.txt` — System packages (Linux)
- `runtime.txt` — Python runtime (3.11)

## Where to get help

- Open an issue in this repository for bugs or enhancement requests.
- For Streamlit usage questions consult the Streamlit docs: https://docs.streamlit.io
- For TensorFlow model compatibility see: https://www.tensorflow.org/guide/saved_model

## Maintainers & contributing

Maintainers: see `CONTRIBUTING.md` for the current maintainers and contribution process.

Contributions are welcome — please read `CONTRIBUTING.md` before opening issues or pull requests.

## License

This repository does not include a license file. Add a `LICENSE` file if you wish to change the licensing.
