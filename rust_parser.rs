use std::time::Instant;

#[derive(Debug)]
struct TelemetryPacket<'a> {
    target_id: &'a str,
    range_km: f64,
    velocity_ms: f64,
}

// Adding the '_ lifetime annotation explicitly cleans the compiler telemetry warnings
fn parse_packet(raw_stream: &str) -> Option<TelemetryPacket<'_>> {
    let mut parts = raw_stream.split('|');
    
    let id = parts.next()?;
    let range: f64 = parts.next()?.parse().ok()?;
    let velocity: f64 = parts.next()?.parse().ok()?;
    
    Some(TelemetryPacket {
        target_id: id,
        range_km: range,
        velocity_ms: velocity,
    })
}

fn main() {
    println!("🛰️ RUST AI FORCE: Initializing Ultra-Low Latency Telemetry Workspace.");
    println!("=======================================================================");

    let mock_network_packets = vec![
        "TRK-091|42.15|340.20",
        "TRK-772|12.80|610.45",
        "TRK-404|119.50|210.15",
        "TRK-118|24.35|780.90",
    ];

    let start_time = Instant::now();

    for (index, raw_packet) in mock_network_packets.iter().enumerate() {
        match parse_packet(raw_packet) {
            Some(packet) => {
                println!(
                    "⚡ [Packet {}] Decoded -> ID: {} | Vector Range: {} km | Velocity: {} m/s",
                    index + 1, packet.target_id, packet.range_km, packet.velocity_ms
                );
                
                if packet.range_km < 30.0 {
                    println!("   🚨 ALERT: Threat inside proxy perimeter! Intercept calculation locked.");
                }
            }
            None => println!("⚠️ Error: Telemetry line degradation on index {}", index),
        }
    }

    let duration = start_time.elapsed();
    println!("=======================================================================");
    println!("✅ PARSE ARRAY PIPELINE COMPLETE!");
    println!("📈 Total Processing Latency: {:?}", duration);
}
