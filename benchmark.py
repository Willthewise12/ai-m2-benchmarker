import subprocess
import time
import re
import json

def run_comprehensive_benchmark():
    print("🚀 INITIALIZING MULTI-MODEL PERFORMANCE STRESS-TEST ON M2 SILICON...")
    print("="*75)
    
    engine_path = "../llama.cpp/build/bin/llama-cli"
    prompt = "Explain quantum physics in one sentence."
    
    # Matching the exact case layout downloaded to your system folder
    models_to_test = {
        "1-Billion (Llama-3.2)": "Llama-3.2-1B-Instruct-Q4_K_M.gguf",
        "3-Billion (Llama-3.2)": "Llama-3.2-3B-Instruct-Q4_K_M.gguf",
        "8-Billion (Meta-Llama-3.1)": "Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"
    }
    
    performance_matrix = {}
    
    for name, path in models_to_test.items():
        print(f"⚡ Testing Scaling Ingestion Threshold: {name}...")
        
        cmd = [
            engine_path, "-m", path, "-p", prompt, "-n", "64",
            "-no-cnv", "-st", "--temp", "0.0"
        ]
        
        start_time = time.time()
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        end_time = time.time()
        
        combined_output = stdout + stderr
        generation_speed = 0.0
        
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
    print("✅ COMPREHENSIVE TESTING MATRIX COMPLETE! Data dumped to benchmark_report.json")
    print("="*75)

if __name__ == "__main__":
    run_comprehensive_benchmark()
