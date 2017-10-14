from checkio.electronic_station.roman_numerals import checkio


def test_checkio():
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'


def test_checkio_extra_all_small():
    assert checkio(1) == 'I'
    assert checkio(2) == 'II'
    assert checkio(3) == 'III'
    assert checkio(4) == 'IV'
    assert checkio(5) == 'V'
    assert checkio(6) == 'VI'
    assert checkio(7) == 'VII'
    assert checkio(8) == 'VIII'
    assert checkio(9) == 'IX'


def test_checkio_extra():
    assert checkio(25) == 'XXV'
