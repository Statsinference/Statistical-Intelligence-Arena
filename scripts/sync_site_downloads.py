"""Refresh portable site downloads from canonical sources; no training or PDF build."""
from pathlib import Path
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
DOWNLOADS = ROOT / 'site/downloads'
DOCUMENTS = {
    'contribution_en.md': 'CausalTaskBench_Contribution_Requirements_EN.md',
    'contribution_zh.md': 'CausalTaskBench_Contribution_Requirements_ZH.md',
    'contribution_en_zh.md': 'CausalTaskBench_Contribution_Requirements_EN_ZH.md',
    'student_guide_en.md': 'Student_Contribution_Walkthrough_EN.md',
    'student_guide_zh.md': 'Student_Contribution_Walkthrough_ZH.md',
}
PDFS = {
    'contribution_en.pdf': 'Statistical_Inference_Arena_Contribution_EN.pdf',
    'contribution_zh.pdf': 'Statistical_Inference_Arena_贡献规范_中文版.pdf',
    'contribution_en_zh.pdf': 'CausalTaskBench_Contribution_Guide_EN_ZH.pdf',
}

def download_document(source):
    text = (ROOT / 'docs' / source).read_text(encoding='utf-8')
    for canonical, legacy in DOCUMENTS.items():
        text = text.replace('](' + canonical + ')', '](' + legacy + ')')
    return text

def starter_files():
    return sorted(p for p in (ROOT/'starter').rglob('*')
                  if p.is_file() and '__pycache__' not in p.parts and p.suffix != '.pyc')

def main():
    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    for source, dest in DOCUMENTS.items():
        (DOWNLOADS / dest).write_bytes(download_document(source).encode('utf-8'))
    for source, dest in PDFS.items():
        shutil.copy2(ROOT/'docs/pdf'/source, DOWNLOADS/dest)
    shutil.copy2(ROOT/'starter/CONTRIBUTING.md', DOWNLOADS/'CONTRIBUTING.md')
    files = starter_files()
    with zipfile.ZipFile(DOWNLOADS/'causaltaskbench-starter.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for file in files:
            archive.write(file, 'causaltaskbench-starter/' + file.relative_to(ROOT/'starter').as_posix())
    print(f'Synchronized {len(DOCUMENTS)} documents, {len(PDFS)} PDFs and starter ({len(files)} files).')
    print('PDFs are reviewed exports; this command does not rebuild them.')

if __name__ == '__main__':
    main()
