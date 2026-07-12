import subprocess
import sys
from pathlib import Path

print("=" * 60)
print("Bluestock Mutual Fund ETL Pipeline")
print("=" * 60)

# Folder containing this script
scripts_dir = Path(__file__).parent

scripts = [
    "clean_nav.py",
    "clean_transactions.py",
    "clean_performance.py",
    "load_sqlite.py"
]

for script in scripts:

    script_path = scripts_dir / script

    print(f"\nRunning {script}...")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        text=True
    )

    if result.returncode == 0:
        print(f"✅ {script} completed successfully.")
    else:
        print(f"❌ Error while running {script}")
        break

print("\n🎉 ETL Pipeline Finished.")