"""Every shipped template must produce a runtm.yaml that passes manifest validation (#47)."""

from pathlib import Path

import pytest

from runtm_shared.manifest import Manifest
from runtm_shared.types import MachineTier

TEMPLATES_DIR = Path(__file__).resolve().parents[3] / "templates"
TEMPLATE_MANIFESTS = sorted(TEMPLATES_DIR.glob("*/runtm.yaml"))


def test_templates_found() -> None:
    assert TEMPLATE_MANIFESTS, f"no template manifests found under {TEMPLATES_DIR}"


@pytest.mark.parametrize("path", TEMPLATE_MANIFESTS, ids=lambda p: p.parent.name)
def test_template_manifest_validates(path: Path) -> None:
    manifest = Manifest.from_yaml(path.read_text(encoding="utf-8"))
    assert manifest.template == path.parent.name
    assert manifest.get_machine_tier() in MachineTier
