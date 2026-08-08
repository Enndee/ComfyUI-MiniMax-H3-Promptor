__version__ = "1.0.0"

from .py.h3_multimodal_promptor import H3_Multimodal_Promptor_Enndee

NODE_CLASS_MAPPINGS = {
    "H3_Multimodal_Promptor_Enndee": H3_Multimodal_Promptor_Enndee,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "H3_Multimodal_Promptor_Enndee": "MiniMax H3 Direct Promptor (Enndee)",
}
WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]

print(
    f"\033[34m[H3-Promptor-Enndee]\033[0m v\033[93m{__version__}\033[0m | "
    f"\033[93m{len(NODE_CLASS_MAPPINGS)} nodes\033[0m \033[92mLoaded\033[0m"
)