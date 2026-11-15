# Chạy: python build.py  -> nhúng data.txt vào index.html (để mở offline vẫn có dữ liệu)
from pathlib import Path
t = Path("template.html").read_text(encoding="utf-8")
d = Path("data.txt").read_text(encoding="utf-8").replace("</script", "<\\/script")
Path("index.html").write_text(t.replace("__DATA__", d), encoding="utf-8")
print("OK -> index.html")
