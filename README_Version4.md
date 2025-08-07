# CNN Image Classifier (CIFAR-10)

A deep learning project that classifies images from the CIFAR-10 dataset using a Convolutional Neural Network (CNN) built with TensorFlow/Keras. The project demonstrates model training, evaluation, data augmentation, and transfer learning. Easily extensible to other datasets and architectures.

## Features

- End-to-end pipeline (data loading, preprocessing, training, evaluation)
- Baseline CNN architecture
- Data augmentation for improved generalization
- Transfer learning with a pre-trained ResNet model
- Training history visualization

## Requirements

- Python 3.7+
- tensorflow
- matplotlib
- numpy

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Jupyter notebook step by step:
   ```bash
   jupyter notebook cnn_image_classifier.ipynb
   ```

2. Or execute the Python scripts for each stage.

## Project Structure

- `cnn_image_classifier.ipynb` — Main notebook with all steps
- `src/` — Python scripts for modular use
- `models/` — Saved trained models
- `plots/` — Training plots and sample outputs

---

Feel free to open issues or pull requests for improvements!