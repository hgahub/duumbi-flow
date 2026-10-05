"""Validate this package's metadata and simple inline Markdown file links."""
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


def read_mapping(path):
    value = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("expected a YAML mapping")
    return value


def validate_skill(folder):
    errors = []
    try:
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
        if not match:
            raise ValueError("missing YAML frontmatter")
        meta = yaml.safe_load(match.group(1))
        if not isinstance(meta, dict):
            raise ValueError("expected frontmatter mapping")
        name = meta.get("name")
        if (not isinstance(name, str) or name != folder.name
                or len(name) > 64 or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)):
            errors.append("name must match the folder and use lowercase kebab-case")
        description = meta.get("description")
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            errors.append("description must contain 1–1024 characters")
        if not text[match.end():].strip():
            errors.append("skill body is empty")
        interface = read_mapping(folder / "agents/openai.yaml").get("interface")
        if not isinstance(interface, dict):
            raise ValueError("missing interface mapping")
        for field in ("display_name", "short_description", "default_prompt"):
            if not isinstance(interface.get(field), str) or not interface[field].strip():
                errors.append(f"interface.{field} must be nonempty text")
        short = interface.get("short_description")
        if isinstance(short, str) and not 25 <= len(short) <= 64:
            errors.append("short_description must contain 25–64 characters")
        prompt = interface.get("default_prompt", "")
        if isinstance(prompt, str) and f"${folder.name}" not in prompt:
            errors.append("default_prompt must reference the skill by $name")
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(str(exc))
    return errors


def validate_links(path, root):
    """Check inline links; fenced examples and external URLs are out of scope."""
    root = root.resolve()
    path = path.resolve()
    relative = path.relative_to(root)
    boundary = root
    if len(relative.parts) >= 3 and relative.parts[0] == "skills":
        boundary = root / "skills" / relative.parts[1]
    errors = []
    fence = None
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        for match in re.finditer(r'!?\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\)', line):
            target = match.group(1).strip("<>")
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(boundary):
                errors.append(f"line {line_number}: link escapes package boundary: {target}")
            elif not resolved.exists():
                errors.append(f"line {line_number}: missing local target: {target}")
    return errors


def validate(root):
    errors = []
    for required in ("README.md", "LICENSE", "docs/methodology.md", "docs/workflow.md"):
        if not (root / required).is_file():
            errors.append(f"{required}: required file is missing")
    folders = sorted(p for p in (root / "skills").glob("*") if p.is_dir())
    if not folders:
        errors.append("no skills found")
    for folder in folders:
        errors.extend(f"{folder.relative_to(root)}: {e}" for e in validate_skill(folder))
    documents = list(root.glob("*.md"))
    for directory in ("docs", "skills", "examples"):
        documents.extend((root / directory).rglob("*.md"))
    for path in sorted(documents):
        errors.extend(f"{path.relative_to(root)}: {e}" for e in validate_links(path, root))
    return errors


if __name__ == "__main__":
    errors = validate(Path(__file__).resolve().parents[1])
    for error in errors:
        print(error, file=sys.stderr)
    if not errors:
        print("Package validation passed.")
    sys.exit(bool(errors))
