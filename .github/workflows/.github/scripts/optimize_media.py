import json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MEDIA = ROOT / "media"
DATA = ROOT / "data"
IMG_EXT = {".jpg", ".jpeg", ".png", ".webp", ".heic", ".heif"}
VID_EXT = {".mp4", ".mov", ".m4v", ".webm", ".3gp"}
MAX_PHOTO = 1600
MAX_SHORT_SIDE = 720
renames = {}


def probe(path):
    out = subprocess.run(
        ["ffprobe", "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=codec_name,width,height", "-of", "json", str(path)],
        capture_output=True, text=True)
    try:
        s = json.loads(out.stdout)["streams"][0]
        return s.get("codec_name"), int(s.get("width", 0)), int(s.get("height", 0))
    except Exception:
        return None, 0, 0


def do_video(p):
    codec, w, h = probe(p)
    if p.suffix.lower() == ".mp4" and codec == "h264" and 0 < min(w, h) <= MAX_SHORT_SIDE:
        return
    out = p.with_suffix(".mp4")
    tmp = p.with_name(p.stem + ".tmp.mp4")
    vf = ("scale='if(gt(iw,ih),-2,min(720,iw))':'if(gt(iw,ih),min(720,ih),-2)',"
          "fps=30,format=yuv420p")
    cmd = ["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", str(p),
           "-map", "0:v:0", "-map", "0:a:0?", "-vf", vf,
           "-c:v", "libx264", "-preset", "veryfast", "-crf", "28",
           "-c:a", "aac", "-b:a", "128k", "-ac", "2", "-movflags", "+faststart", str(tmp)]
    if subprocess.run(cmd).returncode != 0:
        print("Could not convert", p, file=sys.stderr)
        tmp.unlink(missing_ok=True)
        return
    if out != p:
        p.unlink()
        renames[p.name] = out.name
    tmp.replace(out)
    print("video:", p.name, "->", out.name)


def do_photo(p):
    from PIL import Image, ImageOps
    try:
        import pillow_heif
        pillow_heif.register_heif_opener()
    except ImportError:
        pass
    heic = p.suffix.lower() in {".heic", ".heif"}
    im = Image.open(p)
    if not heic and max(im.size) <= MAX_PHOTO:
        return
    im = ImageOps.exif_transpose(im)
    im.thumbnail((MAX_PHOTO, MAX_PHOTO))
    out = p.with_suffix(".jpg") if heic else p
    if out.suffix.lower() in {".jpg", ".jpeg"}:
        im.convert("RGB").save(out, quality=82, optimize=True, progressive=True)
    else:
        im.save(out, optimize=True)
    if out != p:
        p.unlink()
        renames[p.name] = out.name
    print("photo:", p.name, "->", out.name)


for f in sorted(MEDIA.rglob("*")):
    if not f.is_file():
        continue
    ext = f.suffix.lower()
    try:
        if ext in VID_EXT:
            do_video(f)
        elif ext in IMG_EXT:
            do_photo(f)
    except Exception as e:
        print("Skipped", f, e, file=sys.stderr)

if renames:
    for j in DATA.glob("*.json"):
        txt = j.read_text()
        new = txt
        for old, nw in renames.items():
            new = new.replace("/" + old + '"', "/" + nw + '"')
        if new != txt:
            j.write_text(new)
            print("updated", j.name)
