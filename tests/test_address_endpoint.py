import os
import requests

# configuration of api base url
ENDPOINT = "address"
API_VERSION = os.environ.get("API_VERSION")
BASE_URL = os.environ.get("BASE_URL")
API_URL = f"{BASE_URL}v{API_VERSION}/{ENDPOINT}/"

# http method should be GET, POST, DELETE, PUT
# 405 not implemented if any other http verb

# GET /address/
# 501 not implemented

# POST /address?={json}
# 200 if json ok and database ok

# POST /address?={json}
# 422 if json not ok

# POST /address?={json}
# 417 if json ok but database not ok

# PUT /address?={json}
# 200 if json ok and database ok

# PUT /address?={json}
# 422 if json not ok

# PUT /address?={json}
# 417 if json ok but database not ok
