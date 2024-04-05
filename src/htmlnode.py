
class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"Tag={self.tag}, Value={self.value}, Children={self.children}, Props={self.props}"

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(f' {k}="{v}"' for k,v in self.props.items())