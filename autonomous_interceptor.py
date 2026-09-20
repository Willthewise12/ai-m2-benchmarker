import time
import os
import sys

def listen_for_radar_vectors():
    pipe_path = "/tmp/radar_pipeline"
    
    # Initialize the synchronized data network bridge if missing
    if not os.path.exists(pipe_path):
        os.mkfifo(pipe_path)
        
    print("\n🚀 AI FORCE: Autonomous Interceptor System Initialized.")
    print("🛰️ Listening for live targeting vectors across network stream...")
    print("="*75)
    
    try:
        while True:
            # Read telemetry variables coming through the socket channel
            with open(pipe_path, "r") as pipe:
                for line in pipe:
                    data = line.strip()
                    if not data:
                        continue
                        
                    # Parse the message components
                    if "TARGET DETECTED" in data:
                        print(f"📡 [INCOMING TELEMETRY] {data}")
                    elif "CRITICAL ALERT" in data:
                        print(f"🔥 {data}")
                        print("⚡ COUNTERMEASURE TRIGGERED: Intercept vector locked. Launching automated kinetic deterrent.")
                        print("-" * 75)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\n🛑 Interceptor shutdown sequence complete. Disengaging launchers.")

if __name__ == '__main__':
    listen_for_radar_vectors()
