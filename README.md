# DDoS Attack Detection using Machine Learning

This project implements a machine learning pipeline to detect Distributed Denial of Service (DDoS) attacks using the KDD Cup 1999 dataset. Multiple Python scripts and models are used to preprocess, train, compare, and evaluate algorithms for classifying network traffic.

## Project Structure

```bash
DDoS-Attack-Detection-using-Machine-Learning/
├── MAIN/                    # Core scripts and data files
│   ├── abc1.py
│   ├── attack1.py
│   ├── attack2.py
│   ├── attacks.py
│   ├── attacks1.py
│   ├── compare1.py
│   ├── gnb1.py
│   ├── attacks.ui           # UI layout
│   ├── Generic_4055.txt
│   ├── kddcup.data_10_percent.gz  # Dataset
│   ├── kddcup.names
│   ├── sample_data.txt
│   └── training_attack_types
├── ignore/                 # Ignored folder (papers, docs, presentations)
│   └── *.docx, *.pdf, *.png, *.pptx
```

## Technologies Used

- Python (with libraries like `sklearn`, `pandas`, `numpy`)
- Classic ML algorithms: Naive Bayes, etc.
- Dataset: KDD Cup 1999

## How to Run

```bash
cd MAIN
python gnb1.py     # or run any relevant script based on your test
```

> Some scripts may expect the dataset to be extracted and available in the same folder.

## Ignored Files and Folders

All content inside the `ignore/` folder is excluded from Git version control:

```gitignore
ignore/
```

---

For academic reference, see `7053Abstract.docx` and `7053Main.docx` (excluded from GitHub).

---

 **Author**: Nikhil Yarra
