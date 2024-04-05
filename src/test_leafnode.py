import unittest

from leafnode import LeafNode

class LeafNodeTest(unittest.TestCase):
    def test_html_render(self):
        node_leaf = LeafNode("Test leaf node", "p", {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node_leaf.to_html(), '<p href="https://google.com" target="_blank">Test leaf node</p>')

    def test_none_value(self):
        with self.assertRaises(ValueError):
            node_leaf = LeafNode(None, "p")
            node_leaf.to_html()

    def test_none_tag(self):
        node_leaf = LeafNode("Value Test", None)
        html = node_leaf.to_html()
        self.assertEqual(html, node_leaf.value)


if __name__ == '__main__':  
    unittest.main()