# 🚨 Project Title: SentryCam-AWS

A Real time vehicle detection pipeline for ATM surveillance applications, built with AWS Sagemaker, Lambda, Step Functions, S3 and Cloudwatch

---

## 📌 Overview

This project simulates an intelligent surveillance system that monitors ATM areas and detects the type of vehicles present — such as bicycles, motorcycles, or trucks — to help prevent unauthorized access or parking.

Using the CIFAR-100 dataset (filtered to different vehicle types), this system classifies uploaded images and automates decision-making using serverless AWS components.

> 🛠 **Built with:** AWS SageMaker, Lambda, Step Functions, S3, and Cloudwatch
---

## 🎯 Objectives

- 🔍 Detect specific types of vehicles (e.g. `bicycle`, `motorcycle`, `pickup truck`, `bus`)
- ⚙️ Automate the image classification pipeline using AWS Step Functions
- 📊 Monitor inference confidence levels to evaluate model trustworthiness
- 🧠 Visualize and interpret predictions over time

---

## 🧱 Architecture

![Insert diagram here or describe it]

**Pipeline Flow:**

1. 📤 Image uploaded to S3
2. ⚙️ Lambda function serializes the image (base64 encoding)
3. 🧠 Second Lambda calls SageMaker endpoint
4. ✅ Third Lambda filters results based on confidence threshold
5. 📈 Inference is logged and visualized from captured data

---

## 🖼️ Dataset

Using **CIFAR-100**, filtered to include the following classes:

| Class Label | ID | Description |
|-------------|----|-------------------------------|
| bicycle     | 0  | [e.g., "Unauthorized small vehicle"] |
| motorcycle  | 1  | [e.g., "High-risk vehicle"] |
| pickup truck| 2  | [e.g., "Delivery or service vehicle"] |
| bus         | 3  | [e.g., "Rare/flagged vehicle type"] |

> _You can describe how you selected, filtered, and uploaded the dataset to S3._

---

## 🛠 Setup

### Prerequisites
- AWS account
- SageMaker Studio or notebook instance
- Python 3.x

### Installation

```bash
git clone https://github.com/your-username/your-project-name.git
cd your-project-name
pip install -r requirements.txt
