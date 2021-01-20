import sys
import AksharaJaana.main as ak
from AksharaJaana.utils import utils

_, input_file, output_file = sys.argv

print(f'Reading file {input_file}')
text = ak.ocr_engine(sys.argv[1])
u = utils()
print(f'Saving text to file {output_file}')
u.write_as_RTF(text, saving_path=output_file)