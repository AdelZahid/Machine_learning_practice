import matplotlib.pyplot as plt
import numpy as np

# Define the collector-emitter voltage range
V_CE = np.linspace(0, 20, 200)

# Define base currents
I_B_values = [10e-6, 20e-6, 30e-6, 40e-6, 50e-6]

# Define a hypothetical current gain (Beta)
Beta = 100

# Plotting
plt.figure(figsize=(10, 6))

for I_B in I_B_values:
    # Calculate collector current I_C
    I_C = Beta * I_B * (1 - np.exp(-V_CE))
    plt.plot(V_CE, I_C, label=f'I_B = {I_B * 1e6:.0f} µA')

# Labels and title
plt.xlabel('Collector-Emitter Voltage V_CE (V)')
plt.ylabel('Collector Current I_C (mA)')
plt.title('Output Characteristics of a PNP Transistor')
plt.legend()
plt.grid(True)
plt.ylim(0, 6)  # Adjust according to hypothetical I_C values
plt.xlim(0, 20)

# Show plot
plt.show()
