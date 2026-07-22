#!/usr/bin/env python
"Generate the per-tool plugin skill trees in `plugins/` from the shared sources in `src/skills`: each SKILL.md is a jinja2 template rendered per tool with `tool` ('codex' or 'claude') and `name` (that tool's built skill name) in context, and a `src/skills/<name>/<tool>/` dir is copied verbatim into that tool's output. A `SKILLS` value may be a `{tool: output_name}` dict when the built skill is named differently per tool."
import re,shutil,sys
from pathlib import Path
from jinja2 import Environment, StrictUndefined

ROOT = Path(__file__).parent
BOTH = ('codex','claude')
SKILLS = {'coding-patterns': BOTH, 'persistent-python': BOTH, 'nbdev-editing': BOTH,
    'write-prose': BOTH, 'docs': dict(codex='codex-docs', claude='claude-code-docs')}
PLUGINS = dict(codex='codex-aai', claude='claude-aai')
_env = Environment(trim_blocks=True, lstrip_blocks=True, undefined=StrictUndefined)


def render(src, tool, name):
    "Render a skill source for `tool`, with `name` that tool's built skill name"
    return _env.from_string(src).render(tool=tool, name=name)


def build(check=False):
    "Write every target skill; with `check`, write nothing and return the stale output paths. Otherwise return the tools whose outputs changed"
    stale,changed = [],set()
    for name, tools in SKILLS.items():
        d = ROOT/'src'/'skills'/name
        for tool in tools:
            outname = tools[tool] if isinstance(tools, dict) else name
            out = ROOT/'plugins'/PLUGINS[tool]/'skills'/outname
            txt = render((d/'SKILL.md').read_text(), tool, outname).rstrip() + '\n'
            cur = (out/'SKILL.md').read_text() if (out/'SKILL.md').exists() else None
            if check:
                if cur != txt: stale.append(str(out/'SKILL.md'))
            else:
                if cur != txt: changed.add(tool)
                out.mkdir(parents=True, exist_ok=True)
                (out/'SKILL.md').write_text(txt)
                if (d/tool).exists():
                    for f in (x for x in (d/tool).rglob('*') if x.is_file()):
                        dst = out/f.relative_to(d/tool)
                        if not dst.exists() or dst.read_bytes() != f.read_bytes(): changed.add(tool)
                    shutil.copytree(d/tool, out, dirs_exist_ok=True)
    return stale if check else changed


def bump(tools):
    "Bump the patch version in each tool's plugin.json (a surgical text edit, preserving formatting), returning `{plugin: new_version}`"
    res = {}
    for tool in sorted(tools):
        p = ROOT/'plugins'/PLUGINS[tool]/f'.{tool}-plugin'/'plugin.json'
        txt = p.read_text()
        m = re.search(r'"version": "(\d+)\.(\d+)\.(\d+)"', txt)
        ver = f'{m[1]}.{m[2]}.{int(m[3])+1}'
        p.write_text(txt[:m.start()] + f'"version": "{ver}"' + txt[m.end():])
        res[PLUGINS[tool]] = ver
    return res


if __name__ == '__main__':
    if '--check' in sys.argv:
        if (stale := build(check=True)): sys.exit('stale outputs, run ./build.py:\n' + '\n'.join(stale))
    else:
        changed = build()
        if changed and '--no-bump' not in sys.argv:
            for name, ver in bump(changed).items(): print(f'{name} -> {ver}')
