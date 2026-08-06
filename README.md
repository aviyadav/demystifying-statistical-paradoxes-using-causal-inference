# Demystifying Statistical Paradoxes Using Causal Inference

This project provides clear, code-based demonstrations of common statistical paradoxes. By simulating these paradoxes and analyzing the data, we can understand how misleading conclusions can be drawn from data if the underlying causal structure (or selection bias) is ignored.

## 🚀 Paradoxes Covered

### 1. Simpson's Paradox
**What is it?**
Simpson's Paradox occurs when a trend appears in several groups of data but disappears or reverses when these groups are combined.

**Examples included:**
- **UC Berkeley Admissions**: A classic case where women appeared to have a lower admission rate overall, but actually had higher admission rates in most individual departments.
- **Kidney Stone Treatment**: A case where Treatment A appears worse than Treatment B overall, but is actually more effective for both small and large stones individually.

### 2. Berkson's Paradox
**What is it?**
Berkson's Paradox is a form of selection bias. It occurs when two independent variables appear to be negatively correlated because the sample is restricted to a subset of the population (e.g., only those who were "selected" or "successful").

**Example included:**
- **Attribute Selection Simulation**: A simulation showing how two independent traits in a general population become negatively correlated when we only look at individuals who possess at least one of those traits.

## 🛠️ Project Structure

```text
src/
└── demystifying_statistical_paradoxes_using_causal_inference/
    ├── base.py         # Abstract base class for paradox examples
    ├── simpsons_paradox.py  # Implementation of Simpson's Paradox
    ├── berksons_paradox.py  # Implementation of Berkson's Paradox
    └── main.py         # Entry point to run all demonstrations
```

## 📦 Installation & Running

### Prerequisites
- Python 3.x
- `pandas`
- `numpy`
- `statsmodels`

### How to Run
You can run the demonstrations using the following command from the project root:

```bash
PYTHONPATH=src python3 -m demystifying_statistical_paradoxes_using_causal_inference.main
```

### Using `uv`
```bash
uv run python -m demystifying_statistical_paradoxes_using_causal_inference.main
```

## 🧠 Key Takeaway
The core lesson across these paradoxes is that **correlation does not imply causation**. Understanding the "collider" variables (in Berkson's) or "confounders" (in Simpson's) is essential for correct data interpretation.
