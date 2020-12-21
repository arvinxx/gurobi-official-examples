import os

path = '../documents'
output = '../dist'
for root, dirs, files in os.walk(path):
    for file in files:
        # print(os.path.join(root,file))
        if file.endswith(".ipynb"):
            # 过滤掉 check point 的 ipynb
            if file.find('-checkpoint') < 0:
                # print(file.find('-checkpoint'))
                print(root)
                print(file)
                os.system(
                    "jupyter nbconvert --to html " + os.path.join(root, file) + ' --output-dir ' + output)
