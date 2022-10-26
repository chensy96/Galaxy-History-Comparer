import subprocess
import os.path

subprocess.check_call(
    ['python', 'ghevaluator/ghevaluator_main.py',
     'https://usegalaxy.eu/u/siyu_chen/h/assemblyhands-onsiyu-chen',
     'https://usegalaxy.eu/training-material/topics/assembly/tutorials/general-introduction/workflows/assembly-general-introduction.ga',
     'D4XEpojvk877VKOAtCpu8H2Irdr3kol'])
assert os.path.exists('./report.json')