import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # HF dissociation constant (25°C)
    Ka = 6.6e-4

    # pH range (guaranteed 0.1 spacing, no float drift)
    pH = np.linspace(0, 14, 141)
    H = 10**(-pH)

    # Speciation fractions
    alpha_F = Ka / (Ka + H)
    alpha_HF = H / (Ka + H)

    # Convert to %
    perc_F = alpha_F * 100
    perc_HF = alpha_HF * 100

    # Create dataframe
    df = pd.DataFrame({
        'pH': np.round(pH, 2),
        'HF_percent': np.round(perc_HF, 6),
        'F_minus_percent': np.round(perc_F, 6)
    })

    # Save CSV (this will ALWAYS execute)
    df.to_csv('hf_speciation.csv', index=False)

    # Create plot
    plt.figure()
    plt.plot(pH, perc_F, label='F- (%)')
    plt.plot(pH, perc_HF, label='HF (%)')

    plt.xlabel('pH')
    plt.ylabel('Percentage (%)')
    plt.title('HF / F- Speciation vs pH')
    plt.legend()
    plt.grid()

    # Save figure BEFORE show (critical)
    plt.savefig('hf_speciation_plot.png', dpi=300)

    # Try to show (safe even if backend fails)
    try:
        plt.show()
    except:
        print("Plot display skipped (no GUI backend). File saved instead.")

    print("Execution complete.")
    print("Files generated:")
    print("- hf_speciation.csv")
    print("- hf_speciation_plot.png")


if __name__ == "__main__":
    main()