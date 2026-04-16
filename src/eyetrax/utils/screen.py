from screeninfo import get_monitors


def get_monitor_geometry(monitor_index: int = 0):
    monitors = get_monitors()
    if monitor_index < 0 or monitor_index >= len(monitors):
        raise ValueError(
            f"Invalid monitor_index {monitor_index}, available: 0-{len(monitors)-1}"
        )
    m = monitors[monitor_index]
    
    try:
        x, y, width, height = int(m.x), int(m.y), int(m.width), int(m.height)
    except (AttributeError, TypeError, ValueError):
        raise ValueError(f"Invalid monitor data: {m}")

    if width <= 0 or height <= 0:
        raise ValueError(
            f"Invalid monitor dimensions: width={width}, height={height}"
        )

    return x, y, width, height
