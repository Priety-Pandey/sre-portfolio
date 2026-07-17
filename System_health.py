# Task 2 - System Health Reporter
# SRE Portfolio - Priety Pandey
# GitHub: github.com/Priety-Pandey

import psutil
import datetime

def get_health_status(percent, warn=70, critical=90):
    if percent >= critical:
        return "🔴 CRITICAL"
    elif percent >= warn:
        return "🟡 WARNING"
    else:
        return "🟢 HEALTHY"

def system_health_report():
    print("=" * 55)
    print("   SYSTEM HEALTH REPORTER - SRE TOOL")
    print("   By Priety Pandey | github.com/Priety-Pandey")
    print("=" * 55)
    print(f"   Report Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)

    # CPU
    cpu = psutil.cpu_percent(interval=1)
    print(f"\n💻 CPU Usage      : {cpu}%  {get_health_status(cpu)}")

    # Memory
    mem = psutil.virtual_memory()
    print(f"🧠 Memory Usage   : {mem.percent}%  {get_health_status(mem.percent)}")
    print(f"   Total RAM      : {round(mem.total / (1024**3), 1)} GB")
    print(f"   Used RAM       : {round(mem.used / (1024**3), 1)} GB")
    print(f"   Available RAM  : {round(mem.available / (1024**3), 1)} GB")

    # Disk
    disk = psutil.disk_usage('C:\\')
    print(f"\n💾 Disk Usage     : {disk.percent}%  {get_health_status(disk.percent)}")
    print(f"   Total Disk     : {round(disk.total / (1024**3), 1)} GB")
    print(f"   Used Disk      : {round(disk.used / (1024**3), 1)} GB")
    print(f"   Free Disk      : {round(disk.free / (1024**3), 1)} GB")

    # Overall Health
    print(f"\n--- OVERALL SYSTEM STATUS ---")
    statuses = [cpu, mem.percent, disk.percent]
    if any(s >= 90 for s in statuses):
        print("🔴 System Status  : CRITICAL — Immediate action needed!")
    elif any(s >= 70 for s in statuses):
        print("🟡 System Status  : WARNING — Monitor closely!")
    else:
        print("🟢 System Status  : HEALTHY — All systems normal!")

    print("\n" + "=" * 55)
    print("✅ Report complete!")
    print("=" * 55)

system_health_report()