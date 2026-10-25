"""Safely export submitted generator.py source for GitHub viewing/downloading.

NEVER import, compile, run, or otherwise execute untrusted contributor code.
The exported code is exactly the UTF-8 source from the selected ZIP member.
"""
from __future__ import annotations

import hashlib
import re
import zipfile
from pathlib import Path

from .zip_reader import safe_zip

_MAX_SOURCE_BYTES = 2 * 1024 * 1024
_RECORD_ID = re.compile(r"^[a-z0-9][a-z0-9-]{1,127}$")


def export_generators(records, registry_dir: Path, notes):
    """Export one source file per indexed DGP; record links only after success."""
    root = Path(registry_dir) / "generators"
    root.mkdir(parents=True, exist_ok=True)
    for old in root.glob("*.py"):
        old.unlink()

    for rec in records:
        impl = rec.setdefault("implementation", {})
        impl.pop("exported_generator_path", None)
        impl.pop("exported_generator_sha256", None)
        member = impl.get("generator_reference")
        source = (rec.get("provenance") or {}).get("submission_file")
        rid = rec.get("record_id")
        if not member or not source or not _RECORD_ID.fullmatch(str(rid)):
            continue
        if not (member == "generator.py" or member.endswith("/generator.py")):
            rec.setdefault("warnings", []).append("Unexpected generator path: no source link published.")
            continue
        try:
            with zipfile.ZipFile(source) as archive:
                safe_zip(archive)
                info = archive.getinfo(member)
                if info.is_dir() or info.file_size > _MAX_SOURCE_BYTES:
                    raise ValueError("generator.py is a directory or exceeds 2 MiB")
                raw = archive.read(info)
        except (OSError, KeyError, ValueError, zipfile.BadZipFile) as exc:
            notes.append("Unable to export generator for " + rid + ": " + str(exc))
            rec.setdefault("warnings", []).append("Generator export failed; source ZIP remains unchanged.")
            continue
        if len(raw) > _MAX_SOURCE_BYTES or b"\x00" in raw:
            rec.setdefault("warnings", []).append("Generator cannot be displayed as UTF-8 source.")
            continue
        try:
            raw.decode("utf-8-sig")
        except UnicodeDecodeError:
            rec.setdefault("warnings", []).append("Generator is not UTF-8; source retained only inside ZIP.")
            continue

        destination = root / (rid + ".py")
        destination.write_bytes(raw)
        impl["exported_generator_path"] = "generators/" + rid + ".py"
        impl["exported_generator_sha256"] = hashlib.sha256(raw).hexdigest()

    return sum(bool((r.get("implementation") or {}).get("exported_generator_path"))
               for r in records)
