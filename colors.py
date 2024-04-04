from sort_draw import draw_sorting
import random

def list_rgb(NUM_SECTIONS):
    liste_rgb = []
    for _ in range(NUM_SECTIONS):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        liste_rgb.append((r, g, b))
    return liste_rgb

def RGB_to_HSV(list_rgb):
    list_hsv = []
    for r, g, b in list_rgb:
        r, g, b = r / 255, g / 255, b / 255
        cmax = max(r, g, b)
        cmin = min(r, g, b)
        delta = cmax - cmin
        if delta == 0:
            h = 0
        elif cmax == r:
            h = 60 * (((g - b) / delta) % 6)
        elif cmax == g:
            h = 60 * ((b - r) / delta + 2)
        elif cmax == b:
            h = 60 * ((r - g) / delta + 4)
        if cmax == 0:
            s = 0
            v = 0
        else:
            s = 1
            v = 1
        list_hsv.append((h, s, v))
        liste_hsv_selection = list_hsv.copy()
        liste_hsv_bubble = list_hsv.copy()
        liste_hsv_insertion = list_hsv.copy()
        liste_hsv_merge = list_hsv.copy()
        liste_hsv_quick = list_hsv.copy()
        liste_hsv_heap = list_hsv.copy()
        liste_hsv_combes = list_hsv.copy()
        
    return liste_hsv_selection, liste_hsv_bubble, liste_hsv_insertion, liste_hsv_merge, liste_hsv_quick, liste_hsv_heap, liste_hsv_combes

def HSV_to_RGB(liste_hsv, font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS):
    liste_rgb.clear()
    for h, s, v in liste_hsv:
        c = v * s
        x = c * (1 - abs((h / 60) % 2 - 1))
        m = v - c
        if 0 <= h < 60:
            r, g, b = c, x, 0
        elif 60 <= h < 120:
            r, g, b = x, c, 0
        elif 120 <= h < 180:
            r, g, b = 0, c, x
        elif 180 <= h < 240:
            r, g, b = 0, x, c
        elif 240 <= h < 300:
            r, g, b = x, 0, c
        elif 300 <= h < 360:
            r, g, b = c, 0, x
        liste_rgb.append((int((r + m) * 255), int((g + m) * 255), int((b + m) * 255)))
        draw_sorting(font, message, window, liste_rgb, a, d, radius, WHITE, NUM_SECTIONS)