# agent-omc-api-doc

# 安装 tree-sitter cli
npm install -g tree-sitter-cli
# 编译 java grammar 生成 languages.so
tree-sitter build --output languages.so ./tree-sitter-java/src

from tree_sitter import Language, Parser

# 直接加载提前编译好的so，无编译逻辑
java_lang = Language("languages.so", "java")
parser = Parser(java_lang) # 新版不用 set_language，构造器传入