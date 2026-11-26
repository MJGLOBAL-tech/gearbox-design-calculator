# Gearbox Design Calculator
# By MJGLOBAL-tech

import math

def main():
    print("=== GEARBOX DESIGN CALCULATOR ===")
    print("")

    # Inputs
    power_kw = float(input("Enter Power (kW): "))
    input_rpm = float(input("Enter Input Speed (rpm): "))
    output_rpm = float(input("Enter Output Speed (rpm): "))
    teeth_pinion = int(input("Enter No. of Teeth on Pinion: "))
    teeth_gear = int(input("Enter No. of Teeth on Gear: "))
    module = float(input("Enter Module (mm): "))

    # Calculations
    gear_ratio = input_rpm / output_rpm
    actual_ratio = teeth_gear / teeth_pinion
    torque_nm = (power_kw * 1000 * 60) / (2 * math.pi * input_rpm)
    output_torque = torque_nm * actual_ratio
    pitch_dia_pinion = module * teeth_pinion
    pitch_dia_gear = module * teeth_gear
    centre_distance = (pitch_dia_pinion + pitch_dia_gear) / 2

    print("")
    print("--- RESULTS ---")
    print(f"Required Gear Ratio: {gear_ratio:.2f}")
    print(f"Actual Gear Ratio: {actual_ratio:.2f}")
    print(f"Input Torque: {torque_nm:.2f} Nm")
    print(f"Output Torque: {output_torque:.2f} Nm")
    print(f"Pinion Pitch Diameter: {pitch_dia_pinion:.2f} mm")
    print(f"Gear Pitch Diameter: {pitch_dia_gear:.2f} mm")
    print(f"Centre Distance: {centre_distance:.2f} mm")

if __name__ == "__main__":
    main()
