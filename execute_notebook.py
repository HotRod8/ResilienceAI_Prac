"""Execute in a fresh Python process without requiring local kernel sockets."""
from pathlib import Path
import os
import nbformat
from IPython.core.interactiveshell import InteractiveShell
from IPython.utils.capture import capture_output
root=Path(__file__).resolve().parent
os.chdir(root)
nb=nbformat.read(root/'ResilienceAI.ipynb',as_version=4)
nbformat.validate(nb)
shell=InteractiveShell.instance()
shell.run_cell("import matplotlib; matplotlib.use('module://matplotlib_inline.backend_inline')")
n=0
for cell in nb.cells:
    if cell.cell_type!='code': continue
    n+=1
    with capture_output() as captured:
        result=shell.run_cell(cell.source,store_history=True)
    if result.error_in_exec or result.error_before_exec:
        raise RuntimeError(f'Cell {n} failed') from (result.error_in_exec or result.error_before_exec)
    outputs=[]
    if captured.stdout: outputs.append(nbformat.v4.new_output('stream',name='stdout',text=captured.stdout))
    if captured.stderr: outputs.append(nbformat.v4.new_output('stream',name='stderr',text=captured.stderr))
    for item in captured.outputs:
        outputs.append(nbformat.v4.new_output('display_data',data=item.data,metadata=item.metadata))
    cell.outputs=outputs; cell.execution_count=n
nbformat.validate(nb)
nbformat.write(nb,root/'ResilienceAI.ipynb')
print(f'Executed {n} code cells successfully')
