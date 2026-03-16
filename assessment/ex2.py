import json
from urllib.request import urlopen

with urlopen("https://agents-for-data-prod-tmp.8e464e4039ccd5897a90175399bb04a7.r2.cloudflarestorage.com/2026-02-25/e90b6c84-8977-4a0e-ac72-d47230ef583e/mtcars.json?X-Amz-Expires=3600&X-Amz-Date=20260225T165014Z&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=7283c8cfa964ae1d21c994a61ac3c987%2F20260225%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=79ecd7b61e3a2d16cf8cf53151379d8c7b005bb5e77500cf12dbf593b22ed6d3") as file:
    source = file.read()
    # print(source)
    data = json.loads(source)
    print(json.dumps(data, indent=1))
    for item in data:
        print(item['model'],item['gear'])