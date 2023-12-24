from setuptools import find_packages,setup
from typing import List


def get_requirements(obj_path)-> List[str]:
    hed = '-e .'
    requirements = []
    with open(obj_path) as obj:
        requirements = obj.readlines()
        print("Line wise ",requirements)

        re = []
        for req in requirements:
            req= req.replace("\n","")
            re.append(req)
            print("Individual ",re)
        
        # for req in requirements:
        #     req = req.replace(hed,"")
        #     requirements.append(req)
        #     print("hed delete ",requirements)
        if hed in re:
            re.remove(hed) 
            print("Final ",re)


    return(re)


setup(
name = 'mlproject_02',
version = '0.0.1',
author_email = 'poojarypsl@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)

# get_requirements('requirements.txt')