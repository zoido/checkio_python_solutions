from checkio.elementary.right_to_left import left_join


def test_index_power():
    assert left_join(("left", "right", "left",
                      "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright",
                      "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(
        ("brightness wright", )) == "bleftness wleft", "One phrase"
    assert left_join(("enough",
                      "jokes")) == "enough,jokes", "Nothing to replace"
