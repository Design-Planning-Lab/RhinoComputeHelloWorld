import os
import compute_rhino3d.Util
from compute_rhino3d import Grasshopper as GH

import dotenv
dotenv.load_dotenv()
compute_rhino3d.Util.url = os.getenv('RHINO_URL')
compute_rhino3d.Util.apiKey = os.getenv('RHIO_API_KEY')
# compute_rhino3d.Util.url = "http://localhost:6500/"

x = GH.DataTree("RH_IN:x")
x.Append([0], [1])
y = GH.DataTree("RH_IN:y")
y.Append([0], [1])

tree = GH.DataTree("root")
tree.Append([0, 1], [x, y])
# resByURL = GH.EvaluateDefinition("https://github.com/cookiedan42/RhinoComputeHelloWorld/raw/main/Add/Add.gh", [x, y])
resByLocal = GH.EvaluateDefinition("./Add/Add.gh", [x, y])
print(resByLocal)
