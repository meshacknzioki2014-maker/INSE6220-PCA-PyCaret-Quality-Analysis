# INSE 6220 – Advanced Statistical Approaches to Quality  
## Final Project: PCA & Machine Learning for Wine Quality Classification

This repository contains the complete implementation for the INSE 6220 term project at Concordia University.  
The project applies **Principal Component Analysis (PCA)** and **Machine Learning models** using **PyCaret** to classify wine quality based on chemical features.  
The analysis also includes **SHAP explainability**, visual diagnostics, and a complete reproducible workflow in Google Colab.

---

##Repository Structure

INSE6220-PCA-PyCaret-Quality-Analysis/
│
├── Figures/
│ ├── Scree Plot.png
│ ├── Cumulative Variance (Pareto).png
│ ├── PCA Biplot.png
│ ├── PCA Loadings.png
│ ├── Model Comparison (PyCaret).png
│ ├── Confusion Matrix (Best Model).png
│ ├── SHAP Summary Plot.png
│ ├── SHAP Force Plot.png
│
├── INSE_6220_Complete_Colab_Notebook.ipynb # Main notebook (Google Colab ready)
├── inse_6220_project_colab_notebook.py # Python version of the notebook
├── wine_dataset.csv # Dataset used for the project
├── requirements.txt # Required Python packages
├── README.md # Project documentation
└── Project Report (PDF/Docx)
-
---

##Overview

### **Objective**  
To apply **advanced statistical quality analysis techniques** to a real-world dataset by:

- Reducing dimensionality using **Principal Component Analysis (PCA)**
- Training classification models using **PyCaret**
- Selecting the best-performing model based on cross-validated metrics
- Explaining the model using **SHAP interpretability**
- Visualizing PCA components, model comparison, and classification outputs

---

##Installation & Requirements

Install required libraries (Colab recommended):

```bash
pip install scikit-learn numpy pandas matplotlib seaborn shap pycaret
Alternatively, install from the provided requirements.txt:

pip install -r requirements.txt

Running the Project
Option 1 — Google Colab (Recommended)

Open the notebook:

INSE_6220_Complete_Colab_Notebook.ipynb


Upload the dataset when prompted (or switch to use_sklearn_wine=True).

Option 2 — Local execution
python inse_6220_project_colab_notebook.py


Ensure all dependencies in requirements.txt are installed.

Methods Implemented
1. Data Preprocessing

Standardization with StandardScaler

PCA transformation

Explained variance evaluation

Selection of components covering ≥90% variance

2. PCA Visualizations

Scree plot

Cumulative variance (Pareto curve)

PCA biplot

PCA loading plot

3. Machine Learning Models (PyCaret)

Logistic Regression

K-Nearest Neighbors

Quadratic Discriminant Analysis

Random Forest (comparison)

PyCaret automatically performs:

Model comparison

Cross-validated scoring

Hyperparameter tuning

Confusion matrix and metrics

4. Explainability (SHAP)

SHAP summary plot for global feature importance

SHAP force plot for local explanation

Key Figures Produced

This project generates the following visuals (saved in Figures/):

Scree plot

Cumulative explained variance curve

PCA biplot

PCA loading plot

PyCaret model comparison chart

Confusion matrix of best classifier

SHAP summary plot

SHAP force plot (HTML + PNG)

Dataset

The project uses the Wine Dataset, containing chemical analysis of wine cultivars.

Samples: 178

Features: 13 chemical measurements

Target classes: 3 wine categories

Dataset file: wine_dataset.csv

Author

Student Name: [Your Name]
Student ID: [Your ID]
Course: INSE 6220 – Advanced Statistical Approaches to Quality
Instructor: [Instructor Name]
Institution: Concordia University

Project Paper

The full written report is provided inside the repository in PDF/Docx format.

Contact

For questions or academic verification, please contact:
Email: [Your Concordia Email]

Acknowledgments

PyCaret Team (Open-source ML automation)

SHAP (Model interpretability package)

UCI Machine Learning Repository

Concordia Institute for Information Systems Engineering (CIISE)


---

#THAT IS YOUR README.md  
Paste ALL of it into GitHub.  
Nothing else.  
You’re done.

If you want, I can also generate:

A professional GitHub **description**  
A `.gitignore` file  
A **requirements.txt** file  
Final GitHub push commands  

Just tell me **“Generate the push commands”** or **“Generate .gitignore”**.
