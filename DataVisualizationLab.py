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

print("\n3)")
# A Line plot
#  
# https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [n**3 for n in x]
print(y)
fix,ax = plt.subplots()
ax.plot(x,y)                        # create a plot of x and y axis values
ax.set_title('Powers of Three')     # set a title
ax.set_xlabel('Numbers')            # name the x-axis
ax.set_ylabel('Cubes')            # name the y-axis
plt.show()
