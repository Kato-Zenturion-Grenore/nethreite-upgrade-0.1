package com.netheriteresonante;

import java.util.EnumMap;
import java.util.Map;

import net.minecraft.resources.ResourceKey;
import net.minecraft.world.item.ToolMaterial;
import net.minecraft.world.item.equipment.ArmorMaterial;
import net.minecraft.world.item.equipment.ArmorMaterials;
import net.minecraft.world.item.equipment.ArmorType;
import net.minecraft.world.item.equipment.EquipmentAsset;
import net.minecraft.world.item.equipment.EquipmentAssets;

/**
 * Materiales de Netherite Resonante. Todas las cifras salen de las de la Netherite
 * vanilla multiplicadas por {@link #MULT}, de modo que sigan siendo coherentes con ella.
 */
public final class ResonantMaterials {
	/** Multiplicador sobre la Netherite. */
	public static final float MULT = 1.9F;

	// Valores base de la jugadora/jugador en Minecraft.
	private static final float PLAYER_BASE_DAMAGE = 1.0F;
	private static final float PLAYER_BASE_ATTACK_SPEED = 4.0F;

	private static final ToolMaterial NETHERITE_TOOL = ToolMaterial.NETHERITE;
	private static final ArmorMaterial NETHERITE_ARMOR = ArmorMaterials.NETHERITE;

	/** Herramientas: durabilidad, velocidad de minería y bonus de daño x1,9. */
	public static final ToolMaterial TOOL = new ToolMaterial(
			NETHERITE_TOOL.incorrectBlocksForDrops(),
			Math.round(NETHERITE_TOOL.durability() * MULT),
			NETHERITE_TOOL.speed() * MULT,
			NETHERITE_TOOL.attackDamageBonus() * MULT,
			NETHERITE_TOOL.enchantmentValue(),
			NETHERITE_TOOL.repairItems()
	);

	public static final ResourceKey<EquipmentAsset> ARMOR_ASSET =
			ResourceKey.create(EquipmentAssets.ROOT_ID, NetheriteResonante.id("netherite_resonante"));

	/** Armadura: protección, dureza y resistencia al retroceso x1,9. */
	public static final ArmorMaterial ARMOR = new ArmorMaterial(
			Math.round(NETHERITE_ARMOR.durability() * MULT),
			scaledDefense(),
			NETHERITE_ARMOR.enchantmentValue(),
			NETHERITE_ARMOR.equipSound(),
			NETHERITE_ARMOR.toughness() * MULT,
			NETHERITE_ARMOR.knockbackResistance() * MULT,
			NETHERITE_ARMOR.repairIngredient(),
			ARMOR_ASSET
	);

	private ResonantMaterials() {
	}

	private static Map<ArmorType, Integer> scaledDefense() {
		Map<ArmorType, Integer> map = new EnumMap<>(ArmorType.class);
		for (Map.Entry<ArmorType, Integer> entry : NETHERITE_ARMOR.defense().entrySet()) {
			map.put(entry.getKey(), Math.round(entry.getValue() * MULT));
		}
		return map;
	}

	/**
	 * Parámetro de daño de {@code Item.Properties#sword/pickaxe/...} para que el daño TOTAL
	 * mostrado de la herramienta sea exactamente x1,9 el de la Netherite.
	 * Daño total = 1 (base) + bonus del material + parámetro del arma.
	 */
	public static float attackDamage(float netheriteToolParam) {
		float netheriteTotal = PLAYER_BASE_DAMAGE + NETHERITE_TOOL.attackDamageBonus() + netheriteToolParam;
		float resonantTotal = netheriteTotal * MULT;
		return resonantTotal - PLAYER_BASE_DAMAGE - TOOL.attackDamageBonus();
	}

	/**
	 * Parámetro de velocidad de ataque para que la velocidad TOTAL (4 + parámetro) sea x1,9
	 * la de la Netherite.
	 */
	public static float attackSpeed(float netheriteToolParam) {
		float netheriteTotal = PLAYER_BASE_ATTACK_SPEED + netheriteToolParam;
		return netheriteTotal * MULT - PLAYER_BASE_ATTACK_SPEED;
	}

	/** Durabilidad de una pieza de armadura x1,9 la de la pieza de Netherite equivalente. */
	public static int armorDurability(ArmorType type) {
		return Math.round(type.getDurability(NETHERITE_ARMOR.durability()) * MULT);
	}
}
