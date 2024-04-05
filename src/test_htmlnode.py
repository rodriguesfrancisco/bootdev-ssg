import unittest

from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode("Test Tag", "Test Value", "Test Children", {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(html_node.props_to_html(), ' href="https://google.com" target="_blank"')

    def test_props_to_html_when_props_is_none(self):
        html_node = HTMLNode("Test Tag", "Test Value", "Test Children", None)
        self.assertEqual(html_node.props_to_html(), "")