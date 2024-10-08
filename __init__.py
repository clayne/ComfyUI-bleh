from .py import settings

BLEH_VERSION = 1

settings.load_settings()

if settings.SETTINGS.btp_enabled:
    from .py import betterTaesdPreview  # noqa: F401

from .py.nodes import (
    deepShrink,
    hyperTile,
    misc,
    modelPatchConditional,
    ops,
    refinerAfter,
    samplers,
)

NODE_CLASS_MAPPINGS = {
    "BlehBlockOps": ops.BlehBlockOps,
    "BlehDeepShrink": deepShrink.DeepShrinkBleh,
    "BlehDiscardPenultimateSigma": misc.DiscardPenultimateSigma,
    "BlehDisableNoise": misc.BlehDisableNoise,
    "BlehPlug": misc.BlehPlug,
    "BlehForceSeedSampler": samplers.BlehForceSeedSampler,
    "BlehHyperTile": hyperTile.HyperTileBleh,
    "BlehInsaneChainSampler": samplers.BlehInsaneChainSampler,
    "BlehLatentScaleBy": ops.BlehLatentScaleBy,
    "BlehLatentOps": ops.BlehLatentOps,
    "BlehModelPatchConditional": modelPatchConditional.ModelPatchConditionalNode,
    "BlehRefinerAfter": refinerAfter.BlehRefinerAfter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "BlehHyperTile": "HyperTile (bleh)",
    "BlehDeepShrink": "Kohya Deep Shrink (bleh)",
}

__all__ = ("BLEH_VERSION", "NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS")

from .py.nodes import blockCFG

NODE_CLASS_MAPPINGS["BlehBlockCFG"] = blockCFG.BlockCFGBleh
