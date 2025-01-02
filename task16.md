### MQ135 Gas Sensor Report

#### Overview
The MQ135 gas sensor is widely used for air quality monitoring, capable of detecting gases like ammonia (NH3), nitrogen oxides (NOx), alcohol, benzene, smoke, and carbon dioxide (CO2). It is a versatile and low-cost solution for environmental and industrial applications.

#### Technical Specifications
- **Operating Voltage:** 5V
- **Heating Voltage:** 5V (AC or DC)
- **Load Resistance:** Adjustable (typically 10 kΩ)
- **Heater Resistance:** 33±5Ω (room temperature)
- **Sensing Resistance:** 10kΩ to 200kΩ (depending on the gas concentration)
- **Detectable Concentration Range:** 10 to 1000 ppm
- **Preheat Time:** ≤20 seconds

#### Working Principle
The MQ135 uses a tin dioxide (SnO2) sensitive layer with a lower conductivity in clean air. When exposed to target gases, the conductivity increases proportionally to the gas concentration. The sensor's output is an analog voltage that can be read by a microcontroller or an ADC (Analog-to-Digital Converter).

---

### ICs and Circuit Components Used

#### 1. **L293D Motor Driver IC**
While primarily used for controlling motors, the L293D can play a role in interfacing and controlling peripheral devices like actuators in gas detection systems.

- **Features:**
  - Dual H-Bridge for controlling two motors or loads.
  - Built-in diodes for back EMF protection.
  - Operates at 4.5V to 36V.

- **Internal Components:**
  - **H-Bridge:** A circuit configuration allowing current to flow in either direction through a load.
  - **Logic Control:** Determines the operation of the H-Bridge based on input signals.

#### 2. **Pulse Width Modulation (PWM):**
PWM is crucial for controlling heater voltage in the MQ135 sensor. It modulates the power supplied to the heater, maintaining optimal operating temperatures for different gases.

#### 3. **H-Bridge:**
Used in systems requiring bi-directional control, the H-Bridge can manage the polarity of voltage supplied to components like actuators in automated gas monitoring systems.

---

### Calibration and Gas Detection
Calibration is critical for accurate gas detection using the MQ135 sensor. The sensor must be calibrated in clean air and against known gas concentrations to establish a reference resistance (Ro).

#### Calibration Steps
1. **In Clean Air:**
   - Measure the sensor's resistance (Rs) in clean air (typically at 100 ppm).
   - Calculate Ro:
     \[ Ro = \frac{Rs}{CleanAirFactor} \]
     The CleanAirFactor for MQ135 is typically 3.6.

2. **For Target Gases:**
   - Use the sensor's datasheet to find the appropriate curve for the target gas.
   - Calculate the gas concentration (ppm) using the equation:
     \[ \text{ppm} = 10^{\left(\frac{\log(Rs/Ro)}{Slope}\right)} \]
     where Rs is the measured resistance, and the slope is derived from the datasheet.

#### Gas-Specific Calibration Values
- **Ammonia (NH3):** Slope = -0.77
- **Benzene:** Slope = -0.61
- **Carbon Dioxide (CO2):** Slope = -0.35

---

### Freundlich Adsorption Isotherm
The Freundlich adsorption theorem is used to describe the sensor's adsorption of gas molecules. The relationship is expressed as:
\[ x/m = k \cdot C^{1/n} \]
where:
- \( x/m \): Amount of gas adsorbed per unit mass of adsorbent.
- \( C \): Gas concentration.
- \( k \) and \( 1/n \): Empirical constants.

#### Freundlich Absorption Graph
The graph plots \( \log(x/m) \) against \( \log(C) \), resulting in a straight line where:
- Slope = \( 1/n \)
- Intercept = \( \log(k) \)



This relationship helps understand the adsorption behavior and enhances calibration accuracy.

---

### Applications
- Air quality monitoring in homes and offices.
- Industrial safety systems for gas leak detection.
- Agricultural monitoring for greenhouse gases.
- Vehicle emission testing.

---

### Conclusion
The MQ135 gas sensor is a reliable and efficient tool for detecting a variety of gases. Proper calibration and understanding of its working principles, including the Freundlich adsorption theorem, are essential for accurate gas measurement and implementation in diverse applications.

