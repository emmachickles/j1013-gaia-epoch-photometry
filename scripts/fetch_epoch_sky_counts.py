"""Refresh the aggregate sky counts from the Gaia ESA archive (network required)."""
from pathlib import Path
from urllib.request import urlopen
from urllib.parse import urlencode
import hashlib,json,datetime,io
import pandas as pd
root = Path(__file__).resolve().parents[1]
query = (root/'data/gaia_dr3_epoch_photometry_sky_query.adql').read_text()
endpoint = 'https://gea.esac.esa.int/tap-server/tap/sync'
params = urlencode(dict(REQUEST='doQuery',LANG='ADQL',FORMAT='csv',MAXREC=100000,QUERY=query))
with urlopen(endpoint+'?'+params,timeout=300) as response:
    content = response.read()
frame = pd.read_csv(io.BytesIO(content))
assert frame.n_sources.sum()==11754237
flag = frame.in_andromeda_survey.astype(str).str.lower().eq('true')
assert frame.loc[flag,'n_sources'].sum()==1257319
name = 'data/gaia_dr3_epoch_photometry_healpix6.csv'
(root/name).write_bytes(content)
manifest_path = root/'data/source_manifest.json'
manifest = json.loads(manifest_path.read_text())
for item in manifest:
    if item['file']==name:item['sha256']=hashlib.sha256(content).hexdigest()
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
meta_path = root/'data/gaia_dr3_epoch_photometry_sky_metadata.json'
meta = json.loads(meta_path.read_text())
meta['retrieved_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
meta_path.write_text(json.dumps(meta,indent=2)+'\n')
print(f'Refreshed counts of {frame.n_sources.sum():,} sources.')
