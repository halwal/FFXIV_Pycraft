import pytest

from ffxiv_pycraft.item import Item

@pytest.fixture()
def item():
    name = 'Griffin Leather Tricorne of Striking'
    doh_class = 'LTW'
    lvl = '60**'
    rlvl = 180
    durability = 70
    progress = 1436
    quality = 9430

    return Item( name, doh_class, lvl, rlvl, durability, progress, quality)

def test_init(item):
    assert item.name == 'Griffin Leather Tricorne of Striking'
    assert item.doh_class == 'LTW'
    assert item.lvl == '60**'
    assert item.rlvl == 180
    assert item.durability == 70
    assert item.progress == 1436
    assert item.quality == 9430