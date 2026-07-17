# Task 3 - Uptime Monitor
# SRE Portfolio - Priety Pandey
# GitHub: github.com/Priety-Pandey

import requests
import datetime

WEBSITES = [
    "https://www.google.com",
    "https://www.github.com",
    "https://www.dynatrace.com",
    "https://www.linkedin.com",
    "https://www.fujitsu.com"
]

def check_website(url):
    try:
        start = datetime.datetime.now()
        response = requests.get(url, timeout=5)
        end = datetime.datetime.now()
        response_time = round((end - start).total_seconds() * 1000, 2)

        if response.status_code == 200:
            status = "🟢 UP"
        else:
            status = "🟡 DEGRADED"

        return status, response_time, response.status_code

    except requests.exceptions.ConnectionError:
        return "🔴 DOWN", None, "Connection Error"
    except requests.exceptions.Timeout:
        return "🔴 DOWN", None, "Timeout"
    except Exception as e:
        return "🔴 DOWN", None, str(e)

def uptime_monitor():
    print("=" * 60)
    print("   UPTIME MONITOR - SRE TOOL")
    print("   By Priety Pandey | github.com/Priety-Pandey")
    print("=" * 60)
    print(f"   Check Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    up_count = 0
    down_count = 0
    results = []

    print(f"\n{'Website':<35} {'Status':<15} {'Response Time':<15} {'HTTP Code'}")
    print("-" * 75)

    for url in WEBSITES:
        status, response_time, code = check_website(url)
        rt = f"{response_time} ms" if response_time else "N/A"
        # URL short karo display ke liye
        short_url = url.replace("https://www.", "")
        print(f"{short_url:<35} {status:<15} {rt:<15} {code}")

        if "UP" in status:
            up_count += 1
        else:
            down_count += 1

        results.append((url, status, response_time))

    # Summary
    total = len(WEBSITES)
    availability = round((up_count / total) * 100, 1)

    print("\n" + "=" * 60)
    print(f"--- SUMMARY ---")
    print(f"✅ UP      : {up_count}/{total} websites")
    print(f"❌ DOWN    : {down_count}/{total} websites")
    print(f"📊 Availability : {availability}%")

    # SLO Check
    print(f"\n--- SLO STATUS ---")
    if availability >= 99.9:
        print("🟢 SLO MET     : 99.9% target achieved!")
    elif availability >= 95.0:
        print("🟡 SLO AT RISK : Below 99.9% target!")
    else:
        print("🔴 SLO BREACHED: Immediate action needed!")

    print("\n" + "=" * 60)
    print("✅ Uptime check complete!")
    print("=" * 60)

uptime_monitor()