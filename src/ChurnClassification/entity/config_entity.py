from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    sourse_url: str
    local_data_file: Path
    unzip_dir: Path
    