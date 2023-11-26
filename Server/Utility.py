from bson import ObjectId

def serialize_doc(doc):
    if isinstance(doc, list):
        return [serialize_doc(subdoc) for subdoc in doc]
    if not isinstance(doc, dict):
        return doc
    return {k: str(v) if isinstance(v, ObjectId) else v for k, v in doc.items()}
