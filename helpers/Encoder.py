def to_md5(s: str):
    import hashlib
    encoder = hashlib.md5()
    encoder.update(s.encode('utf-8'))
    return encoder.hexdigest()
