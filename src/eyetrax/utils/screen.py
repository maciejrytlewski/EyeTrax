from screeninfo import get_monitors


def get_monitor_geometry(monitor_index: int = 0):
    monitors = get_monitors()
    if monitor_index < 0 or monitor_index >= len(monitors):
        raise ValueError(
            f"Invalid monitor_index {monitor_index}, available: 0-{len(monitors)-1}"
        )
    m = monitors[monitor_index]
    return m.x, m.y, m.width, m.height
