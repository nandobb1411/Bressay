# BRESSAY: Brazilian Essays Dataset for Handwritten Text Recognition

## Overview

The BRESSAY dataset is part of the ICDAR 2024 Competition focusing on Handwritten Text Recognition in Brazilian Essays. It comprises images of handwritten essays in Brazilian Portuguese, offering a variety of challenges for optical character recognition models. The dataset encourages the development of algorithms capable of transcribing essays with diverse handwriting styles, paper textures, and writing qualities.

## Dataset Composition

The dataset includes images of essays written under timed conditions, reflecting real-world challenges such as erasures, overwriting, and striking-through texts. It features:
- Diverse handwriting styles and qualities (unique writer per essay image)
- Variations in ink, paper texture, and image resolutions
- Essays on various themes, written under different constraints

## Data Structure

The dataset is organized as follows:

- `data/`: Main folder containing segmented essay images
  - `lines/`: Images of individual lines
    - PNG files: Line images
    - TXT files: Transcriptions of lines
  - `pages/`: Full page essay images
    - PNG files: Page images
    - TXT files: Transcriptions of pages
  - `paragraphs/`: Images of paragraphs
    - PNG files: Paragraph images
    - TXT files: Transcriptions of paragraphs

- `sets/`: Contains partition files
  - `test.txt`: Names of images in the test set
  - `validation.txt`: Names of images in the validation set
  - `training.txt`: Names of images in the training set

## Dataset Usage and Annotations

- Each name in `test.txt`, `validation.txt` and `training.txt` represents the name of the page and all its content (lines, paragraphs, pages) must be in the respective partition.
- Annotations used in the dataset:
  - `##text##`: Text overwritten above the line.
  - `$$text$$`: Text subscripted below the line.
  - `--text--`: Strikethrough or crossed-out text.
  - `--xxx--`: Illegible crossed-out text.
  - `@@???@@`: Illegible text, unidentifiable.
- Mixed tags such as `##---xxx--##`, `$$--xxx--$$`, `##@@???@@##`, and variations are also used.

## Terms of Usage

The BRESSAY dataset may be used for non-commercial research and teaching purposes only. If you are publishing scientific work based on the BRESSAY dataset, we request you to include a reference to our paper:

*Details for dataset citation will be provided.*

## Contact

For any clarifications, please contact Arthur Neto (afsn@ecomp.poli.br) or Byron Bezerra (byron.leite@upe.br) from Universidade de Pernambuco, Brazil.
