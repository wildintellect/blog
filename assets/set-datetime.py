import panflute as pf

def action(elem, doc):
    if isinstance(elem, pf.Str):
        keyword = "Posted:"
        if elem.text == keyword:
            date = " ".join([
                elem.next.next.text
                ,elem.next.next.next.next.text
                ,"-0700"])
            doc.metadata['date'] = date

if __name__ == "__main__":
    pf.toJSONFilter(action)
