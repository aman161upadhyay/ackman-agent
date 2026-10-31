#!/usr/bin/env python3
"""Plant a canary fact in a pack (a harmless, invented but plausible detail) and later verify the agent cited it.
This is a grounding check (did the agent read the pack?), not a cutoff check: use tools/cutoff_probe.py for that.
Usage: python tools/canary.py plant calibration/data_packs/<id>   -> writes docs/D99_canary.md and records the canary in meta.json
       python tools/canary.py check calibration/runs/<run>.json   -> reports whether the canary text appears in the agent output
"""
import json, os, sys, random
if __name__ == '__main__':
    if len(sys.argv) != 3 or sys.argv[1] not in ('plant', 'check'): sys.exit(__doc__)
    cmd, path = sys.argv[1], sys.argv[2]
    if cmd == 'plant':
        with open(os.path.join(path, 'meta.json'), encoding='utf-8') as f: meta = json.load(f)
        canary = f"The company disclosed that its {random.choice(['Omaha','Tulsa','Reno','Albany'])} regional office lease runs through {random.randint(2027, 2034)}."
        meta['canary'] = canary
        with open(os.path.join(path, 'meta.json'), 'w', encoding='utf-8') as f: json.dump(meta, f, indent=1, ensure_ascii=False)
        open(os.path.join(path, 'docs', 'D99_canary.md'), 'w', encoding='utf-8').write(f"Title: Lease footnote\nSource: company filing (footnote)\nDate: {meta['as_of_date']}\n\n{canary}\n")
        print('planted:', canary)
    else:
        with open(path, encoding='utf-8') as f: run = json.load(f)
        txt = json.dumps(run)
        with open(os.path.join(os.path.dirname(os.path.dirname(path)), 'data_packs', run['pack'], 'meta.json'), encoding='utf-8') as f: meta = json.load(f)
        print('canary cited:', meta.get('canary', '')[:40] in txt or 'D99' in txt)
