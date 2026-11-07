#!/usr/bin/env python3
"""Genera recetas, modelos, traducciones, tags y texturas de Netherite Resonante.

Uso:  python3 tools/generate_assets.py [raiz_del_proyecto]
Requiere Pillow (pip install pillow).
"""
import json
import sys
from pathlib import Path

from PIL import Image

MOD = "netherite_resonante"
ROOT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
RES = ROOT / "src" / "main" / "resources"
ASSETS = RES / "assets" / MOD
DATA = RES / "data" / MOD

SHARD = "resonant_amethyst_shard"
OVERCHARGED = "overcharged_resonant_amethyst_shard"
TEMPLATE = "crystallized_upgrade_template"

TOOLS = ["sword", "pickaxe", "axe", "shovel", "hoe"]
ARMOR = ["helmet", "chestplate", "leggings", "boots"]
GEAR = TOOLS + ARMOR


def rid(kind):
    return f"resonant_netherite_{kind}"


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# ----------------------------------------------------------------------------- recetas
def recipes():
    write_json(DATA / "recipe" / f"{SHARD}.json", {
        "type": "minecraft:crafting_shaped",
        "category": "misc",
        "pattern": ["AAA", "AEA", "AAA"],
        "key": {"A": "minecraft:amethyst_shard", "E": "minecraft:echo_shard"},
        "result": {"id": f"{MOD}:{SHARD}", "count": 1},
    })
    write_json(DATA / "recipe" / f"{TEMPLATE}.json", {
        "type": "minecraft:crafting_shapeless",
        "category": "misc",
        "ingredients": [
            "minecraft:netherite_upgrade_smithing_template",
            f"{MOD}:{OVERCHARGED}",
        ],
        "result": {"id": f"{MOD}:{TEMPLATE}", "count": 1},
    })
    for kind in GEAR:
        write_json(DATA / "recipe" / f"{rid(kind)}_smithing.json", {
            "type": "minecraft:smithing_transform",
            "template": f"{MOD}:{TEMPLATE}",
            "base": f"minecraft:netherite_{kind}",
            "addition": f"{MOD}:{OVERCHARGED}",
            "result": {"id": f"{MOD}:{rid(kind)}", "count": 1},
        })


# ----------------------------------------------------------------------------- modelos
def models():
    simple = [SHARD, OVERCHARGED, TEMPLATE] + [rid(k) for k in ARMOR]
    handheld = [rid(k) for k in TOOLS]
    for name, parent in [(n, "minecraft:item/generated") for n in simple] + \
                        [(n, "minecraft:item/handheld") for n in handheld]:
        write_json(ASSETS / "models" / "item" / f"{name}.json", {
            "parent": parent,
            "textures": {"layer0": f"{MOD}:item/{name}"},
        })
        write_json(ASSETS / "items" / f"{name}.json", {
            "model": {"type": "minecraft:model", "model": f"{MOD}:item/{name}"},
        })
    layer = [{"texture": f"{MOD}:{MOD}"}]
    write_json(ASSETS / "equipment" / f"{MOD}.json", {
        "layers": {"humanoid": layer, "humanoid_baby": layer, "humanoid_leggings": layer},
    })


# ----------------------------------------------------------------------------- tags
def tags():
    groups = {
        "swords": ["sword"], "pickaxes": ["pickaxe"], "axes": ["axe"], "shovels": ["shovel"],
        "hoes": ["hoe"], "head_armor": ["helmet"], "chest_armor": ["chestplate"],
        "leg_armor": ["leggings"], "foot_armor": ["boots"],
    }
    for tag, kinds in groups.items():
        write_json(RES / "data" / "minecraft" / "tags" / "item" / f"{tag}.json", {
            "replace": False,
            "values": [f"{MOD}:{rid(k)}" for k in kinds],
        })


# ----------------------------------------------------------------------------- traducciones
ES = {
    SHARD: ("Fragmento de Amatista Resonante",
            "Cristal de amatista cargado con el eco de las Ciudades Antiguas."),
    OVERCHARGED: ("Fragmento de Amatista Resonante Sobrecargada",
                  "Resonancia concentrada al límite. Necesaria para forjar Netherite Resonante."),
    TEMPLATE: ("Plantilla de Mejora Cristalizada",
               "Mejora Netherite a Netherite Resonante. Úsala en la mesa de herrería junto a un fragmento sobrecargado."),
    "sword": ("Espada de Netherite Resonante", "Estadísticas x1,9 respecto a la Netherite."),
    "pickaxe": ("Pico de Netherite Resonante", "Estadísticas x1,9 respecto a la Netherite."),
    "axe": ("Hacha de Netherite Resonante", "Estadísticas x1,9 respecto a la Netherite."),
    "shovel": ("Pala de Netherite Resonante", "Estadísticas x1,9 respecto a la Netherite."),
    "hoe": ("Azada de Netherite Resonante", "Estadísticas x1,9 respecto a la Netherite."),
    "helmet": ("Casco de Netherite Resonante", "Estadísticas x1,9 respecto a la Netherite."),
    "chestplate": ("Pechera de Netherite Resonante", "Estadísticas x1,9 respecto a la Netherite."),
    "leggings": ("Pantalones de Netherite Resonante", "Estadísticas x1,9 respecto a la Netherite."),
    "boots": ("Botas de Netherite Resonante", "Estadísticas x1,9 respecto a la Netherite."),
}
EN = {
    SHARD: ("Resonant Amethyst Shard",
            "An amethyst crystal charged with the echo of the Ancient Cities."),
    OVERCHARGED: ("Overcharged Resonant Amethyst Shard",
                  "Resonance concentrated to its limit. Required to forge Resonant Netherite."),
    TEMPLATE: ("Crystallized Upgrade Template",
               "Upgrades Netherite to Resonant Netherite. Use it at a smithing table with an overcharged shard."),
    "sword": ("Resonant Netherite Sword", "Stats x1.9 compared to Netherite."),
    "pickaxe": ("Resonant Netherite Pickaxe", "Stats x1.9 compared to Netherite."),
    "axe": ("Resonant Netherite Axe", "Stats x1.9 compared to Netherite."),
    "shovel": ("Resonant Netherite Shovel", "Stats x1.9 compared to Netherite."),
    "hoe": ("Resonant Netherite Hoe", "Stats x1.9 compared to Netherite."),
    "helmet": ("Resonant Netherite Helmet", "Stats x1.9 compared to Netherite."),
    "chestplate": ("Resonant Netherite Chestplate", "Stats x1.9 compared to Netherite."),
    "leggings": ("Resonant Netherite Leggings", "Stats x1.9 compared to Netherite."),
    "boots": ("Resonant Netherite Boots", "Stats x1.9 compared to Netherite."),
}


def lang_dict(table):
    out = {}
    for key, (name, desc) in table.items():
        item_id = key if key in (SHARD, OVERCHARGED, TEMPLATE) else rid(key)
        out[f"item.{MOD}.{item_id}"] = name
        out[f"tooltip.{MOD}.{item_id}"] = desc
    return out


def lang():
    es = lang_dict(ES)
    for code in ["es_es", "es_mx", "es_ar", "es_cl", "es_uy", "es_ve", "es_co", "es_pe"]:
        write_json(ASSETS / "lang" / f"{code}.json", es)
    write_json(ASSETS / "lang" / "en_us.json", lang_dict(EN))


# ----------------------------------------------------------------------------- texturas
PAL = {
    "K": (10, 5, 18, 255),      # negro
    "M": (28, 12, 46, 255),     # negro violáceo
    "D": (62, 24, 108, 255),    # morado oscuro
    "P": (124, 54, 198, 255),   # morado
    "L": (182, 112, 238, 255),  # morado claro
    "W": (248, 242, 255, 255),  # blanco
    "H": (40, 22, 62, 255),     # mango
}


def blank():
    return [[None] * 16 for _ in range(16)]


def put(g, x, y, c):
    if 0 <= x < 16 and 0 <= y < 16:
        g[y][x] = c


def outline(g):
    """Contorno negro alrededor de las formas, como en las texturas vanilla."""
    marks = []
    for y in range(16):
        for x in range(16):
            if g[y][x] is None:
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < 16 and 0 <= ny < 16 and g[ny][nx] is not None:
                        marks.append((x, y))
                        break
    for x, y in marks:
        g[y][x] = "K"


def to_image(g, scale=1):
    img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
    for y in range(16):
        for x in range(16):
            if g[y][x] is not None:
                img.putpixel((x, y), PAL[g[y][x]])
    if scale != 1:
        img = img.resize((16 * scale, 16 * scale), Image.NEAREST)
    return img


def from_art(rows):
    assert len(rows) == 16, len(rows)
    g = blank()
    for y, row in enumerate(rows):
        assert len(row) == 16, (y, row, len(row))
        for x, ch in enumerate(row):
            if ch != ".":
                g[y][x] = ch
    return g


def handle(g, x0, x1):
    for x in range(x0, x1 + 1):
        put(g, x, 15 - x, "H")
    put(g, x0 - 1, 15 - x0 + 1, "P")


def art_sword():
    g = blank()
    for i in range(8):
        x, y = 6 + i, 9 - i
        put(g, x, y, "P")
        put(g, x - 1, y, "W" if i % 3 == 1 else "L")
    put(g, 14, 1, "W")
    for p in [(3, 8), (4, 9), (5, 10), (6, 11), (7, 12)]:
        put(g, *p, "D")
    put(g, 5, 10, "W")
    for p in [(4, 11), (3, 12), (2, 13), (1, 14)]:
        put(g, *p, "H")
    put(g, 0, 15, "P")
    outline(g)
    return g


def art_pickaxe():
    g = blank()
    inner = [(4, 6), (5, 5), (6, 4), (7, 4), (8, 3), (9, 3), (10, 3), (11, 4), (11, 5), (12, 6)]
    outer = [(3, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 3), (8, 2), (9, 2), (10, 2), (11, 3),
             (12, 4), (12, 5), (13, 6), (13, 7)]
    for p in inner:
        put(g, *p, "P")
    for p in outer:
        put(g, *p, "L")
    put(g, 8, 2, "W")
    put(g, 4, 5, "W")
    handle(g, 1, 10)
    outline(g)
    return g


def art_axe():
    g = blank()
    rows = {2: (8, 11), 3: (6, 12), 4: (5, 10), 5: (5, 9), 6: (5, 7)}
    for y, (a, b) in rows.items():
        for x in range(a, b + 1):
            put(g, x, y, "L" if x == a else ("D" if x == b else "P"))
    put(g, 9, 3, "W")
    handle(g, 1, 11)
    outline(g)
    return g


def art_shovel():
    g = blank()
    rows = {1: (12, 13), 2: (11, 14), 3: (11, 14), 4: (12, 13)}
    for y, (a, b) in rows.items():
        for x in range(a, b + 1):
            put(g, x, y, "L" if x == a else ("D" if x == b else "P"))
    put(g, 12, 2, "W")
    handle(g, 1, 11)
    outline(g)
    return g


def art_hoe():
    g = blank()
    for x in range(7, 13):
        put(g, x, 2, "L" if x == 7 else ("D" if x == 12 else "P"))
    put(g, 6, 3, "L")
    put(g, 7, 3, "P")
    put(g, 11, 3, "P")
    put(g, 6, 4, "P")
    put(g, 9, 2, "W")
    handle(g, 1, 11)
    outline(g)
    return g


ART_HELMET = [
    "................",
    "................",
    "....LLLLLLLL....",
    "...LPPPPPPPPD...",
    "..LPPPWPPWPPPD..",
    "..LPPPPPPPPPPD..",
    "..LPPPPPPPPPPD..",
    "..LPPPPPPPPPPD..",
    "..LPPPPPPPPPPD..",
    "..LPPD....LPPD..",
    "..LPPD....LPPD..",
    "..DDDD....DDDD..",
    "................",
    "................",
    "................",
    "................",
]
ART_CHEST = [
    "................",
    "..PPP......PPP..",
    ".LPPPL....LPPPD.",
    ".LPPPPPPPPPPPPD.",
    ".LPPPPPPPPPPPPD.",
    "..LPPPPPPPPPPD..",
    "..LPPPPWWPPPPD..",
    "..LPPPWKKWPPPD..",
    "..LPPPPWWPPPPD..",
    "..LPPPPPPPPPPD..",
    "..LPPPPPPPPPPD..",
    "..LPPPPPPPPPPD..",
    "..DDDDDDDDDDDD..",
    "................",
    "................",
    "................",
]
ART_LEGS = [
    "................",
    "................",
    "..LPPPPPPPPPPD..",
    "..LPPPPPPPPPPD..",
    "..LPWPPPPPPWPD..",
    "..LPPPPPPPPPPD..",
    "..LPPPDDDDPPPD..",
    "..LPPPD..DPPPD..",
    "..LPPPD..DPPPD..",
    "..LPPD....LPDD..",
    "..LPPD....LPDD..",
    "..LPPD....LPDD..",
    "..DDDD....DDDD..",
    "................",
    "................",
    "................",
]
ART_BOOTS = [
    "................",
    "................",
    "................",
    "................",
    "................",
    "................",
    "...LPPD..LPPD...",
    "...LPPD..LPPD...",
    "...LPPD..LPPD...",
    "...LPPD..LPPD...",
    "..LPPPD..LPPPD..",
    "..LWPPD..LWPPD..",
    "..LPPPD..LPPPD..",
    "..DDDDD..DDDDD..",
    "................",
    "................",
]
ART_SHARD = [
    "................",
    ".......PP.......",
    "......LLPP......",
    ".....LWLLPD.....",
    "....LWLLPPPD....",
    "....LWLPPPPD....",
    "....LLPPPPDD....",
    ".....LPPPPDD....",
    ".....LPPPDD.....",
    "......LPDD......",
    ".......DD.......",
    "................",
    "................",
    "................",
    "................",
    "................",
]
ART_OVERCHARGED = [
    "..W.........W...",
    "........W.......",
    ".......LP.......",
    "......LWPP......",
    ".....LWLPPD.....",
    "....LWLPKKPD....",
    "...LWLPKKKKPD...",
    "...LLPKWKKKPD...",
    "...LPPKKKKPDD...",
    "....LPPKKPDD....",
    ".....LPPPDD.....",
    "......LPDD......",
    ".......DD.......",
    ".W.........W..W.",
    "................",
    "..........W.....",
]


def art_template():
    g = blank()
    for y in range(1, 15):
        for x in range(2, 14):
            if (x in (2, 13)) and (y in (1, 14)):
                continue
            edge = x in (2, 13) or y in (1, 14)
            put(g, x, y, "P" if edge else "M")
    # esquinas luminosas y marco interior
    for x in range(4, 12):
        put(g, x, 3, "D")
        put(g, x, 12, "D")
    for y in range(3, 13):
        put(g, 4, y, "D")
        put(g, 11, y, "D")
    # cristal central
    crystal = {5: [7, 8], 6: [6, 7, 8, 9], 7: [6, 7, 8, 9], 8: [6, 7, 8, 9], 9: [6, 7, 8, 9], 10: [7, 8]}
    for y, xs in crystal.items():
        for x in xs:
            put(g, x, y, "L" if x in (6, 7) else "P")
    put(g, 7, 6, "W")
    put(g, 7, 7, "W")
    put(g, 5, 2, "W")
    put(g, 10, 13, "W")
    put(g, 2, 7, "L")
    put(g, 13, 8, "L")
    return g


def textures():
    items = ASSETS / "textures" / "item"
    items.mkdir(parents=True, exist_ok=True)
    arts = {
        SHARD: from_art(ART_SHARD),
        OVERCHARGED: from_art(ART_OVERCHARGED),
        TEMPLATE: art_template(),
        rid("sword"): art_sword(),
        rid("pickaxe"): art_pickaxe(),
        rid("axe"): art_axe(),
        rid("shovel"): art_shovel(),
        rid("hoe"): art_hoe(),
        rid("helmet"): from_art(ART_HELMET),
        rid("chestplate"): from_art(ART_CHEST),
        rid("leggings"): from_art(ART_LEGS),
        rid("boots"): from_art(ART_BOOTS),
    }
    for name, g in arts.items():
        if name in (SHARD, OVERCHARGED) or name.endswith(("helmet", "chestplate", "leggings", "boots")):
            outline(g)
        to_image(g).save(items / f"{name}.png")

    # icono del mod
    to_image(arts[OVERCHARGED], scale=8).save(ASSETS / "icon.png")

    # texturas de armadura al vestir (formato 64x32)
    eq = ASSETS / "textures" / "entity" / "equipment"
    regions = [(0, 0, 32, 16), (16, 16, 24, 16), (40, 16, 16, 16), (0, 16, 16, 16)]

    def inside(x, y):
        return any(rx <= x < rx + rw and ry <= y < ry + rh for rx, ry, rw, rh in regions)

    def layer(leggings):
        img = Image.new("RGBA", (64, 32), (0, 0, 0, 0))
        base = PAL["D"] if leggings else PAL["P"]
        facet = PAL["P"] if leggings else (140, 66, 214, 255)
        for y in range(32):
            for x in range(64):
                if not inside(x, y):
                    continue
                c = base if ((x // 2) + (y // 2)) % 2 == 0 else facet
                if (x + y) % 9 == 0:
                    c = PAL["L"]
                if x % 8 == 0 or y % 8 == 0:
                    c = PAL["M"]
                if ((x * 73856093) ^ (y * 19349663)) % 31 == 0:
                    c = PAL["W"]
                img.putpixel((x, y), c)
        return img

    for sub, leg in (("humanoid", False), ("humanoid_baby", False), ("humanoid_leggings", True)):
        d = eq / sub
        d.mkdir(parents=True, exist_ok=True)
        layer(leg).save(d / f"{MOD}.png")


if __name__ == "__main__":
    recipes()
    models()
    tags()
    lang()
    textures()
    print("Recursos generados en", RES)
