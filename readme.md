# Hypertension Prediction Based on NHANES Data

## Description
An older case I prepared for an interview, most of the work is fit for the case's specifications but feel free to grab anything you might find useful. 

The task is to predict potential hypertensive patients using the data available on the NHANES (National Health and Nutrition Examination Survey), where the range for hypertension is defined as either the **median systolic blood pressure of a patient >= 130 mmHg, or their median diastolic blood pressure >= 80 mmHg.**

The following data is used for the preliminary data analysis and the training of the models:

- BPX (non-oscillometric blood pressure)
- BMX (body measurements)
- DEMO (demographics information)
- BPQ (blood pressure questionnaire)
- DIQ (diabetes questionnaire)
- SMQ (smoking questionnaire)
- ALQ (alcohol questionnaire)
- PAQ (physical activity questionnaire)

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation
Pull the repo and install the required libraries.

```bash
git clone https://github.com/nhanes_hypertension.git
cd nhanes_hypertension
pip install -r requirements.txt
```

## Usage
Run the parser script to fetch the necessary data, it downloads the listed .XPT files from the NHANES website.

```bash
python parser.py
```

