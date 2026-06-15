import subprocess
import sys
import time
import webbrowser


def start_camera_monitor():
    print("[INFO] Starting Multi Camera Monitor...")
    return subprocess.Popen(
        [sys.executable, "backend/multi_camera_monitor.py"]
    )


def start_cleanup():
    print("[INFO] Starting Cleanup Service...")
    return subprocess.Popen(
        [sys.executable, "backend/cleanup.py"]
    )


def start_dashboard():
    print("[INFO] Starting Dashboard...")
    return subprocess.Popen(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            "frontend/dashboard.py"
        ]
    )


def open_dashboard():
    time.sleep(5)
    webbrowser.open("http://localhost:8501")


def main():
    camera_process = None
    cleanup_process = None
    dashboard_process = None

    try:
        print("\n🚆 Starting Rakshak AI...\n")

        camera_process = start_camera_monitor()
        cleanup_process = start_cleanup()
        dashboard_process = start_dashboard()

        open_dashboard()

        print("\n✅ Rakshak AI is running successfully!")
        print("📹 Multi Camera Monitor: Active")
        print("🧹 Cleanup Service: Active")
        print("📊 Dashboard: Active")
        print("🌐 Dashboard URL: http://localhost:8501")
        print("\nPress CTRL + C to stop all services.\n")

        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n🛑 Stopping Rakshak AI...\n")

        if camera_process:
            camera_process.terminate()

        if cleanup_process:
            cleanup_process.terminate()

        if dashboard_process:
            dashboard_process.terminate()

        print("✅ Shutdown complete.")


if __name__ == "__main__":
    main()