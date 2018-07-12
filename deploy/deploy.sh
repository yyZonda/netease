cd ../
branch=`git branch | awk -F " " '{print $2}'`
cd -

if [ $# == 0 ]; then
	python EduDeploy.py "default" $branch
elif [ $# == 1 ]; then
	python EduDeploy.py $1 $branch
else
	echo "#usage: deploy [config]"
fi
