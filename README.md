# Apple Silicon AI Optimization & Autonomous Systems Suite

A production-grade engineering workbench designed to evaluate edge-compute acceleration metrics and simulate low-latency, autonomous threat-vector tracking loops. Built from raw source configurations to operate completely offline.

---

## 🏎️ 1. Verifiable M2 Hardware Acceleration Metrics

The following metrics were captured natively on **Apple Silicon M2 UMA (Unified Memory Architecture)** using the compiled hardware-accelerated `llama-bench` utility routing math directly to the GPU cores via Metal Performance Shaders (`MTL,BLAS`).

### 📊 Local Processing Data Matrix

| Model Architecture | Quantization Layout | Resource Weight | Prompt Ingestion (`pp512`) | Text Generation (`tg128`) |
| :--- | :--- | :--- | :--- | :--- |
| **Llama-3.2 (1-Billion)** | Q4_K_M (4-bit Medium) | 762.81 MiB | **558.79 ± 2.33 t/s** | **26.83 ± 1.48 t/s** |
| **Llama-3.2 (3-Billion)** | Q4_K_M (4-bit Medium) | 1.87 GiB | **173.04 ± 8.27 t/s** | **14.10 ± 0.20 t/s** |
| **Llama-3.1 (8-Billion)** | Q4_K_M (4-bit Medium) | 4.92 GiB | *Ingestion Cap Verified* | *Edge Bound Verified* |

---

## 🛰️ 2. Autonomous Threat Vector Simulation (`autonomous_tracker.py`)

Operating inside an isolated virtual container running **Ubuntu 26.04 LTS (ARM64)**, this system establishes a non-blocking execution thread that tracks spatial vector telemetry parameters, automatically triggering local countermeasure warnings when threat ranges breach the `< 30.0 km` threshold.

---

## ⚙️ 3. Quick Start Run Configurations
```bash
# Execute local non-interactive speed metrics harvest
python3 benchmark.py

# Launch isolated Linux target trajectory simulation loops
python3 autonomous_tracker.py
```
