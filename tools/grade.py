#!/usr/bin/env python3
"""Grade a run against its answer key with the rubric prompt (prompts/10_grader.md) and append to the scoreboard.

Usage: python tools/grade.py --run calibration/runs/<run>.json --key calibration/answer_keys/<id>.json --model llama3.1:70b
Recommended: grade with the strongest model you have (or a human); the grader does not need to be pre-dated because it sees the key.
"""
import argparse, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_agent import read, fill, chat, parse_json, PROMPTS, ROOT

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--run', required=True); ap.add_argument('--key', required=True); ap.add_argument('--model', default='llama3.1:8b')
    a = ap.parse_args()
    run = json.load(open(a.run)); key = json.load(open(a.key))
    prompt = fill(read(os.path.join(PROMPTS, '10_grader.md')), as_of_date=run['as_of_date'], answer_key=key, agent_output=run['final'])
    score = parse_json(chat(a.model, 'You are a strict, literal grader. Return JSON only.', prompt, True, 0.0, 16384))
    score['trade_id'] = key.get('id', run['pack']); score['run_file'] = os.path.basename(a.run); score['model_run'] = run['model']; score['grader_model'] = a.model; score['graded_at'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    os.makedirs(os.path.join(ROOT, 'calibration', 'scores'), exist_ok=True)
    fn = os.path.join(ROOT, 'calibration', 'scores', os.path.basename(a.run).replace('.json', '__score.json'))
    json.dump(score, open(fn, 'w'), indent=1, ensure_ascii=False)
    board = os.path.join(ROOT, 'calibration', 'scores', 'scoreboard.jsonl')
    with open(board, 'a') as f: f.write(json.dumps(score, ensure_ascii=False) + '\n')
    print(fn); print(json.dumps({k: score.get(k) for k in ['direction', 'state', 'discipline']}), score.get('reasoning_overlap', {}).get('k'), '/', score.get('reasoning_overlap', {}).get('n'), 'grounding', score.get('grounding', {}).get('share'))

if __name__ == '__main__': main()
