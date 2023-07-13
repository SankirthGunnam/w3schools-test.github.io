import os
import pickle
import pprint

modules = {
    'prod': '',
    'calc': '',
    'gui': '',
    'main': ''
}

for plugin in modules:
    for root, dirs, files in os.walk('plugin1'):
        for file in files:
            if not file.endswith('.py'):
                continue

            with open(os.path.join(root, file), 'r') as fp:
                modules[file.replace('.py', '')] = fp.read()

print(f"Found and packed below modules to dll\n{'#' * 100}")
pprint.pprint(modules)
with open('plugin.dll', 'wb') as wp:
    pickle.dump(modules, wp, protocol=4)
