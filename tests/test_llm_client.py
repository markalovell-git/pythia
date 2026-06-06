from app.frontend.services.llm_client import trim_to_last_sentence


def test_already_ends_cleanly_is_unchanged():
    assert trim_to_last_sentence("All done here.") == "All done here."
    assert trim_to_last_sentence("Really?") == "Really?"
    assert trim_to_last_sentence("Wow!") == "Wow!"


def test_trailing_whitespace_stripped():
    assert trim_to_last_sentence("Done.   \n") == "Done."


def test_mid_sentence_cutoff_trimmed_back():
    # Only the period is a sentence end; the trailing fragment is dropped.
    text = "Saturn is testing you right now. The pressure eases by winter though, so han"
    assert trim_to_last_sentence(text) == "Saturn is testing you right now."


def test_no_sentence_boundary_returned_as_is():
    # A single unfinished clause with no punctuation can't be trimmed sensibly.
    assert trim_to_last_sentence("this got cut off immediately") == "this got cut off immediately"


def test_empty_string():
    assert trim_to_last_sentence("") == ""
    assert trim_to_last_sentence("   ") == ""


def test_ellipsis_counts_as_sentence_end():
    assert trim_to_last_sentence("Let me think…") == "Let me think…"
