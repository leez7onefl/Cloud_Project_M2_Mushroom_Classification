# Mushroom Classification Report

## Table of Contents

1. Installing Required Libraries
2. Reading and Understanding our Data
3. Handling Outliers
4. Data Visualization
5. Data Preprocessing
   - Separate Features and Target
   - Data Scaling
   - Train/Test Split
6. Machine Learning
   - Logistic Regression
   - K Nearest Neighbors

## 1. Installing Required Libraries

To kick-start our project, we brought in essential libraries like Pandas for data manipulation, NumPy for mathematical operations, Seaborn and Matplotlib for visual insights, and SciPy for statistical processing. This setup ensured our environment was equipped to handle comprehensive data exploration and model development.

## 2. Reading and Understanding our Data

### Objective

Our objective in this step was to thoroughly understand the underlying structure and composition of our dataset, ensuring familiarity and preparedness for subsequent analysis stages.

### Process

1. **Loading Data:** 
   - Imported the dataset using Pandas and examined the first few entries. The data preview (refer to first image) shows features like cap-diameter, cap-shape, etc., with their respective classes (edible or poisonous).

2. **Dataset Structure:**
   - The dataset comprises 54,035 rows and 9 features, as validated by the `shape` function.
   - Data types (refer to second image) were consistent, with most features being integers, making further numerical analysis straightforward.

3. **Summary Statistics:**
   - Utilized `describe()` to gather insights on central tendency and dispersion (refer to third image). For instance, cap-diameter varies significantly, showing the spread and range of observations. 

4. **Correlation Analysis:**
   - Calculated correlations between each feature and the class variable (see fourth image). Stem-height exhibited a slight positive correlation with class, indicating a small degree of association with mushroom edibility.
   - 

### Insights

- **Non-null Values:** Confirmed that there are no missing values, indicating data completeness.
- **Feature Variability:** Observed diverse ranges and standard deviations in features like cap-diameter and stem-height.
- **Correlations:** Noted that stem-height shows the highest correlation with class, though still modest.

### Azure ML Designer Implementation

- **Data Import Module:** Decoded data import and preliminary exploration using Azure’s intuitive interfaces, significantly reducing manual preprocessing time.
- **Data Profile Tool:** Automatically highlighted data types and potential discrepancies, enabling rapid insights into dataset characteristics.

## 3. Handling Outliers

### Objective

Addressing outliers was crucial to ensuring that anomalous data points did not distort model training or prediction accuracy.

### Process

1. **Z-score Analysis:**
   - Calculated Z-scores for every feature to identify extreme values, using a conventional threshold of 3 to determine outliers.
   - Outliers disrupt machine learning models, and identifying them through Z-score ensured data homogeneity.

2. **Eliminating Outliers:**
   - Rows with excessive Z-scores were expunged, leading to a refined dataset potentially yielding higher model fidelity.

### Azure Implementation

- **Custom Python Scripts:** Ease of implementation through Azure’s Execute Script module, specializing in custom code execution for tailored data cleaning.

## 4. Data Visualization

### Objective

Visualization aimed at revealing underlying patterns and relationships between dataset features, facilitating intuitive comprehension of class distributions.

### Process

1. **Histogram and Count Plots:**
   - Developed visual plots (e.g., histograms) to compare distributions across classes. Visualization confirmed that certain measurements, like cap shape and dimensions, varied distinctly between edible and poisonous mushrooms.

### Insights

- Clear differentiation emerged in feature distributions when analyzed via histograms and count plots, specifically in mushroom cap sizes and stem measurements.

![__results___35_0](https://github.com/user-attachments/assets/ee738e01-7dac-4c7d-82e4-6d9931889adf)

---

## 5. Data Preprocessing

### 5.1. Separate Features and Target

#### Objective

To streamline model training, it was essential to systematically separate input variables (features) from the target variable (class).

#### Azure Implementation

- **Data Split Facilitation:** Directly separated features and target with Azure’s Split Data module, ensuring accurate dataset trajectory into model training phases.

### 5.2. Data Scaling

#### Objective

By scaling features, we ensured fairness and comparability among them, preventing any feature from unduly dominating the distance-based models.

#### Process

1. **Standardization:**
   - Employed `StandardScaler` for feature normalization, centralizing all features around a mean of zero with unit variance, indispensable for algorithms sensitive to input scales.

#### Azure Implementation

- **Scaler Integration:** Azure enabled smooth flow of scaled datasets into modeling pipelines, aligning with end-to-end lifecycle support.

### 5.3. Train/Test Split

#### Objective

Conducted data splitting to prepare training and validation sets, providing future performance assessments on untouched data.

#### Process

- Opted for a stratified 70/30 split, ensuring class distribution integrity across subsets.

#### Azure Implementation

- **Split Data Module:** Facilitated accurate divisions within Azure, offering a seamless approach to maintain consistent class ratios.

## 6. Machine Learning

### 6.1. Logistic Regression

#### Objective

Adopted logistic regression to understand linearly separable relationships between features and classes, setting a solid simple-model baseline.

#### Process

1. **Regularization Techniques:**
   - Deployed cross-validation over L1 and L2 regularizations, optimizing model complexity and reducing overfitting risks.

#### Azure Implementation

- **Model Hyperparameter Tuning Module:** Streamlined hyperparameter decisions within Azure, ensuring efficient computation of different regularization paths.

![__results___62_0](https://github.com/user-attachments/assets/916acd6c-03e9-4e4c-a824-a4a01de06b4a)

---

### 6.2. K Nearest Neighbors

#### Objective

KNN highlighted locality-driven class resolutions, harnessing large dataset intricacies for improved predictions.

#### Process

1. **K Optimization:**
   - Iteratively tested multiple `k` values, quantifying error rates to pinpoint `k=3` for minimal prediction errors.

#### Azure Implementation

- **Scripting Module for KNN:** Enabled dynamic adjustment of `k`, leveraging Azure’s interactive tools for quick recalibrations.

![__results___73_0](https://github.com/user-attachments/assets/2bd35636-fcf8-42b7-b869-b229c90cd862)

![__results___76_0](https://github.com/user-attachments/assets/8b36be38-a3df-4e6b-a9d1-693e6fd74a0d)
