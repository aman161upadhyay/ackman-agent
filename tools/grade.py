#!/usr/bin/env python3
"""Grade a run against its answer key with the rubric prompt (prompts/10_grader.md) and append to the scoreboard.

Usage: python tools/grade.py --run calibration/runs/<run>.json --key calibration/answer_keys/<id>.json --model <grader>
       add --decision model to grade the model's own call instead of the rule-enforced one (runs from runner 1.5.1+)
The grader must be a strong model (or a human), not the 8B model under test: it does not need to be pre-dated because it
sees the key, and an 8B grader is generous with paraphrase.
"""
import argparse, copy, json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from run_agent import read, fill, chat, parse_json, PROMPTS, ROOT

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--run', required=True); ap.add_argument('--key', required=True)
    ap.add_argument('--model', required=True, help='grader model, e.g. a 70B local model or an OpenAI-compatible frontier model')
    ap.add_argument('--decision', choices=['enforced', 'model'], default='enforced')
    a = ap.parse_args()
    with open(a.run, encoding='utf-8') as f: run = json.load(f)
    with open(a.key, encoding='utf-8') as f: key = json.load(f)
    final = copy.deepcopy(run['final'])
    if a.decision == 'model' and 'model_decision' in final: final['decision'] = final['model_decision']
    for k in ('model_decision', 'enforced_by_code'): final.pop(k, None)
    prompt = fill(read(os.path.join(PROMPTS, '10_grader.md')), as_of_date=run['as_of_date'], answer_key=key, agent_output=final)
    score = parse_json(chat(a.model, 'You are a strict, literal grader. Return JSON only.', prompt, True, 0.0, 16384))
    score['trade_id'] = key.get('id', run['pack']); score['run_file'] = os.path.basename(a.run); score['model_run'] = run['model']; score['grader_model'] = a.model; score['graded_at'] = time.strftime('%Y-%m-%dT%H:%M:%S')
    score['graded_decision'] = a.decision if 'model_decision' in run['final'] else 'model'
    os.makedirs(os.path.join(ROOT, 'calibration', 'scores'), exist_ok=True)
    fn = os.path.join(ROOT, 'calibration', 'scores', os.path.basename(a.run).replace('.json', f'__{a.decision}__score.json'))
    with open(fn, 'w', encoding='utf-8') as f: json.dump(score, f, indent=1, ensure_ascii=False)
    board = os.path.join(ROOT, 'calibration', 'scores', 'scoreboard.jsonl')
    with open(board, 'a', encoding='utf-8') as f: f.write(json.dumps(score, ensure_ascii=False) + '\n')
    sys.stdout.reconfigure(encoding='utf-8')
    print(fn); print(json.dumps({k: score.get(k) for k in ['direction', 'state', 'discipline']}), score.get('reasoning_overlap', {}).get('k'), '/', score.get('reasoning_overlap', {}).get('n'), 'grounding', score.get('grounding', {}).get('share'))

if __name__ == '__main__': main()
