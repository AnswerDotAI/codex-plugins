import build


def test_render():
    src = "a\n<!-- claude -->\nc1\n<!-- /claude -->\n<!-- codex -->\nx1\n<!-- /codex -->\nb\n"
    assert build.render(src, 'claude') == "a\nc1\nb\n"
    assert build.render(src, 'codex') == "a\nx1\nb\n"
    inline = "pre <!-- claude -->A<!-- /claude --><!-- codex -->B<!-- /codex --> post\n"
    assert build.render(inline, 'claude') == "pre A post\n"
    assert build.render(inline, 'codex') == "pre B post\n"


def test_build_roundtrip():
    build.build()
    assert not build.build(check=True)          # freshly built: nothing stale
    for p in (build.ROOT/'plugins').glob('*/skills/*/SKILL.md'):
        t = p.read_text()
        assert '<!--' not in t and t.startswith('---\n')   # outputs marker-free, frontmatter intact
    ya = build.ROOT/'plugins/codex-aai/skills/write-prose/agents/openai.yaml'
    assert ya.exists()                                      # codex-only extras copied
    assert not (build.ROOT/'plugins/claude-aai/skills/write-prose/agents').exists()
