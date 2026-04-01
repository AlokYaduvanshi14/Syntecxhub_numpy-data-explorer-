# 📊 NumPy Data Explorer

A lightweight and efficient data exploration tool built using **NumPy**. This project helps you quickly load, analyze, and summarize datasets directly from the command line or scripts.

---

## 🚀 Features

* 📂 Load datasets from CSV / text files
* 🔢 Fast numerical computations using NumPy
* 📈 Basic statistical analysis:

  * Mean
  * Median
  * Standard Deviation
  * Min / Max values
* 🔍 Data inspection utilities:

  * Shape and dimensions
  * Data types
  * Missing value detection
* ⚡ Lightweight and fast (no heavy dependencies)

---

## 🛠️ Tech Stack

* Python 🐍
* NumPy

---

## 📁 Project Structure

```
numpy-data-explorer/
│── data/              # Sample datasets
│── src/               # Source code
│   ├── loader.py      # Data loading functions
│   ├── analyzer.py    # Statistical analysis
│   ├── utils.py       # Helper functions
│── main.py            # Entry point
│── requirements.txt
│── README.md
```

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/numpy-data-explorer.git
cd numpy-data-explorer
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

Example:

```python
import numpy as np
from src.loader import load_data
from src.analyzer import summarize_data

data = load_data("data/sample.csv")
summarize_data(data)
```

---

## 📊 Example Output

```
Shape: (100, 5)
Mean: [23.4, 45.1, 12.3, 67.8, 34.5]
Std Dev: [5.2, 3.1, 6.7, 2.4, 4.8]
Min: [10, 40, 5, 60, 30]
Max: [30, 50, 20, 70, 40]
```

---

## 🎯 Future Improvements

* 📉 Data visualization (Matplotlib / Seaborn)
* 🧠 Integration with Pandas
* 🌐 Web-based interface
* 📊 Advanced analytics (correlation, distributions)

---

##  Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Open a pull request

---

## License

This project is licensed under the MIT License.

---

##  Acknowledgements

* NumPy community for amazing tools
* Open-source contributors

---
