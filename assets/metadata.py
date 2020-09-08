from pandocfilters import toJSONFilter, Null

def behead(key, value, format, meta):
    meta["layout"] = {"t": "MetaString", "c": "post"}

    if key == "Header" and value[0] == 1 and "title" not in meta:
        meta["title"] = {"t": "MetaInlines", "c": value[2]}
        return Null()

    meta["date"] = {"t": "MetaString", "c": "0000-00-00"}

if __name__ == "__main__":
    toJSONFilter(behead)
