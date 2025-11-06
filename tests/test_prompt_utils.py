from langchain_sample import prompt_utils


def test_build_translate_prompt():
    out = prompt_utils.build_translate_prompt("Hello")
    assert "Translate to French:" in out
    assert "Hello" in out


def test_bullet_points_prompt():
    items = ["apple", "banana"]
    out = prompt_utils.bullet_points_prompt(items)
    assert "- apple" in out
    assert "- banana" in out
