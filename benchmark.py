import subprocess
import time
import re
import json

def run_benchmark():
    print("🚀 Initializing M2 Silicon Performance Benchmark...")
    engine_path = "../llama.cpp/build/bin/llama-cli"
    model_path = "../llama.cpp/Llama-3.2-1B-Instruct-Q4_K_M.gguf"
    prompt = "Explain the concept of quantum computing in one short sentence."
    
    cmd = [engine_path, "-m", model_path, "-p", prompt, "-n", "64"]
    
    start_time = time.time()
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    end_time = time.time()
    
    generation_speed = 0.0
    match = re.search(r"Generation:\s+([\d.]+)\s+t/s", stderr + stdout)
    if match:
        generation_speed = float(match.group(1))
        
    report = {
        "device": "Apple Silicon M2",
        "model": "Llama-3.2-1B-Q4",
        "generation_speed_t_s": generation_speed,
        "total_execution_time_sec": round(end_time - start_time, 2)
    }
    
    with open("benchmark_report.json", "w") as f:
        json.dump(report, f, indent=4)
        
    print("✅ Benchmark complete! Data matrix exported to benchmark_report.json")
    print(f"📈 Local Compute Speed: {generation_speed} tokens/second")

if __name__ == "__main__":
    run_benchmark()
