
def hexdump(b, step=16, decimal=False):
    for i in range(0, len(b), step):             # i =0,16,32,48,..,len(b)
        sub = b[i: i + step]                     # extract substring from b[i to i+16]
        output = '%08x ' % i                     # display i, index as a 8 digit hexadecimal
        output += '%08d ' % i if decimal else ''
        output += ' '.join(['%02x' % c for c in sub])  # display each char of substring as a 2 digit hexadecimal
        # fill empty spaces at the end
        output += '   ' * (step - len(sub))
        output += ' '
        # display substring in original form but not those not displayable
        output += ''.join([chr(c) if 0x20 <= c < 0x7F else '.' for c in sub])
        print(output)
    return output
