from pathlib import Path

import pandas as pd

from credit_scoring_mlops.data.column_mapping import COLUMN_MAPPING
from credit_scoring_mlops.data.validation import validate_dataset

PROJECT_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "SouthGermanCredit.asc"


def load_credit_data(file_path: Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """
    Load the South German Credit dataset.

    Parameters
    ----------
    file_path : Path
        Path to the raw dataset file.

    Returns
    -------
    pd.DataFrame
        Loaded credit dataset.

    Raises
    ------
    FileNotFoundError
        If the dataset file does not exist.
    """
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    df = pd.read_csv(file_path, sep=r"\s+")

    df.rename(columns=COLUMN_MAPPING, inplace=True)

    validate_dataset(df)

    return df
