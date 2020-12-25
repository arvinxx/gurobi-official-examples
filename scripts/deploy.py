import os

output = '../dist'
generate = 'generate_html.py'
# 清理前产物
os.system(f"rm -rf {output}")
# 生成 html
os.system(f"python {generate}")
# 部署
os.system(f"ghp-import -n -p -f {output}")
# 清理生成产物
os.system(f"rm -rf {output}")
