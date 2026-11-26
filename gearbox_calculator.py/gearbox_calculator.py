# Gearbox Design Calculatorimport math

# Gearbox Design Calculator
print("=== Gearbox Design Calculator ===")

# Inputs
power_kw = float(input("Enter power (kW): "))
input_rpm = float(input("Enter input speed (RPM): "))
output_rpm = float(input("Enter output speed (RPM): "))
teeth_pinion = int(input("Enter teeth on pinion: "))
teeth_gear = int(input("Enter teeth on gear: "))
module = float(input("Enter module (mm): "))

# Calculations
gear_ratio = input_rpm / output_rpm
actual_ratio = teeth_gear / teeth_pinion

# Torque: T = (P * 60) / (2 * pi * N)
torque_nm = (power_kw * 1000 * 60) / (2 * math.pi * input_rpm)
output_torque = torque_nm * actual_ratio

# Gear geometry
pitch_dia_pinion = module * teeth_pinion
pitch_dia_gear = module * teeth_gear
centre_distance = (pitch_dia_pinion + pitch_dia_gear) / 2

# Results
print("\n--- Results ---")
print(f"Required Gear Ratio: {gear_ratio:.2f}")
print(f"Actual Gear Ratio: {actual_ratio:.2f}")
print(f"Input Torque: {torque_nm:.2f} Nm")
print(f"Output Torque: {output_torque:.2f} Nm")
print(f"Pinion Pitch Diameter: {pitch_dia_pinion:.2f} mm")
print(f"Gear Pitch Diameter: {pitch_dia_gear:.2f} mm")
print(f"Centre Distance: {centre_distance:.2f} mm")
