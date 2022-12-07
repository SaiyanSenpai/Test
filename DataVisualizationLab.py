'''
    Use matploitlib.
'''


print("1)")
import subprocess
import sys

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

all_packages_installed = True
for n in ["matplotlib","pandas","plotly",'requests']:
    if n in installed_packages:
        print(n+" is installed.")
        continue
    else:
        all_packages_installed = False
if all_packages_installed:
    print("The packages are installed.")
else:
    print("All packages are not installed.")


print("\n2)")
import matplotlib.pyplot as plt

# a Figure is the space upon which a graph can be placed
fig = plt.figure()                  # create an empty figure
fig = plt.figure(figsize=(9,6))    # create an empty figure which is 9 by by 6 inches
plt.show()       