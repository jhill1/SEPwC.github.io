import re
import glob


ga_tag = """<head><!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-GPHGXML15W"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-GPHGXML15W');
</script>
"""


files = glob.glob('*.html')

for f in files:
    html_fh = open(f, 'r')
    content = html_fh.readlines()
    content = [re.sub('<head>', ga_tag, s) for s in content]
    html_fh.close()
    html_fh = open(f, 'w')
    html_fh.writelines(content)
    html_fh.close()


