"""Generate CSES revision schedules and list due reviews. Python 3.8+, no dependencies."""
import argparse
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STEPS = [(0, 'Understand, dry-run and review mistakes'), (1, 'Recall and explain without notes'), (3, 'Write pseudocode and identify edge cases'), (7, 'Implement independently and submit'), (14, 'Timed interview simulation'), (30, 'Compare approaches and optimize'), (60, 'Solve an unfamiliar problem using the same pattern')]


def due(today):
    rows = []
    for path in ROOT.rglob('revision.md'):
        for line in path.read_text(encoding='utf-8').splitlines():
            cells = [s.strip() for s in line.strip().strip('|').split('|')]
            if len(cells) != 4 or not cells[0].startswith('R') or cells[3].lower() == 'completed':
                continue
            try:
                scheduled = date.fromisoformat(cells[1])
            except ValueError:
                continue
            if scheduled <= today:
                rows.append((scheduled, str(path.parent.relative_to(ROOT)), cells[0], cells[2]))
    for scheduled, folder, revision, task in sorted(rows):
        print(f'{scheduled} | {folder} | {revision} | {task}')
    if not rows:
        print('No pending reviews due.')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--problem')
    p.add_argument('--folder', help='Problem directory relative to repository root')
    p.add_argument('--start', type=date.fromisoformat, default=date.today())
    p.add_argument('--accepted', type=date.fromisoformat)
    p.add_argument('--link', default='')
    p.add_argument('--pattern', default='')
    p.add_argument('--due', action='store_true')
    p.add_argument('--today', type=date.fromisoformat, default=date.today())
    a = p.parse_args()
    if a.due:
        due(a.today)
        return
    if not a.problem or not a.folder:
        p.error('--problem and --folder are required unless using --due')
    folder = (ROOT / a.folder).resolve()
    if ROOT not in folder.parents:
        p.error('Choose a problem folder inside the repository.')
    target = folder / 'revision.md'
    if target.exists():
        p.error(f'{target} already exists; revision history will not be overwritten.')
    lines = ['| Revision | Scheduled date | Task | Status |', '|---|---|---|---|']
    for i, (offset, task) in enumerate(STEPS):
        lines.append(f'| R{i} — Day {offset} | {a.start + timedelta(days=offset)} | {task} | Pending |')
    template = (ROOT / 'templates/revision-template.md').read_text(encoding='utf-8')
    for key, value in {'PROBLEM': a.problem, 'LINK': a.link, 'PATTERN': a.pattern, 'ACCEPTED': str(a.accepted or ''), 'START': str(a.start), 'SCHEDULE': '\n'.join(lines)}.items():
        template = template.replace('{{' + key + '}}', value)
    folder.mkdir(parents=True, exist_ok=True)
    with target.open('x', encoding='utf-8') as f:
        f.write(template)
    print(f'Created {target.relative_to(ROOT)}')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
