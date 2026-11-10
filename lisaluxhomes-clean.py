import os, re
P = 'pb_public/'
if not os.path.isfile(P + 'index.html'):
    raise SystemExit('Run this from your project folder (the one containing pb_public)')

# 1) hide the offers banner and the address/email/phone bar, and the extra headline text on the homepage
css_file = P + 'theme.css' if os.path.isfile(P + 'theme.css') else P + 'style.css'
css = open(css_file, encoding='utf-8').read()
MARK = '/* clean top + short footer */'
if MARK not in css:
    css += '\n' + MARK + '\n.ann,.bar{display:none!important}\n#home .intro{display:none}\n#ft{display:none}\n.about p{max-width:420px}\n'
    open(css_file, 'w', encoding='utf-8').write(css)
    print('ok   ' + css_file + ' | top banner, contact bar and homepage intro hidden')
else:
    print('ok   ' + css_file + ' | already cleaned')

# 2) shorten the footer company text
s = open(P + 'index.html', encoding='utf-8').read()
SHORT = ('<p>Nairobi real estate: homes for sale, rentals, land and Airbnb stays in Muthaiga, Kileleshwa, '
         'Kilimani, Runda, Lavington, Kitisuru, Karen and Westlands. Verified listings, prices in KSh.</p>')
new, n = re.subn(r'<p>Lisaluxhomes is a Nairobi real estate company.*?</p>', SHORT, s, count=1, flags=re.S)
if n:
    open(P + 'index.html', 'w', encoding='utf-8').write(new)
    print('ok   index.html | footer text summarised')
elif SHORT in s:
    print('ok   index.html | footer already short')
else:
    print('MISS index.html | footer paragraph not found (the footer may differ); tell me what the footer shows')
print('\nDone. Reload with Ctrl+Shift+R.')
