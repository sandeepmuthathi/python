scanned_lines=set(open('/home/sandeep.m/testing/test').readlines)
print(scanned_lines)
bar = open('/home/sandeep.m/bar', 'w').writelines(set(scanned_lines))

bar.close()