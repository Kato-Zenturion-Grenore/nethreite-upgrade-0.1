package com.netheriteresonante;

import java.util.List;
import java.util.function.Function;

import net.fabricmc.fabric.api.creativetab.v1.CreativeModeTabEvents;
import net.minecraft.core.Registry;
import net.minecraft.core.component.DataComponents;
import net.minecraft.core.registries.BuiltInRegistries;
import net.minecraft.core.registries.Registries;
import net.minecraft.network.chat.Component;
import net.minecraft.resources.ResourceKey;
import net.minecraft.world.item.CreativeModeTabs;
import net.minecraft.world.item.Item;
import net.minecraft.world.item.Rarity;
import net.minecraft.world.item.component.ItemLore;
import net.minecraft.world.item.equipment.ArmorType;

public final class ModItems {
	// ---- Materiales y plantilla -------------------------------------------------
	public static final Item RESONANT_AMETHYST_SHARD = register(
			"resonant_amethyst_shard", Item::new,
			new Item.Properties().rarity(Rarity.UNCOMMON).component(DataComponents.LORE, lore("resonant_amethyst_shard")));

	public static final Item OVERCHARGED_RESONANT_AMETHYST_SHARD = register(
			"overcharged_resonant_amethyst_shard", Item::new,
			new Item.Properties().rarity(Rarity.RARE).component(DataComponents.LORE, lore("overcharged_resonant_amethyst_shard")));

	public static final Item CRYSTALLIZED_UPGRADE_TEMPLATE = register(
			"crystallized_upgrade_template", Item::new,
			new Item.Properties().rarity(Rarity.RARE).component(DataComponents.LORE, lore("crystallized_upgrade_template")));

	// ---- Herramientas (valores de Netherite vanilla entre paréntesis) ----------------
	// Espada 3.0 / -2.4, pico 1.0 / -2.8, hacha 5.0 / -3.0, pala 1.5 / -3.0, azada -4.0 / 0.0
	public static final Item RESONANT_NETHERITE_SWORD = register(
			"resonant_netherite_sword", Item::new,
			tool("resonant_netherite_sword").sword(ResonantMaterials.TOOL,
					ResonantMaterials.attackDamage(3.0F), ResonantMaterials.attackSpeed(-2.4F)));

	public static final Item RESONANT_NETHERITE_PICKAXE = register(
			"resonant_netherite_pickaxe", Item::new,
			tool("resonant_netherite_pickaxe").pickaxe(ResonantMaterials.TOOL,
					ResonantMaterials.attackDamage(1.0F), ResonantMaterials.attackSpeed(-2.8F)));

	public static final Item RESONANT_NETHERITE_AXE = register(
			"resonant_netherite_axe", Item::new,
			tool("resonant_netherite_axe").axe(ResonantMaterials.TOOL,
					ResonantMaterials.attackDamage(5.0F), ResonantMaterials.attackSpeed(-3.0F)));

	public static final Item RESONANT_NETHERITE_SHOVEL = register(
			"resonant_netherite_shovel", Item::new,
			tool("resonant_netherite_shovel").shovel(ResonantMaterials.TOOL,
					ResonantMaterials.attackDamage(1.5F), ResonantMaterials.attackSpeed(-3.0F)));

	public static final Item RESONANT_NETHERITE_HOE = register(
			"resonant_netherite_hoe", Item::new,
			tool("resonant_netherite_hoe").hoe(ResonantMaterials.TOOL,
					ResonantMaterials.attackDamage(-4.0F), ResonantMaterials.attackSpeed(0.0F)));

	// ---- Armadura -------------------------------------------------------------------
	public static final Item RESONANT_NETHERITE_HELMET = register(
			"resonant_netherite_helmet", Item::new, armor("resonant_netherite_helmet", ArmorType.HELMET));

	public static final Item RESONANT_NETHERITE_CHESTPLATE = register(
			"resonant_netherite_chestplate", Item::new, armor("resonant_netherite_chestplate", ArmorType.CHESTPLATE));

	public static final Item RESONANT_NETHERITE_LEGGINGS = register(
			"resonant_netherite_leggings", Item::new, armor("resonant_netherite_leggings", ArmorType.LEGGINGS));

	public static final Item RESONANT_NETHERITE_BOOTS = register(
			"resonant_netherite_boots", Item::new, armor("resonant_netherite_boots", ArmorType.BOOTS));

	private ModItems() {
	}

	private static Item.Properties tool(String name) {
		return new Item.Properties()
				.fireResistant()
				.rarity(Rarity.EPIC)
				.component(DataComponents.LORE, lore(name));
	}

	private static Item.Properties armor(String name, ArmorType type) {
		return new Item.Properties()
				.humanoidArmor(ResonantMaterials.ARMOR, type)
				.durability(ResonantMaterials.armorDurability(type))
				.fireResistant()
				.rarity(Rarity.EPIC)
				.component(DataComponents.LORE, lore(name));
	}

	/** Descripción traducible del objeto: clave {@code tooltip.netherite_resonante.<nombre>}. */
	private static ItemLore lore(String name) {
		return new ItemLore(List.of(Component.translatable("tooltip." + NetheriteResonante.MOD_ID + "." + name)));
	}

	private static Item register(String name, Function<Item.Properties, Item> factory, Item.Properties properties) {
		ResourceKey<Item> key = ResourceKey.create(Registries.ITEM, NetheriteResonante.id(name));
		Item item = factory.apply(properties.setId(key));
		return Registry.register(BuiltInRegistries.ITEM, key, item);
	}

	/** Carga la clase (registra los objetos) y los añade a las pestañas creativas. */
	public static void initialize() {
		CreativeModeTabEvents.modifyOutputEvent(CreativeModeTabs.INGREDIENTS).register(tab -> {
			tab.accept(RESONANT_AMETHYST_SHARD);
			tab.accept(OVERCHARGED_RESONANT_AMETHYST_SHARD);
			tab.accept(CRYSTALLIZED_UPGRADE_TEMPLATE);
		});

		CreativeModeTabEvents.modifyOutputEvent(CreativeModeTabs.TOOLS_AND_UTILITIES).register(tab -> {
			tab.accept(RESONANT_NETHERITE_PICKAXE);
			tab.accept(RESONANT_NETHERITE_AXE);
			tab.accept(RESONANT_NETHERITE_SHOVEL);
			tab.accept(RESONANT_NETHERITE_HOE);
		});

		CreativeModeTabEvents.modifyOutputEvent(CreativeModeTabs.COMBAT).register(tab -> {
			tab.accept(RESONANT_NETHERITE_SWORD);
			tab.accept(RESONANT_NETHERITE_AXE);
			tab.accept(RESONANT_NETHERITE_HELMET);
			tab.accept(RESONANT_NETHERITE_CHESTPLATE);
			tab.accept(RESONANT_NETHERITE_LEGGINGS);
			tab.accept(RESONANT_NETHERITE_BOOTS);
		});
	}
}
