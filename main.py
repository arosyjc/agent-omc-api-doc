from tree_sitter import Language, Parser
import os

# define JAVA grammar path
# java1.8.0
JAVA_GRAMMAR_PATH = "./java1.8"
if not os.path.exists(JAVA_GRAMMAR_PATH):
    from tree_sitter import Language
    import subprocess

    repo_url = "https://github.com/tree-sitter/tree-sitter-java"
    target_dir = "java1.8"
    # create target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    # 参数必须平铺列表，一个字符串一个元素
    subprocess.run(["git", "clone", repo_url, target_dir], check=True)

# 编译语法
lang_lib = Language.build_library("languages.so", [JAVA_GRAMMAR_PATH])
JAVA_LANG = Language(lang_lib, "java")
parser = Parser()
parser.set_language(JAVA_LANG)

# java code root path
src_code_path="/mnt/e/projects/cnr/omc-live"
# java code relative path
java_code_path = "live/src/main/java"
# package path
package_path = "com.yunting.live"
# whole path cancat with '/'
whole_path = os.path.join(src_code_path, java_code_path, package_path.replace('.', '/'))

print("Whole path:", whole_path)
def main():
    print("Hello from omc-api-doc!")


if __name__ == "__main__":
    main()
