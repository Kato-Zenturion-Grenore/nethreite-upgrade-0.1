# Netherite Resonante

Mod de Minecraft Java **26.3** para **Fabric** (Java 25). Añade la mejora *Netherite Resonante*, con estadísticas **x1,9** sobre la Netherite.

## Progresión

1. **Fragmento de Amatista Resonante** – mesa de crafteo: 8 fragmentos de amatista rodeando 1 fragmento resonante (Echo Shard).
2. **Fragmento de Amatista Resonante Sobrecargada** – yunque: Fragmento Resonante (solo, 1 unidad) + Aliento de Dragón. Cuesta 1 nivel de experiencia.
3. **Plantilla de Mejora Cristalizada** – mesa de crafteo (sin forma): Plantilla de Mejora de Netherite + Fragmento Sobrecargado.
4. **Equipamiento** – mesa de herrería (ranuras vanilla: plantilla, base, material): Plantilla Cristalizada + pieza de Netherite + Fragmento Sobrecargado. Conserva encantamientos y daño.

Piezas: espada, pico, hacha, pala, azada, casco, pechera, pantalones y botas.

## Estadísticas (x1,9 sobre Netherite)

- Herramientas: daño total, velocidad de ataque total, velocidad de minería y durabilidad.
- Armadura: puntos de protección (redondeados), dureza, resistencia al retroceso y durabilidad por pieza.

Las fórmulas están en `ResonantMaterials.java`.

## Compilar con GitHub Actions

1. Sube esta carpeta a un repositorio de GitHub (rama `main`).
2. Ve a **Actions → Compilar mod**. Se ejecuta solo en cada push.
3. Descarga el artefacto `netherite-resonante-jar` y copia `netherite_resonante-1.0.0.jar` a tu carpeta `mods`.
   También hace falta **Fabric Loader ≥ 0.19.5** y **Fabric API para 26.3**.

Si creas un tag `v1.0.0`, el workflow además publica el `.jar` en *Releases*.

## Compilar en local

```
./gradlew build      # requiere JDK 25
```

El `.jar` queda en `build/libs/`.

## Regenerar texturas, recetas y traducciones

`python3 tools/generate_assets.py` (requiere Pillow) vuelve a generar todo `src/main/resources` salvo `fabric.mod.json` y el mixin.
