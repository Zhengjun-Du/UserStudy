from genericpath import exists
import lxml.etree as et
from cairosvg import svg2png
from pathlib import Path
from sys import argv
import shutil

def clear_dirc(dirc:Path):
    if dirc.exists():
        shutil.rmtree(dirc)
    dirc.mkdir()

#files = ["29-shoe2","3-Cone","33-Syn0","34-syn1","35-syn2","36-syn3","37-syn4","38-syn5","39-syn6","40-syn7","41-syn8"]
files = ["3-Cone"]
#files = ["10-cow","11-Hammer","12-Truck","13-Tiger","16-House","17-Apple","18-Sound","20-Bear","25-Soda","26-Lamp","27-Teapot1","9-Phone"]

if __name__=='__main__':
    # src_path=Path(argv[1])
    for file in files:
        src_path=Path("./" + file)
        for im in src_path.iterdir():
            if im.suffix!=".svg":
                continue
            svg=et.parse(im)
            rt=svg.getroot()
            nsmap={'ns':rt.nsmap[None]}
            paths=list(rt.xpath("//ns:path",namespaces=nsmap))
            layers=[p.xpath("..")[0] for p in paths]
            dir_name = im.name.split('.')[0]
            #svg_path,png_path=src_path/f"{im.name}_svg",src_path/f"{im.name}_png"
            #clear_dirc(svg_path)
            png_path=Path("./" + file) /f"{dir_name}.png" #src_path
            clear_dirc(png_path)
            for p,l in zip(paths,layers):
                l.remove(p)
            for k,item in enumerate(zip(paths,layers)):
                p,l=item
                l.append(p)
                #svg.write(f"./{str(svg_path)}/{k}.svg",encoding='utf-8')
                text=et.tostring(svg)
                svg2png(bytestring=text,write_to=f"./{str(png_path)}/{k}.png")
                l.remove(p)
