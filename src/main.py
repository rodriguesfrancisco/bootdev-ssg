from leafnode import LeafNode
from textnode import TextNode
from htmlnode import HTMLNode

def main():
    text_node = TextNode("This is a text node", "bold", "https://boot.dev")
    print(text_node)
    html_node = HTMLNode("Test", "Test Value", "Test Children", {"href": "https://google.com"})
    print(html_node.props_to_html())
    node_leaf = LeafNode("Test leaf node", "p", {"href": "https://google.com"})
    print(node_leaf.to_html())

main()
