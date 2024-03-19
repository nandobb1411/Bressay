# BRESSAY Handwritten Text Recognition Project Documentation

## Overview

This project aims to participate in the ICDAR 2024 Competition, focusing on Handwritten Text Recognition in Brazilian Essays, utilizing the BRESSAY dataset. Our approach employs a Convolutional Recurrent Neural Network (CRNN) with Connectionist Temporal Classification (CTC) loss to effectively transcribe handwritten essays in Brazilian Portuguese.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Access to the BRESSAY dataset

### Installation

1. **Clone the Repository**

    Clone this repository to your local machine to get started with the project.

    ```sh
    git clone <repository_url>
    cd path/to/repository
    ```

2. **Create a Virtual Environment**

    It's recommended to create a virtual environment for this project to manage dependencies.

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Unix/macOS
    venv\Scripts\activate  # On Windows
    ```

3. **Install Dependencies**

    Install all required dependencies using the `requirements.txt` file provided.

    ```sh
    pip install -r requirements.txt
    ```

4. **Download and Prepare the Dataset**

    Download the BRESSAY dataset and prepare it according to the instructions provided by the dataset maintainers. Ensure you have the dataset structured as per the BRESSAY dataset documentation for optimal performance with our model.

## Project Structure

- `EDA.ipynb`: Jupyter notebook containing exploratory data analysis and model training steps.
- `requirements.txt`: File containing all necessary Python packages.
- `models/`: Directory where trained models are saved.
- `data/`: Directory containing the BRESSAY dataset, organized as per the dataset's documentation.

## Training the Model

To train the model, follow the steps outlined in the `EDA.ipynb` Jupyter notebook. This notebook guides you through the process of loading the dataset, preprocessing the images and annotations, defining the CRNN architecture, and finally training the model using CTC loss.

## Evaluation and Testing

After training, the notebook also provides instructions on evaluating the model's performance on the test set and visualizing the results to ensure the handwritten text is correctly transcribed.

## Terms of Use

Please adhere to the BRESSAY dataset's terms of usage for non-commercial research and teaching purposes only. Remember to cite their paper if you are publishing scientific work based on the dataset.

## Contact

For any issues or questions related to this project, refer to the contact details provided in the BRESSAY dataset documentation or directly reach out to the project contributors.

## Acknowledgements

Special thanks to the creators of the BRESSAY dataset and the ICDAR 2024 Competition for facilitating research in handwritten text recognition.
