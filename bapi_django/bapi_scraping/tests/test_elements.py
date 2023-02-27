import pytest
import pytest-xdist
import pytest-playwright

def test_visit_elements_page(page):
    
    page.goto("https://www.demoqa.com/elements")
    header_text = page.inner_text(".main-header")

    assert "Elements" in header_text

def test_coppalse_elements_container(page):
    
    page.goto("https://www.demoqa.com/elements")
    element_group = page.wait_for_selector(".element-group")

    page.click(".header-right")

    element_list_class = element_group.eval_on_selector(
        ".element-list", "el => el.className"
    )

    assert "show" not in element_list_class

@pytest.mark.parametrize(
    "button_type",
    [
        ("Double Click", "doubleClickMessage"),
        ("Right Click", "rightClickMessage"),
        ("Click", "dynamicClickMessage"),
    ],
)
def test_click_types(button_type, page):
    """Test that specific click actions provide a result.
    :param button_type: A tuple containing click action and result.
    :param page: A Playwright browser page.
    """
    click_action, result = button_type

    page.goto("https://www.demoqa.com/buttons")

    if click_action == "Double Click":
        page.wait_for_selector("#doubleClickBtn").dblclick()
    elif click_action == "Right Click":
        page.wait_for_selector("#rightClickBtn").click(button="right")
    else:
        page.wait_for_selector("button >> text='Click Me'").click()

    message = page.is_visible(f"#{result}")

    assert message