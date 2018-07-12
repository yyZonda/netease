#!/bin/bash

project_dir=`pwd`
echo $project_dir

mvn spring-boot:run -Drun.jvmArguments="-Ddev.project.dir=$project_dir"

