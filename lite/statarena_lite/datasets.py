"""Versioned public starter kits for StatArena Lite."""

from dataclasses import dataclass
import errno
import hashlib
from pathlib import Path, PurePosixPath
import shutil
import stat
import tempfile
from urllib.error import URLError
from urllib.request import urlopen
from zipfile import ZipFile


@dataclass(frozen=True)
class Dataset:
    name: str
    url: str
    sha256: str
    root: str = "."


_HUB = "https://huggingface.co/datasets/"
_ATE_CATE = Dataset(
    name="ate-cate",
    url=_HUB + "fuyao11/StatsInference-Arena-ATE-CATE/resolve/"
    "6de515dae59a4b502d6ceb66a03180fd08a46a59/ate-cate-starter-v1.zip",
    sha256="3a19886bb4966af103ed0b5e36a4f16b224e411cf64f47e01789aae6a6159037",
    root="ate-cate-starter-v1",
)

DATASETS: dict[str, Dataset] = {
    "ate": _ATE_CATE,
    "cate": _ATE_CATE,
    "mediation": Dataset(
        name="mediation",
        url=_HUB + "shibo769/StatsInference-Arena-Mediation/resolve/"
        "f70008b2eb4dd82fa9d981d3759ea4dcf5983e33/mediation-starter-v1.zip",
        sha256="c611ca41f36ea08cfc3eceb6f543ca9a4c6b99fe0bf6487d2ae1a7fd4516727e",
    ),
    "iv": Dataset(
        name="iv",
        url=_HUB + "Brownight/StatsInference-Arena-IV/resolve/"
        "f4d6f68c73f745872b46d919a156c2c300476308/iv-starter-v1.zip",
        sha256="04cb3b3c251ce505c312a48bd42deebcf951acbcc54a10619587b4a954f1aecc",
    ),
    "proximal": Dataset(
        name="proximal",
        url=_HUB + "wytzzka/StatsInference-Arena-Proximal/resolve/"
        "2027f348fa54db3db9dd006e2f4d7dcf55282b22/proximal-starter-v1.zip",
        sha256="55bc8e29b91bdcc440a3888a28db57644cd415558836a74d5096c2b4956bb079",
    ),
    "did": Dataset(
        name="did",
        url=_HUB + "lisuo/StatsInference-Arena-DiD/resolve/"
        "ac97ca41e0a8c4797a8fa33d2d0d47c02ce6a87c/did-starter-v1.zip",
        sha256="d29dbf99c8eddd55f3c97c32d66cd8dcd04a2e498d29d84413dfcb848f8463a8",
    ),
}


def _download(dataset: Dataset, archive: Path) -> None:
    checksum = hashlib.sha256()
    try:
        with urlopen(dataset.url, timeout=30) as source, archive.open("wb") as target:
            while chunk := source.read(1024 * 1024):
                checksum.update(chunk)
                target.write(chunk)
    except (URLError, TimeoutError) as exc:
        raise ValueError(f"Could not download the {dataset.name} starter kit: {exc}") from exc

    if checksum.hexdigest() != dataset.sha256:
        raise ValueError(f"SHA-256 verification failed for the {dataset.name} starter kit")


def _extract(archive: Path, target: Path) -> None:
    with ZipFile(archive) as bundle:
        for member in bundle.infolist():
            path = PurePosixPath(member.filename)
            mode = stat.S_IFMT(member.external_attr >> 16)
            if (path.is_absolute() or not path.parts or ".." in path.parts
                    or "\\" in member.filename or ":" in member.filename
                    or mode not in (0, stat.S_IFDIR, stat.S_IFREG)):
                raise ValueError(f"Unsafe ZIP entry: {member.filename!r}")
            destination = target.joinpath(*path.parts)
            if member.is_dir():
                destination.mkdir(parents=True, exist_ok=True)
            else:
                destination.parent.mkdir(parents=True, exist_ok=True)
                with bundle.open(member) as source, destination.open("xb") as output:
                    shutil.copyfileobj(source, output)


def _starter_root(dataset: Dataset, directory: Path) -> Path:
    root = directory / dataset.root
    if not (root / "baseline.py").is_file() or not (root / "score.py").is_file():
        raise ValueError(f"Incomplete {dataset.name} starter kit at {directory}")
    return root


def prepare(dataset: Dataset, cache_dir: Path) -> Path:
    """Download, verify, and cache the requested public starter kit."""
    cache_dir = cache_dir.expanduser().resolve()
    destination = cache_dir / dataset.sha256
    if destination.exists():
        return _starter_root(dataset, destination)

    cache_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".download-", dir=cache_dir) as work:
        archive = Path(work) / "starter.zip"
        extracted = Path(work) / "extracted"
        _download(dataset, archive)
        _extract(archive, extracted)
        _starter_root(dataset, extracted)
        try:
            extracted.rename(destination)
        except OSError as exc:
            if exc.errno not in (errno.EEXIST, errno.ENOTEMPTY) or not destination.is_dir():
                raise
            # Another invocation published this verified kit during the download.

    return _starter_root(dataset, destination)
