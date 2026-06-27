from tree_sitter import Language, Parser
import tree_sitter_python
from pathlib import Path

def extract_chunks(file_path: str) -> list:
    code = Path(file_path).read_text(encoding="utf-8")
    
    py_lang = Language(tree_sitter_python.language())
    parser = Parser(py_lang)
    tree = parser.parse(bytes(code, "utf-8"))
    root = tree.root_node
    
    chunks = []
    
    def parse_node(node):
        for child in node.children:
            parse_node(child)
            if child.type == "function_definition":
                chunks.append({
                    "name": child.child_by_field_name("name").text.decode("utf-8"),
                    "code": code[child.start_byte:child.end_byte],
                    "start_line": child.start_point[0] + 1,
                    "end_line": child.end_point[0] + 1,
                })
    
    parse_node(root)
    return chunks


if __name__ == "__main__":
    chunks = extract_chunks("./Chunk/test_file.py")
    for chunk in chunks:
        print(f"{chunk['name']} | lines {chunk['start_line']}-{chunk['end_line']}")