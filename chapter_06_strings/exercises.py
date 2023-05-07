"""
Exercise 5: Take the following Python code that stores a string:
str = 'X-DSPAM-Confidence:0.8475'
Use find and string slicing to extract the portion of the string after the
colon character and then use the float function to convert the extracted
string into a floating point number.
"""


def extract(sentence):
    out = None
    colon_pos = sentence.find(':')
    if colon_pos != -1:
        host = sentence[colon_pos+1:]
        try:
            out = float(host)
        except ValueError:
            out = None
    return out


sentence = 'X-DSPAM-Confidence:0.8475'
extracted_portion = extract(sentence)
if extracted_portion is None:
    print('Something went wrong!')
else:
    print(extracted_portion)

