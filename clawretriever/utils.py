def clean_text(text: str) -> str:
    """Basic text cleanup."""
    return " ".join(text.split())

def validate_config(config: dict):
    """Ensure required configuration keys are present."""
    required = ["data_dir", "index_path"]
    for key in required:
        if key not in config:
            raise ValueError(f"Missing config key: {key}")
