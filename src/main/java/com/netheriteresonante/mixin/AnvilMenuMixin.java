package com.netheriteresonante.mixin;

import com.netheriteresonante.ModItems;
import org.spongepowered.asm.mixin.Final;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.Shadow;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;

import net.minecraft.world.inventory.AnvilMenu;
import net.minecraft.world.inventory.DataSlot;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.item.Items;

/**
 * Receta de yunque: Fragmento de Amatista Resonante + Aliento de Dragón
 * = Fragmento de Amatista Resonante Sobrecargada.
 *
 * Fabric no ofrece un evento de yunque, así que se intercepta {@code createResult}.
 * El consumo de materiales lo hace el propio {@code onTake} vanilla:
 *  - ranura 0 (el fragmento) se vacía,
 *  - de la ranura 1 se descuentan {@code repairItemCountCost} unidades (1 aliento de dragón).
 */
@Mixin(AnvilMenu.class)
public abstract class AnvilMenuMixin {
	/** Coste en niveles de experiencia (el yunque exige un coste mayor que 0 para poder recoger el resultado). */
	private static final int NETHERITE_RESONANTE_LEVEL_COST = 1;

	@Shadow
	private int repairItemCountCost;

	@Shadow
	@Final
	private DataSlot cost;

	@Inject(method = "createResult", at = @At("HEAD"), cancellable = true)
	private void netheriteResonante$overchargeRecipe(CallbackInfo ci) {
		AnvilMenu menu = (AnvilMenu) (Object) this;
		ItemStack left = menu.getSlot(0).getItem();
		ItemStack right = menu.getSlot(1).getItem();

		// El fragmento debe ir solo (1 unidad): vanilla vacía toda la ranura 0 al recoger el resultado.
		if (left.is(ModItems.RESONANT_AMETHYST_SHARD) && left.getCount() == 1 && right.is(Items.DRAGON_BREATH)) {
			this.repairItemCountCost = 1;
			this.cost.set(NETHERITE_RESONANTE_LEVEL_COST);
			menu.getSlot(2).set(new ItemStack(ModItems.OVERCHARGED_RESONANT_AMETHYST_SHARD));
			menu.broadcastChanges();
			ci.cancel();
		}
	}
}
