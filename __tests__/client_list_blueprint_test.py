from ward import test
from __tests__.fixtures import browser
from __tests__.factories.client_factory import ClientFactory
from flask import url_for


@test("Main page must be online")
def _(browser=browser):

    browser.visit(url_for("client_list.index"))
    assert browser.is_text_present("Hello Flask!")


@test("Visitor accesses main page and visualize clients")
def _(browser=browser):
    client = ClientFactory.create()

    browser.visit(url_for("client_list.index"))

    assert browser.is_text_present(client.name)


@test("Visitor can't visualize any clients")
def _(browser=browser):
    browser.visit(url_for("client_list.index"))
    assert browser.is_text_present("No client registered.")
