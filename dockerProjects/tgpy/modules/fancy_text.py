"""
    name: fancy_text
    once: false
    origin: tgpy://module/fancy_text
    priority: 1727727904
"""
async def fancy_text(text: str):
    await ctx.msg.delete()
    message = await ctx.msg.respond("...")
    for i in range(len(text)):
        await message.edit(text[:i + 1] + "|")
        await asyncio.sleep(0.5)
    await message.edit(text)
