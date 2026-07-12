# Task 1 - Log File Analyser
# SRE Portfolio - Priety Pandey
# GitHub: github.com/Priety-Pandey

import datetime

def analyse_log(file_path):
    
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    errors = []
    warnings = []

    print("=" * 50)
    print("   LOG FILE ANALYSER - SRE TOOL")
    print("   By Priety Pandey | github.com/Priety-Pandey")
    print("=" * 50)

    # File 
    with open(file_path, "r") as f:
        lines = f.readlines()

    total_lines = len(lines)

    for line in lines:
        line = line.strip()
        if "INFO" in line:
            counts["INFO"] += 1
        elif "WARNING" in line:
            counts["WARNING"] += 1
            warnings.append(line)
        elif "ERROR" in line:
            counts["ERROR"] += 1
            errors.append(line)

    # Summary print 
    print(f"\n📄 File: {file_path}")
    print(f"📊 Total Lines: {total_lines}")
    print(f"\n--- LOG SUMMARY ---")
    print(f"✅ INFO     : {counts['INFO']}")
    print(f"⚠️  WARNING  : {counts['WARNING']}")
    print(f"❌ ERROR    : {counts['ERROR']}")

    # Health Score
    error_pct = (counts["ERROR"] / total_lines) * 100
    print(f"\n--- SYSTEM HEALTH ---")
    if error_pct == 0:
        print("🟢 Status: HEALTHY")
    elif error_pct <= 20:
        print("🟡 Status: NEEDS ATTENTION")
    else:
        print("🔴 Status: CRITICAL")

    print(f"📉 Error Rate: {error_pct:.1f}%")

    # Errors 
    if errors:
        print(f"\n--- ERRORS FOUND ---")
        for e in errors:
            print(f"  ❌ {e}")

    # Warnings 
    if warnings:
        print(f"\n--- WARNINGS FOUND ---")
        for w in warnings:
            print(f"  ⚠️  {w}")

    print("\n" + "=" * 50)
    print(f"✅ Analysis complete — {datetime.datetime.now()}")
    print("=" * 50)

# Run 
analyse_log("sample.log")
