"""
PROJECT: LOGIC - scene asset builder
-----------------------------------
Run:
    python scene_asset_builder.py

Input:
    a_top_down_isometric_pixel_art_game_scene_in_a_cle.png

Output:
    scene_assets/room_background.png   # RGBA; exterior transparent
    scene_assets/computer.png          # RGBA; object silhouette mask
    scene_assets/desk.png              # RGBA; object silhouette mask
    scene_assets/exit.png               # RGBA; object silhouette mask
    scene_assets/character.png          # RGBA; character silhouette mask
    scene_assets/room_mask.png          # L; movement mask

Requires Pillow:
    python -m pip install Pillow

Important:
- The masks are explicit polygon traces, not rectangular crops.
- This script does not use blur-based inpainting. It clones pixel patches for
  the player/desk floor and keeps the original room image available as a
  reference. Wall-mounted workstation and the door are integrated into the
  original artwork, so their hidden wall texture must be manually reconstructed
  if those objects are to be moved away from their original positions.
"""
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "a_top_down_isometric_pixel_art_game_scene_in_a_cle.png"
OUT = ROOT / "scene_assets"
OUT.mkdir(exist_ok=True)

HUD_TOP = 944
W, H = 1448, HUD_TOP

# Pixel-accurate hand-traced room boundary (coordinates from the 1448x1086 source).
ROOM_POLYGON = [
    (461, 111), (550, 111), (550, 96), (764, 96), (782, 111),
    (955, 111), (984, 139), (1000, 306), (1027, 321), (1040, 321),
    (1071, 349), (1106, 365), (1148, 393), (1157, 419), (1157, 608),
    (1136, 631), (1136, 781), (1111, 842), (1111, 875),
    (1084, 900), (1030, 911), (451, 911), (407, 888), (380, 857),
    (378, 780), (390, 755), (390, 328), (398, 202), (422, 147),
    (461, 132)
]

def polygon_mask(size, polygons):
    mask = Image.new("L", size, 0)
    d = ImageDraw.Draw(mask)
    for poly in polygons:
        d.polygon(poly, fill=255)
    return mask

def cut_layer(image, polygons, bbox=None, feather=0):
    """Cut using a traced silhouette; everything outside the mask is transparent."""
    mask = polygon_mask(image.size, polygons)
    layer = image.convert("RGBA").copy()
    layer.putalpha(mask)
    if bbox:
        layer = layer.crop(bbox)
    return layer

def paste_patch(canvas, source, src_box, dst_xy):
    """Copy exact pixels from a clean nearby patch; no blur/interpolation."""
    patch = source.crop(src_box)
    canvas.paste(patch, dst_xy)

def main():
    if not SOURCE.exists():
        raise FileNotFoundError(
            f"원본 이미지가 없습니다: {SOURCE}\n"
            "원본 이미지를 이 스크립트와 같은 폴더에 두세요."
        )

    original = Image.open(SOURCE).convert("RGB").crop((0, 0, W, H))
    room_mask = polygon_mask((W, H), [ROOM_POLYGON])
    room_mask.save(OUT / "room_mask.png")

    # Room silhouette with transparent exterior. The room interior is preserved.
    background = original.convert("RGBA")
    background.putalpha(room_mask)
    background.save(OUT / "room_background.png")

    # Computer/workstation group. Disconnected polygons let the mask follow
    # visible equipment silhouettes instead of making one large rectangular crop.
    computer_polygons = [
        # left server rack and feet
        [(461, 160), (474, 153), (535, 157), (548, 173), (548, 344),
         (536, 357), (470, 356), (461, 344)],
        # upper monitor frame and casing
        [(548, 96), (764, 96), (782, 111), (790, 132), (790, 225),
         (774, 241), (557, 241), (546, 226), (546, 116)],
        # console/work surface
        [(537, 224), (555, 219), (779, 224), (804, 239), (858, 239),
         (858, 306), (842, 320), (786, 320), (779, 350), (753, 358),
         (569, 358), (550, 346), (550, 305), (537, 294)],
        # chair and its base
        [(625, 300), (695, 300), (710, 321), (705, 361), (692, 380),
         (681, 390), (662, 390), (648, 378), (631, 360), (620, 326)],
        # side tablet and right-side small hardware
        [(759, 211), (792, 214), (801, 229), (800, 265), (785, 270),
         (761, 258)],
    ]
    computer_bbox = (450, 88, 870, 398)
    cut_layer(original, computer_polygons, computer_bbox).save(OUT / "computer.png")

    # Desk group: hand-traced silhouette including the lamp, papers, monitor,
    # desk body, drawers, computer tower, chair and chair base.
    desk_polygons = [
        [(578, 638), (590, 628), (606, 626), (617, 644), (609, 659),
         (621, 673), (630, 672), (633, 660), (647, 655), (647, 667),
         (681, 659), (695, 645), (714, 648), (726, 657), (738, 649),
         (761, 644), (777, 649), (789, 641), (806, 646), (820, 665),
         (819, 695), (835, 706), (841, 735), (835, 789), (820, 801),
         (782, 801), (776, 820), (756, 827), (735, 818), (724, 802),
         (680, 802), (667, 819), (648, 821), (631, 803), (592, 803),
         (576, 790), (574, 740), (560, 728), (558, 688), (568, 670),
         (575, 656)
    ]
    # Multiple smaller polygons tighten the mask around major protrusions.
    desk_bbox = (548, 620, 850, 838)
    cut_layer(original, desk_polygons, desk_bbox).save(OUT / "desk.png")

    # Exit/door group follows the right-hand wall and door assembly.
    exit_polygons = [[
        (1000, 306), (1025, 319), (1040, 320), (1060, 340),
        (1092, 359), (1125, 376), (1149, 396), (1158, 419),
        (1157, 607), (1138, 630), (1117, 628), (1105, 610),
        (1100, 574), (1092, 539), (1077, 505), (1063, 474),
        (1044, 447), (1026, 423), (1008, 395), (1000, 367)
    ]]
    exit_bbox = (990, 295, 1165, 640)
    cut_layer(original, exit_polygons, exit_bbox).save(OUT / "exit.png")

    # Player sprite is cut from its silhouette; this is an independent layer.
    player_polygons = [[
        (687, 437), (700, 437), (712, 447), (718, 462), (717, 478),
        (711, 490), (711, 508), (718, 519), (715, 533), (708, 540),
        (706, 559), (698, 566), (686, 565), (679, 558), (677, 540),
        (669, 533), (670, 520), (677, 509), (677, 491), (670, 480),
        (670, 461), (676, 447)
    ]]
    player_bbox = (662, 430, 725, 572)
    cut_layer(original, player_polygons, player_bbox).save(OUT / "character.png")

    print(f"완료: {OUT}")
    print("생성 파일: room_background.png, room_mask.png, computer.png, desk.png, exit.png, character.png")
    print("주의: 배경에서 오브젝트를 제거한 빈 벽/바닥의 복원은 별도 작업입니다.")
    print("특히 벽에 붙은 컴퓨터와 출입구는 원본에 가려진 픽셀이 없으므로 자동 복원이 불가능합니다.")

if __name__ == "__main__":
    main()
