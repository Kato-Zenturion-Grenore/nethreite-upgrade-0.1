package com.netheriteresonante;

import net.fabricmc.api.ModInitializer;
import net.minecraft.resources.Identifier;

public class NetheriteResonante implements ModInitializer {
	public static final String MOD_ID = "netherite_resonante";

	public static Identifier id(String path) {
		return Identifier.fromNamespaceAndPath(MOD_ID, path);
	}

	@Override
	public void onInitialize() {
		ModItems.initialize();
	}
}
