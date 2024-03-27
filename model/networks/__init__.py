
class NetworksFactory(object):
    def __init__(self):
        pass

    @staticmethod
    def get_by_name(network_name, *args, **kwargs):


        if network_name == "FDAGAN":
            from .generators.FDAB_spade_resunet import FDABGenerator
            network = FDABGenerator(*args, **kwargs)

        elif network_name == "TextureWarping":
            from .generators.texture_warping_resunet import TextureWarpingGenerator
            network = TextureWarpingGenerator(*args, **kwargs)

        elif network_name == "multi_scale":
            from .discriminators import MultiScaleDiscriminator
            network = MultiScaleDiscriminator(*args, **kwargs)

        elif network_name == "patch_global":
            from .discriminators import GlobalDiscriminator
            network = GlobalDiscriminator(*args, **kwargs)

        elif network_name == "patch_global_local":
            from .discriminators import GlobalLocalDiscriminator
            network = GlobalLocalDiscriminator(*args, **kwargs)

        elif network_name == "patch_global_body_head":
            from .discriminators import GlobalBodyHeadDiscriminator
            network = GlobalBodyHeadDiscriminator(*args, **kwargs)

        else:
            raise ValueError("Network %s not recognized." % network_name)

        print("Network %s was created" % network_name)

        return network
