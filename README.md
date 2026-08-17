# 🇧🇭 Bahraini Food AI

An AI-powered web application that identifies traditional Bahraini food from images using a YOLO-based image classification model.

🌐 **Live Demo:** [Bahraini Food AI](https://bahraini-food-classifier.streamlit.app/?utm_source=chatgpt.com)

---

## 📌 Project Overview

**Bahraini Food AI** is a Computer Vision and Machine Learning project designed to recognize traditional Bahraini dishes from uploaded or captured images.

The model classifies images into **8 Bahraini food categories** and provides the predicted food name together with the model's confidence score.

The application is built using **Python, YOLO, and Streamlit** and deployed as an interactive web application.

---

## 🍽️ Supported Food Classes

The model can recognize the following Bahraini foods:

* 🍜 **Balaleet**
* 🍮 **Halwa**
* ☕ **Karak**
* 🍯 **Luqaimat**
* 🍚 **Machboos**
* 🥞 **Raqaq**
* 🥟 **Samboosa**
* 🍽️ **Tikka**

---

## ✨ Features

* 📸 Upload a food image
* 📷 Capture a photo directly using the device camera
* 🤖 AI-powered food classification
* 🏆 Displays the most likely food category
* 📊 Displays prediction confidence
* 📈 Shows the Top 3 predicted classes
* 🇧🇭 Focused on traditional Bahraini cuisine
* 🌐 Deployed using Streamlit

Streamlit provides both file uploading and camera input widgets, allowing the application to accept images from a device or directly from a camera. ([GitHub][1])

---

## 🧠 Machine Learning Model

The project uses a **YOLO-based image classification model** trained on a custom Bahraini food dataset.

### Dataset

The dataset contains:

| Item              | Value |
| ----------------- | ----: |
| Number of Classes |     8 |
| Images per Class  |    30 |
| Total Images      |   240 |
| Training Images   |   168 |
| Validation Images |    48 |
| Testing Images    |    24 |

### Dataset Distribution

Each food category contains approximately:

* **21 training images**
* **6 validation images**
* **3 testing images**

This provides a balanced dataset across all eight classes.

---

## 📊 Model Evaluation

The model was evaluated using a separate test set containing **24 images**.

### Test Results

**24 / 24 test images were classified correctly.**

**Test Accuracy: 100%**

The confusion matrix showed correct predictions across all eight classes, with all test samples appearing on the main diagonal.

> ⚠️ Since the test set contains only 24 images, this 100% accuracy should be interpreted cautiously. A larger and more diverse dataset would provide a stronger evaluation of real-world performance.

---

## 🛠️ Technologies Used

* **Python**
* **YOLO / Ultralytics**
* **PyTorch**
* **OpenCV**
* **Pillow**
* **NumPy**
* **Streamlit**
* **Google Colab**
* **GitHub**
* **Streamlit Community Cloud**

---

## 📁 Project Structure

```text
bahraini-food-classifier/
│
├── food_app.py
├── bahraini_food_model.pt
├── requirements.txt
└── README.md
```

### Main Files

**`food_app.py`**
The Streamlit application responsible for image input, prediction, and displaying results.

**`bahraini_food_model.pt`**
The trained YOLO classification model.

**`requirements.txt`**
Contains the Python dependencies required to run the application.

---

## 🚀 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/bahraini-food-classifier.git
cd bahraini-food-classifier
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
streamlit run food_app.py
```

The application will open in your browser.

---

## 📦 Requirements

```text
streamlit
ultralytics
opencv-python-headless==4.10.0.84
pillow
numpy<2
```

---

## 🔮 Future Improvements

Future versions of the project could include:

* 📚 Increasing the dataset size
* 📷 Collecting more real-world food images
* 🧠 Improving model generalization
* 📊 Adding more Bahraini food categories
* 🌐 Improving the web application interface
* 📱 Optimizing the application for mobile devices
* 🔍 Adding explainable AI visualizations
* ⭐ Providing information and ingredients for each dish

---

## 🎯 Project Goal

The main goal of this project is to demonstrate how **Computer Vision and Machine Learning** can be used to recognize and digitally preserve aspects of **Bahraini food culture** through an interactive AI application.

---

## 👩🏻‍💻 Author

**Zainab Moosa**

Data Science
