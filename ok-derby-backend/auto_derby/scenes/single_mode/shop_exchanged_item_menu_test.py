from typing import Text

from ... import _test
from .shop_exchanged_item_menu import ShopExchangedItemMenuScene
from ...single_mode import Context
import pytest


@pytest.mark.parametrize(
    "name",
    tuple(
        i.stem
        for i in (
            (_test.DATA_PATH / "single_mode").glob("shop_exchanged_item_menu_*.png")
        )
    ),
)
def test_recognize(name: Text):
    _test.use_screenshot(f"single_mode/{name}.png")
    scene = ShopExchangedItemMenuScene()
    ctx = Context.new()
    scene.recognize(ctx, static=True)
    _test.snapshot_match(
        scene,
        name=name,
    )
