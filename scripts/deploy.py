import os

output = '../dist'
generate = 'generate_html.py'
os.system(f"rm -rf {output}")
os.system(f"python {generate}")
os.system(f"ghp-import -n -p -f {output}")
os.system(f"rm -rf {output}")
