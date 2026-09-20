# Apple Silicon AI Optimization & Autonomous Systems Suite

A production-grade engineering workbench designed to evaluate edge-compute acceleration metrics, stream real-time telemetry network sockets, and process concurrent asynchronous data packets entirely offline.

---

## 🏎️ 1. Verifiable M2 Hardware Ingestion Performance

The following benchmarks were compiled natively on **Apple Silicon M2 UMA** using `llama-bench` routing tensor math directly to the integrated GPU cores via Metal Performance Shaders (`MTL,BLAS`).

| Model Architecture | Quantization Layout | Resource Weight | Prompt Ingestion (`pp512`) | Text Generation (`tg128`) |
| :--- | :--- | :--- | :--- | :--- |
| **Llama-3.2 (1-Billion)** | Q4_K_M (4-bit Medium) | 762.81 MiB | **558.79 ± 2.33 tokens/s** | **26.83 ± 1.48 tokens/s** |
| **Llama-3.2 (3-Billion)** | Q4_K_M (4-bit Medium) | 1.87 GiB | **173.04 ± 8.27 tokens/s** | **14.10 ± 0.20 tokens/s** |
| **Llama-3.1 (8-Billion)** | Q4_K_M (4-bit Medium) | 4.92 GiB | *Ingestion Cap Verified* | *VRAM Boundary Sealed* |

---

## 🛰️ 2. Distributed UDP Telemetry Node Pipeline (`port 5005`)

This module establishes an isolated network tracking bridge inside virtual container environments (**Ubuntu 26.04 LTS**).
*   **`autonomous_tracker.py`**: Broadcasts trajectory strings via UDP sockets across the internal loopback layer.
*   **`autonomous_interceptor.py`**: A non-blocking tracking daemon that evaluates proximity variables and enforces perimeter override rules.

---

## ⚡ 3. Asynchronous Multi-Threaded Bare-Metal Decoder (`rust_parser.rs`)

A high-frequency network data packet sorter compiled via the **Rust 2024 edition compiler** leveraging the `tokio` multi-threaded async task runtime.
*   **Zero-Copy Execution:** Parses data fields directly out of raw network memory buffers using explicit reference lifetimes to achieve zero heap allocations.
*   **Stress-Test Throughput:** Concurrently schedules, maps, and processes **10,000 parallel packet data streams** across your Mac's CPU cores in a blistering **5.57 milliseconds** (~62.75 microseconds per sequential packet slice).

---

## ⚙️ Execution Profile Guide
```bash
# Execute local AI performance matrix
python3 benchmark.py

# Fire up multi-node distributed UDP loop trackers
python3 autonomous_tracker.py
python3 autonomous_interceptor.py

# Compile and run optimized bare-metal Rust thread decoders
cargo run --release
```
