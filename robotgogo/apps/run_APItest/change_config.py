rf_DIR="/root/mygithub/quality/automation/rf/compass/devops/"




def change_config_IP(IP):
    data = ''
    envFile=rf_DIR + "环境信息/globalEnv.txt"
    with open(envFile,"r", encoding="utf-8") as f:
        for line in f.readlines():
            if line.find('${compass_ip}') == 0:
                line = "${compass_ip}" + "      " + IP + '\n'
            data += line

    with open(envFile, "w", encoding="utf-8") as f:
        f.writelines(data)


def change_config_registry(registry):
    data = ''
    envFile = rf_DIR + "环境信息/globalEnv.txt"
    with open(envFile, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if line.find('${registry_url}') == 0:
                line = "${registry_url}" + "      " + registry + '\n'
            data += line

    with open(envFile, "w", encoding="utf-8") as f:
        f.writelines(data)
