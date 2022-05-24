from typing import Type, TypeVar
import discord.ext.commands
import plugins
import discord_client

T = TypeVar("T", bound=discord.ext.commands.Cog)

def cog(cls: Type[T]) -> T:
    cog = cls()
    cog_name = "{}:{}:{}".format(cog.__module__, cog.__cog_name__, hex(id(cog)))
    cog.__cog_name__ = cog_name

    @plugins.init
    async def initialize_cog() -> None:
        await discord_client.client.add_cog(cog)
        @plugins.finalizer
        async def finalize_cog() -> None:
            await discord_client.client.remove_cog(cog_name)

    return cog
