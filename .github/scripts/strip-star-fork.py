"""3D 잔디 SVG에서 스타 수·포크 수(아이콘+숫자)를 제거한다.
github-profile-3d-contrib 에 숨김 옵션이 없어서 생성 직후 후처리로 지운다."""
import pathlib, re, sys

PATTERN = re.compile(
    r'<g transform="translate\([^)]*\),\s*scale\(2\)">\s*<path[^>]*?(?:/>|></path>)\s*</g>'
    r'\s*<text[^>]*>[^<]*<title>[^<]*</title></text>'
)

for f in pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "profile-3d-contrib").glob("*.svg"):
    src = f.read_text(encoding="utf-8")
    out, n = PATTERN.subn("", src)
    if n:
        f.write_text(out, encoding="utf-8")
    print(f"{f.name}: removed {n}")
