import hazm
import re
import re

class Preprocess:


    def text_normalazation(self , raw_text):

        normalizer = hazm.Normalizer()
        clean_text = normalizer.normalize(raw_text)
        # clean_text = re.sub ( r'\n\s*\n', '\n' , clean_text )
        # clean_text = re.sub ( r'\r\s*\r', '\n', clean_text )
        clean_text = raw_text.replace ( '\n' , ' ' ).replace ( '\r' , '' )
        clean_text = re.sub ( ' +' , ' ' , clean_text )
        # clean_text = re.compile ( '<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});' )
        clean_text = clean_text.replace (u'\xa0', u' ')
        # clean_text = re.sub ( clean_text , ' ' , raw_text )
        # clean_text = ' '.join(clean_text.split())

        # clean_text = "\n".join(clean_text.split("\n"))

        return (clean_text)









# op = Preprocess()
# hh = op.text_normalazation("")
# print(hh)





