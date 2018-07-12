这是一个简单的部署脚本，当然，你需要简单的配置一下系统环境
1. 你需要配置一下你本地的ssh登录配置文件
新增ssh登录配置项到~/.ssh/config
如：
Host db-19.space.163.org
    HostName db-19.space.163.org
    Port 1046
    User hzchenhongqin(需要更改为你自己的登录名)
    IdentityFile ~/.ssh/study_server(指向你的ssh登录私钥)

Host study11.server.163.org
    HostName study11.server.163.org
    Port 1046
    User hzchenhongqin(需要更改为你自己的登录名)
    IdentityFile ~/.ssh/study_server(指向你的ssh登录私钥)

2. 如果配置了deploy_script，那么配置deploy_path和deploy_exec_path将是失效的

