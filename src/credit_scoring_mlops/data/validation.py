import pandas as pd


def validate_dataset(df: pd.DataFrame) -> dict[str, int | bool]:
    """
    Validate basic data quality conditions.
    """

    if df.empty:
        raise ValueError("The dataset is empty.")

    validation_report = {
        "is_empty": df.empty,
        "rows": len(df),
        "columns": len(df.columns),
        "missing_values": int(df.isna().sum().sum()),
        "duplicate_rows": int(df.duplicated().sum()),
    }

    return validation_report
