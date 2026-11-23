"""Static configuration: file locations and tunable model constants."""

from pathlib import Path

# --- Paths -------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
TABLES_DIR = PROJECT_ROOT / "tables"

PRESSURE_HUMIDITY_CSV = "pressure-humidity.csv"
WIND_SPEEDS_CSV = "wind_speeds.csv"
STATES_CSV = "states.csv"

# --- Simulation --------------------------------------------------------------
DEFAULT_RUNS = 1095

# --- State grid bounds (indices into the states table) ----------------------
HUMIDITY_LOW = 0
HUMIDITY_HIGH = 16
TEMPERATURE_LOW = 0
TEMPERATURE_HIGH = 23

# --- Navigator ---------------------------------------------------------------
# Base probability weights (percent) for each possible step. Order matters:
# it defines the cumulative ranges used when rolling for a move.
# Moves are (humidity_delta, temperature_delta).
STEP_DELTAS = {
    "stay":       (0, 0),
    "up":         (-1, 0),
    "up_right":   (-1, 1),
    "right":      (0, 1),
    "down_right": (1, 1),
    "down":       (1, 0),
    "down_left":  (1, -1),
    "left":       (0, -1),
    "up_left":    (-1, -1),
}

BASE_STEP_WEIGHTS = {
    "stay":       12,
    "up":         11,
    "up_right":   11,
    "right":      11,
    "down_right": 11,
    "down":       11,
    "down_left":  11,
    "left":       11,
    "up_left":    11,
}

# Percentage-point shift applied to weights to pull the walk towards the centre.
VERTICAL_PC_SHIFT = 1.7
HORIZONTAL_PC_SHIFT = 1.2

# --- Plot --------------------------------------------------------------------
HEXBIN_GRIDSIZE = (12, 8)
