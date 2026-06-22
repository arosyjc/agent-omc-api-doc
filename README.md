# agent-omc-api-doc
1.using tree-sitter and tree-sitter-java to parse JAVA WEB Project to generate API doc
2.using LLM like (Deepseek/Openai/Anthoropic,and so on)to summarize Java Controller
3.generate OpenAPI protocal output doc,using Re-Doc to Show Everyone the API doc.
# 安装 tree-sitter cli
npm install -g tree-sitter-cli@0.24.7
# 编译 java grammar 生成 languages.so
tree-sitter build --output languages.so ./tree-sitter-java/src

from tree_sitter import Language, Parser

# 直接加载提前编译好的so，无编译逻辑
java_lang = Language("languages.so", "java")
parser = Parser(java_lang) # 新版不用 set_language，构造器传入