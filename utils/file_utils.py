import os
import pandas as pd
import numpy as np
import yaml
from pathlib import Path

def find_project_root(markers=('pyproject.toml', '.git', 'requirements.txt')) -> str:
    """
    Automatically detects the project root by walking up directories
    until one contains a known marker file or folder.

    Parameters:
    -----------
    markers : tuple
        Filenames or folder names that indicate the root of the project

    Returns:
    --------
    str
        Absolute path to the project root

    Raises:
    -------
    FileNotFoundError
        If no root marker is found in the current or parent directories
    """
    current_path = os.getcwd()
    
    while True:
        if any(os.path.exists(os.path.join(current_path, marker)) for marker in markers):
            return current_path
        
        new_path = os.path.dirname(current_path)
        if new_path == current_path:
            raise FileNotFoundError("🚫 Project root not found. None of the markers exist above current directory.")
        
        current_path = new_path

def get_project_path(*parts) -> str:
    """
    Returns an absolute path by joining to the auto-detected project root.
    """
    root = find_project_root()
    return os.path.join(root, *parts)

def save_df_to_parquet(df: pd.DataFrame, filepath: str, index: bool = False, verbose: bool = True) -> None:
    """
    Saves a DataFrame to Parquet format, ensuring that the directory exists.
    If any column name contains 'date', it will be stored with time set to 00:00:00.

    Parameters:
    -----------
    df : pd.DataFrame
        The DataFrame to save.

    filepath : str
        Full path where the Parquet file should be saved (e.g., 'data/processed/orders_clean.parquet').

    index : bool
        Whether to include the DataFrame index. Default is False.

    verbose : bool
        Whether to print the saved path. Default is True.
    """

    # Ensure folder path exists
    dirpath = os.path.dirname(filepath)
    os.makedirs(dirpath, exist_ok=True)

    # Process date columns
    exclude_substrings = ['flag', 'updated_at', 'created_at']
    date_cols = [
        col for col in df.columns
        if isinstance(col, str)
        and 'date' in col.lower()
        and all(ex_str not in col.lower() for ex_str in exclude_substrings)
    ]
    
    # Normalize date columns to 00:00:00
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce').dt.normalize()

    # Save as Parquet
    df.to_parquet(filepath, index=index)

    if verbose:
        print(f"✅ Saved DataFrame to {filepath}")

def load_config(config_filename: str = "config.yml") -> dict:
    """
    Loads YAML configuration from the project root.

    Parameters
    ----------
    config_filename : str
        Name of the config file (default: config.yml).

    Returns
    -------
    dict
        Parsed configuration settings.
    """
    config_file = Path(get_project_path('config_files', config_filename))

    if not config_file.exists():
        raise FileNotFoundError(f"Config file not found at {config_file.resolve()}")

    with open(config_file, "r") as f:
        config = yaml.safe_load(f)

    return config