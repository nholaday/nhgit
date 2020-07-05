import os
import json

testenv = json.loads(os.environ.get("TESTENV", "TESTENV does not exist!"))
print("testenv: {}".format(testenv))

# import pdb; pdb.set_trace()
for key, val in testenv.items():
    os.environ[str(key)] = str(val)
    print("{}: {}".format(key,val))