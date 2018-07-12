__author__ = 'chq'


import ConfigParser
import sys
import os
from subprocess import call

def main(args):
    cf = ConfigParser.SafeConfigParser()
    cf.read("deploy.config")

    if len(args) == 2:
        group = "default"
        branch=args[1]
    else:
        group=args[1]
        branch=args[2]


    build_path= cf.get(group, "build_path")
    build_host=cf.get(group, "build_host")
    deploy_path =  cf.get(group, "deploy_path")
    deploy_host= cf.get(group, "deploy_host")
    deploy_exec_path = cf.get(group, "deploy_exec_path")
    deploy_script= cf.get(group, "deploy_script")
    sudo= cf.get(group, "sudo")


    sudo_condition = 'sudo -iu study '


    print "deploy branch:" + branch + ", build in: " + build_path

    space = " ";
    #build
    exec_co = space.join(["ssh " + build_host, "'" + sudo_condition,"git --work-tree=" +build_path, "--git-dir=" + build_path + "/.git", "checkout " + branch, "'"])
    exec_ant_unlock = space.join(["ssh " + build_host, "'" + sudo_condition, "ant -buildfile " + build_path + "/build.xml unlock" + "'"])
    exec_ant = space.join(["ssh " + build_host, "'" + sudo_condition, "ant -buildfile " + build_path + "/build.xml" + "'"])

    os.system(exec_co)
    os.system(exec_ant_unlock)
    os.system(exec_ant)


    #reset sudo
    sudo_condition = '';
    if sudo == "yes":
        sudo_condition = 'sudo -iu study '


    #deploy
    if len(deploy_script) <= 0:
        exec_update = space.join(["ssh " + deploy_host, "'" + sudo_condition, "svn up " + deploy_path + "'"])
        exec_stop = space.join(["ssh " + deploy_host, "'" + sudo_condition, deploy_exec_path + "/tomcat6 stop'"])
        exec_start = space.join(["ssh " + deploy_host, "'" + sudo_condition, deploy_exec_path + "/tomcat6 start'"])
        os.system(exec_update)
        os.system(exec_stop)
        os.system(exec_start)
    else:
        exec_deploy_script = space.join(["ssh " + deploy_host, "'" + sudo_condition, "sh " + deploy_script + "'"])
        os.system(exec_deploy_script)

main(sys.argv)