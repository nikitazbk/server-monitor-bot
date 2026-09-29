from config import CPU_THRESHOLD, RAM_THRESHOLD, DISK_THRESHOLD


def check_thresholds(metrics):
    alerts = []

    if metrics["cpu"] > CPU_THRESHOLD:
        alerts.append(
            f"⚠️ CPU: {metrics['cpu']}% "
            f"(порог {CPU_THRESHOLD}%)"
        )

    if metrics["ram"] > RAM_THRESHOLD:
        alerts.append(
            f"⚠️ RAM: {metrics['ram']}% "
            f"(порог {RAM_THRESHOLD}%)"
        )

    if metrics["disk"] > DISK_THRESHOLD:
        alerts.append(
            f"⚠️ Disk: {metrics['disk']}% "
            f"(порог {DISK_THRESHOLD}%)"
        )

    return alerts