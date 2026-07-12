#!/usr/bin/env python
"Generate the per-tool plugin skill trees in `plugins/` from the shared sources in `src/skills`: conditional regions (`<!-- codex -->...<!-- /codex -->`, whole-line or inline) are kept for that tool and dropped for the others, and a `src/skills/<name>/<tool>/` dir is copied verbatim into that tool's output."
import re,shutil,sys
from pathlib import Path

ROOT = Path(__file__).parent
BOTH = ('codex','claude')
SKILLS = {'coding-patterns': BOTH, 'persistent-python': BOTH, 'nbdev-editing': BOTH,
    'write-prose': BOTH, 'codex-docs': ('codex',)}
PLUGINS = dict(codex='codex-aai', claude='claude-aai')
_COND = re.compile(r'<!-- (\w+) -->\n?(.*?)<!-- /\1 -->\n?', re.S)


def render(src, tool):
    "Resolve conditional regions: keep `tool`'s contents, drop other tools'"
    return _COND.sub(lambda m: m[2] if m[1] == tool else '', src)


def build(check=False):
    "Write every target skill; with `check`, write nothing and return the stale output paths"
    stale = []
    for name, tools in SKILLS.items():
        d = ROOT/'src'/'skills'/name
        for tool in tools:
            out = ROOT/'plugins'/PLUGINS[tool]/'skills'/name
            txt = render((d/'SKILL.md').read_text(), tool).rstrip() + '\n'
            if check:
                if not (out/'SKILL.md').exists() or (out/'SKILL.md').read_text() != txt: stale.append(str(out/'SKILL.md'))
            else:
                out.mkdir(parents=True, exist_ok=True)
                (out/'SKILL.md').write_text(txt)
                if (d/tool).exists(): shutil.copytree(d/tool, out, dirs_exist_ok=True)
    return stale


if __name__ == '__main__':
    if '--check' in sys.argv:
        if (stale := build(check=True)): sys.exit('stale outputs, run ./build.py:\n' + '\n'.join(stale))
    else: build()
