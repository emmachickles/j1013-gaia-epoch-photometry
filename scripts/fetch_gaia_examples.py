"""Refresh the six public DR3 light curves used in the gallery (network required)."""
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen
import datetime
import hashlib
import io
import json
import pandas as pd

root = Path(__file__).resolve().parents[1]
path = root/'data/examples/manifest.json'
metadata = json.loads(path.read_text())
checksums_path = root/'data/source_manifest.json'
checksums = json.loads(checksums_path.read_text())
for item in metadata['examples']:
    params = dict(metadata['request'], ID=item['source_id'])
    with urlopen(metadata['endpoint']+'?'+urlencode(params),timeout=120) as response:
        content = response.read()
    frame = pd.read_csv(io.BytesIO(content),dtype={'source_id':str,'transit_id':str})
    assert len(frame)>0 and frame.source_id.eq(item['source_id']).all()
    assert {'g_transit_time','g_transit_flux','variability_flag_g_reject'} <= set(frame.columns)
    (root/item['file']).write_bytes(content)
    for source in checksums:
        if source['file']==item['file']:
            source['sha256']=hashlib.sha256(content).hexdigest()
    print(item['key'],item['source_id'],len(frame),'downloaded rows')
checksums_path.write_text(json.dumps(checksums,indent=2)+'\n')
metadata['retrieved_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
path.write_text(json.dumps(metadata,indent=2)+'\n')
