# Task 4 - Alert Noise Reducer
# SRE Portfolio - Priety Pandey
# GitHub: github.com/Priety-Pandey

import datetime

ALERTS = [
    {"id": 1,  "time": "08:01:00", "service": "OpsRamp-Agent",   "message": "CPU usage high"},
    {"id": 2,  "time": "08:01:45", "service": "OpsRamp-Agent",   "message": "CPU usage high"},
    {"id": 3,  "time": "08:02:30", "service": "OpsRamp-Agent",   "message": "CPU usage high"},
    {"id": 4,  "time": "08:03:00", "service": "Database",        "message": "Connection timeout"},
    {"id": 5,  "time": "08:03:10", "service": "OpsRamp-Agent",   "message": "CPU usage high"},
    {"id": 6,  "time": "08:04:00", "service": "Database",        "message": "Connection timeout"},
    {"id": 7,  "time": "08:04:30", "service": "Dynatrace-Agent", "message": "Memory usage high"},
    {"id": 8,  "time": "08:05:00", "service": "Database",        "message": "Connection timeout"},
    {"id": 9,  "time": "08:05:30", "service": "Dynatrace-Agent", "message": "Memory usage high"},
    {"id": 10, "time": "08:06:00", "service": "OpsRamp-Agent",   "message": "CPU usage high"},
    {"id": 11, "time": "08:06:30", "service": "Dynatrace-Agent", "message": "Memory usage high"},
    {"id": 12, "time": "08:07:00", "service": "Database",        "message": "Connection timeout"},
]

def parse_time(t):
    return datetime.datetime.strptime(t, "%H:%M:%S")

def reduce_alert_noise(alerts, suppress_window=300, max_count=3):
    print("=" * 60)
    print("   ALERT NOISE REDUCER - SRE TOOL")
    print("   By Priety Pandey | github.com/Priety-Pandey")
    print("=" * 60)
    print(f"\n📥 Total Alerts Received : {len(alerts)}")
    print(f"⚙️  Suppress Window       : {suppress_window} seconds")
    print(f"⚙️  Max Alerts Allowed    : {max_count} per window")
    print("\n" + "=" * 60)

    # Track  — service + message combination
    tracker = {}
    fired = []
    suppressed = []

    for alert in alerts:
        key = f"{alert['service']}|{alert['message']}"
        alert_time = parse_time(alert['time'])

        if key not in tracker:
            tracker[key] = {"count": 1, "first_time": alert_time}
            fired.append(alert)
        else:
            time_diff = (alert_time - tracker[key]["first_time"]).total_seconds()

            if time_diff <= suppress_window:
                tracker[key]["count"] += 1
                if tracker[key]["count"] <= max_count:
                    fired.append(alert)
                else:
                    suppressed.append(alert)
            else:
                # Window reset
                tracker[key] = {"count": 1, "first_time": alert_time}
                fired.append(alert)

    # Fired alerts
    print(f"\n✅ ALERTS FIRED ({len(fired)}):")
    print(f"{'ID':<5} {'Time':<10} {'Service':<20} {'Message'}")
    print("-" * 55)
    for a in fired:
        print(f"{a['id']:<5} {a['time']:<10} {a['service']:<20} {a['message']}")

    # Suppressed alerts
    print(f"\n🔕 ALERTS SUPPRESSED ({len(suppressed)}):")
    print(f"{'ID':<5} {'Time':<10} {'Service':<20} {'Message'}")
    print("-" * 55)
    for a in suppressed:
        print(f"{a['id']:<5} {a['time']:<10} {a['service']:<20} {a['message']}")

    # Summary
    noise_reduction = round((len(suppressed) / len(alerts)) * 100, 1)
    print("\n" + "=" * 60)
    print(f"--- NOISE REDUCTION SUMMARY ---")
    print(f"📥 Total Alerts     : {len(alerts)}")
    print(f"✅ Alerts Fired     : {len(fired)}")
    print(f"🔕 Alerts Suppressed: {len(suppressed)}")
    print(f"📉 Noise Reduced    : {noise_reduction}%")

    if noise_reduction >= 30:
        print(f"🟢 Great job! Significant noise reduction achieved!")
    elif noise_reduction >= 10:
        print(f"🟡 Moderate noise reduction — tuning recommended!")
    else:
        print(f"🔴 Low noise reduction — review alert rules!")

    print("\n" + "=" * 60)
    print("✅ Alert analysis complete!")
    print("=" * 60)

reduce_alert_noise(ALERTS)