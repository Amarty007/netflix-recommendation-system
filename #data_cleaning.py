
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent
RAW_DATA = PROJECT_ROOT / "data" / "raw" / "netflix.csv"
PROCESSED_DATA = PROJECT_ROOT / "data" / "processed"
CLEANED_DATA = PROCESSED_DATA / "cleaned_netflix.csv"
FALLBACK_DATA = PROJECT_ROOT / "netflix_features.csv"


def resolve_dataset() -> Path:
    """Resolve the raw or bundled Netflix dataset without relying on cwd."""
    candidates = (
        RAW_DATA,
        PROJECT_ROOT / "netflix.csv",
        FALLBACK_DATA,
        PROJECT_ROOT / "data" / "processed" / "netflix_features.csv",
    )
    for candidate in candidates:
        if candidate.is_file():
            return candidate

    expected = [str(path.relative_to(PROJECT_ROOT)) for path in candidates]
    raise FileNotFoundError(f"Netflix CSV not found. Checked: {', '.join(expected)}")


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove incomplete rows without mutating the input DataFrame.

    Time: O(n * c), where n is the row count and c is the column count.
    Space: O(k * c), where k is the number of rows retained.
    """
    return df.dropna().reset_index(drop=True)


def main() -> None:
    source = resolve_dataset()
    df = pd.read_csv(source)
    cleaned_df = clean_data(df)

    PROCESSED_DATA.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(CLEANED_DATA, index=False)
    print("Data cleaning completed")


if __name__ == "__main__":
    main()
