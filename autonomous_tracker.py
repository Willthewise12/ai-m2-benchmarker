import time
import random

def run_radar_loop():
    print("\n🛰️ AI FORCE: Autonomous Radar Target Acquisition System Active.")
    print("="*65)
    
    try:
        while True:
            target_distance = round(random.uniform(5.0, 150.0), 2)
            target_velocity = round(random.uniform(200.0, 800.0), 2)
            
            print(f"🎯 TARGET DETECTED | Range: {target_distance} km | Velocity: {target_velocity} m/s")
            
            if target_distance < 30.0:
                print("🚨 CRITICAL ALERT: Threat inside interception vector! Deploying countermeasures.")
            else:
                print("🔒 System Status: Tracking loop stable. Intercept path clear.")
            print("-" * 65)
            
            time.sleep(1.0)
            
    except KeyboardInterrupt:
        print("\n🛑 System shutdown sequence initialized. Stopping radar loops.")

if __name__ == '__main__':
    run_radar_loop()
