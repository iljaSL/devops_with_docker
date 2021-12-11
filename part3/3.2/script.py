import os

clone = "git clone https://github.com/iljaSL/devops_with_docker_ex_3.1.git app" 
build = "docker build ./app -t ex3.2"
tag = "docker tag ex3.2 plustig/ex3.2"
login = "docker login -u username -p password"
push = "docker push plustig/ex3.2"

os.system(clone)
os.system(build)
os.system(tag)
os.system(login)
os.system(push)
