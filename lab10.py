import numpy as np
import matplotlib.pyplot as plt

class FuzzyMembershipFunction:
    @staticmethod
    def triangular(x, a, b, c):
        """Triangular membership function"""
        if x <= a or x >= c:
            return 0
        elif a < x <= b:
            return (x - a) / (b - a)
        else:
            return (c - x) / (c - b)
    
    @staticmethod
    def trapezoidal(x, a, b, c, d):
        """Trapezoidal membership function"""
        if x <= a or x >= d:
            return 0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif b <= x <= c:
            return 1
        else:
            return (d - x) / (d - c)

class FuzzyTemperatureController:
    def __init__(self):
        self.temp_range = (0, 35)
        self.humidity_range = (0, 100)
        self.speed_range = (0, 100)
    
    def fuzzify_temperature(self, temp):
        """Convert crisp temperature to fuzzy values"""
        cold = FuzzyMembershipFunction.triangular(temp, 0, 5, 15)
        warm = FuzzyMembershipFunction.triangular(temp, 10, 17.5, 25)
        hot = FuzzyMembershipFunction.triangular(temp, 20, 27.5, 35)
        return {'cold': cold, 'warm': warm, 'hot': hot}
    
    def fuzzify_humidity(self, humidity):
        """Convert crisp humidity to fuzzy values"""
        low = FuzzyMembershipFunction.triangular(humidity, 0, 20, 40)
        medium = FuzzyMembershipFunction.triangular(humidity, 30, 50, 70)
        high = FuzzyMembershipFunction.triangular(humidity, 60, 80, 100)
        return {'low': low, 'medium': medium, 'high': high}
    
    def fuzzify_fan_speed(self, speed):
        """Membership functions for fan speed"""
        off = FuzzyMembershipFunction.triangular(speed, 0, 0, 20)
        low = FuzzyMembershipFunction.triangular(speed, 10, 30, 50)
        medium = FuzzyMembershipFunction.triangular(speed, 40, 60, 80)
        high = FuzzyMembershipFunction.triangular(speed, 70, 100, 100)
        return {'off': off, 'low': low, 'medium': medium, 'high': high}
    
    def apply_rules(self, temp_fuzzy, humidity_fuzzy):
        """Apply fuzzy rules and return output"""
        rules_fired = []
        
        # Rule 1: IF temp is Cold AND humidity is Low THEN speed is Off
        rule1 = min(temp_fuzzy['cold'], humidity_fuzzy['low'])
        rules_fired.append(('off', rule1))
        
        # Rule 2: IF temp is Warm AND humidity is Low THEN speed is Low
        rule2 = min(temp_fuzzy['warm'], humidity_fuzzy['low'])
        rules_fired.append(('low', rule2))
        
        # Rule 3: IF temp is Warm AND humidity is Medium THEN speed is Medium
        rule3 = min(temp_fuzzy['warm'], humidity_fuzzy['medium'])
        rules_fired.append(('medium', rule3))
        
        # Rule 4: IF temp is Hot AND humidity is Low THEN speed is Low
        rule4 = min(temp_fuzzy['hot'], humidity_fuzzy['low'])
        rules_fired.append(('low', rule4))
        
        # Rule 5: IF temp is Hot AND humidity is Medium THEN speed is Medium
        rule5 = min(temp_fuzzy['hot'], humidity_fuzzy['medium'])
        rules_fired.append(('medium', rule5))
        
        # Rule 6: IF temp is Hot AND humidity is High THEN speed is High
        rule6 = min(temp_fuzzy['hot'], humidity_fuzzy['high'])
        rules_fired.append(('high', rule6))
        
        return rules_fired
    
    def defuzzify(self, rules_fired):
        """Center of Mass defuzzification"""
        numerator = 0
        denominator = 0
        
        for speed_level, strength in rules_fired:
            if speed_level == 'off':
                center = 0
            elif speed_level == 'low':
                center = 30
            elif speed_level == 'medium':
                center = 60
            elif speed_level == 'high':
                center = 90
            
            numerator += center * strength
            denominator += strength
        
        if denominator == 0:
            return 0
        
        return numerator / denominator
    
    def control(self, temperature, humidity):
        """Main control logic"""
        # Fuzzification
        temp_fuzzy = self.fuzzify_temperature(temperature)
        humidity_fuzzy = self.fuzzify_humidity(humidity)
        
        # Rule Evaluation
        rules_fired = self.apply_rules(temp_fuzzy, humidity_fuzzy)
        
        # Defuzzification
        fan_speed = self.defuzzify(rules_fired)
        
        return fan_speed, temp_fuzzy, humidity_fuzzy, rules_fired

# Create Controller
print("\n" + "#" * 70)
print("FUZZY LOGIC TEMPERATURE AND FAN SPEED CONTROLLER")
print("#" * 70)

controller = FuzzyTemperatureController()

# Test Cases
test_cases = [
    (10, 30, "Cold room, low humidity"),
    (18, 45, "Warm room, medium humidity"),
    (28, 75, "Hot room, high humidity"),
    (5, 20, "Very cold, very dry"),
    (32, 90, "Very hot, very humid"),
]

print("\n" + "=" * 70)
print("TEST RESULTS")
print("=" * 70)
print(f"{'Temp(°C)':<12} {'Humidity(%)':<15} {'Fan Speed(%)':<15} {'Scenario':<25}")
print("-" * 70)

for temp, humidity, scenario in test_cases:
    fan_speed, _, _, _ = controller.control(temp, humidity)
    print(f"{temp:<12} {humidity:<15} {fan_speed:<15.2f} {scenario:<25}")

print("=" * 70)

# Detailed Analysis for One Case
print("\n\n" + "#" * 70)
print("DETAILED ANALYSIS: Hot Room with High Humidity")
print("#" * 70)

temperature = 28
humidity = 75

fan_speed, temp_fuzzy, humidity_fuzzy, rules_fired = controller.control(temperature, humidity)

print(f"\nInput Conditions:")
print(f"  Temperature: {temperature}°C")
print(f"  Humidity: {humidity}%")

print(f"\nFuzzification Results:")
print(f"\n  Temperature Fuzzy Values:")
print(f"    Cold:  {temp_fuzzy['cold']:.4f}")
print(f"    Warm:  {temp_fuzzy['warm']:.4f}")
print(f"    Hot:   {temp_fuzzy['hot']:.4f}")

print(f"\n  Humidity Fuzzy Values:")
print(f"    Low:    {humidity_fuzzy['low']:.4f}")
print(f"    Medium: {humidity_fuzzy['medium']:.4f}")
print(f"    High:   {humidity_fuzzy['high']:.4f}")

print(f"\nRules Fired:")
for speed_level, strength in rules_fired:
    if strength > 0:
        print(f"  {speed_level.capitalize()}: {strength:.4f}")

print(f"\nDefuzzification (Center of Mass):")
print(f"  Final Fan Speed: {fan_speed:.2f}%")

if fan_speed < 20:
    status = "OFF"
elif fan_speed < 50:
    status = "LOW"
elif fan_speed < 80:
    status = "MEDIUM"
else:
    status = "HIGH"

print(f"  Status: {status}")
print("=" * 70)
