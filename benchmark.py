import subprocess
import time
import re
import json
import os

def run_comprehensive_benchmark():
    print("🚀 INITIALIZING REAL-TIME MULTI-MODEL PERFORMANCE STRESS-TEST ON M2 SILICON...")
    print("="*75)
    
    # Path routing to locate your compiled engine folder smoothly
    engine_path = "../llama.cpp/build/bin/llama-cli"
    prompt = "Explain quantum physics in one short sentence."
    
    # Direct matching of files in your active folder path
    models_to_test = {
        "1-Billion (Llama-3.2)": "Llama-3.2-1B-Instruct-Q4_K_M.gguf",
        "3-Billion (Llama-3.2)": "Llama-3.2-3B-Instruct-Q4_K_M.gguf",
        "8-Billion (Meta-Llama-3.1)": "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
    }
    
    performance_matrix = {}
    
    for name, filename in models_to_test.items():
        print(f"⚡ Testing Scaling Ingestion Threshold: {name}...")
        
        if not os.path.exists(filename):
            print(f"   ❌ Error: {filename} not found in this folder. Skipping...\n")
            continue
            
        cmd = [
            engine_path, "-m", filename, "-p", prompt, "-n", "32",
            "-no-cnv", "-st", "--temp", "0.0"
        ]
        
        start_time = time.time()
        # Capturing stdout AND stderr together fixes the regex data gap
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        end_time = time.time()
        
        combined_output = stdout + stderr
        generation_speed = 0.0
        
        # Comprehensive search for generation metrics inside the log streams
        match = re.search(r"Generation:\s+([\d.]+)\s+t/s", combined_output)
        if match:
            generation_speed = float(match.group(1))
            
        performance_matrix[name] = {
            "tokens_per_second": generation_speed,
            "total_latency_seconds": round(end_time - start_time, 2)
        }
        print(f"   ↳ Result: {generation_speed} t/s | Process Time: {round(end_time - start_time, 2)}s\n")

    final_report = {
        "hardware_platform": "Apple Silicon M2 (Unified Memory)",
        "test_results": performance_matrix
    }
    
    with open("benchmark_report.json", "w") as f:
        json.dump(final_report, f, indent=4)
        
    print("="*75)
    print("✅ MATRIX ANALYSIS MANIFEST EXPORTED COMPLETE!")
    print("="*75)

if __name__ == "__main__":
    run_comprehensive_benchmark()
