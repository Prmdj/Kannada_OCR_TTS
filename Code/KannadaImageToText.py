import AksharaJaana.main as ak

text = ak.ocr_engine('../data/test.pdf')

from AksharaJaana.utils import utils

u = utils()
u.write_as_RTF(text, saving_path='../output/test.rtl')