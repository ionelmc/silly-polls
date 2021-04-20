def test_index(browser, live_server):
    browser.visit(live_server + '/')
    assert browser.is_text_present('Foo')
