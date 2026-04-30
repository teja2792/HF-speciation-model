# HF-speciation-model

# HF Speciation vs pH

This project calculates and visualizes the equilibrium distribution of hydrofluoric acid (HF) and fluoride ion (F⁻) as a function of pH.

Core dependencies:

numpy
pandas
matplotlib
---

## 📌 Objective

To compute and plot the percentage of:
- HF (undissociated acid)
- F⁻ (fluoride ion)

across a pH range (0–14) using equilibrium thermodynamics.

---

## ⚙️ Model Description

The system is governed by the acid dissociation equilibrium:

HF ⇌ H⁺ + F⁻

Using:
- Ka (HF dissociation constant) = 6.6 × 10⁻⁴
- pH-dependent hydrogen ion concentration

Fractions are computed as:

- Fraction of F⁻:
  
  F⁻ = Ka / (Ka + [H⁺])

- Fraction of HF:
  
  HF = [H⁺] / (Ka + [H⁺])

---

## 📊 Outputs

Running the script generates:

- `hf_speciation.csv`  
  → Tabulated pH vs HF (%) and F⁻ (%)

- `hf_speciation_plot.png`  
  → Plot of HF and F⁻ percentage vs pH
<img width="1920" height="1440" alt="hf_speciation_plot" src="https://github.com/user-attachments/assets/b933f35b-bc43-4583-b0ff-98da9071dd9e" />

---

## ▶️ How to Run

### 1. Clone or download the repository

### 2. Navigate to the project folder

```powershell
cd "path\to\HF Speciation Plot"
