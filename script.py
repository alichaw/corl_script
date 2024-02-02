import configparser

# 初始化配置解析器
config = configparser.ConfigParser()

# 定义要执行的文件列表
files_to_run = ['cal_py.py', 'rebrac.py', 'spot.py', 'td3_bc.py']

envs = ['halfcheetah-medium-expert-v2', 'hopper-medium-expert-v2', 'walker2d-medium-expert-v2', 'pen-expert', 'hammer-expert', 'door-expert', 'relocate-expert']

# 对每个变量值进行循环
for env in envs:
    # 更新配置中的变量值
    config['DEFAULT'] = {'ENV': env}
    
    # 对每个文件进行循环
    for file in files_to_run:
        with open(file, 'r') as f:
            script_content = f.read()
            # 在当前的命名空间中执行脚本内容，使变量值生效
            exec(script_content, {'ENV': env})